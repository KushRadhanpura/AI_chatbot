import streamlit as st
import google.generativeai as genai
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Configure Gemini API
# Try to get API key from Streamlit secrets first (for deployment), then use hardcoded (for local)
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    GEMINI_API_KEY = "AIzaSyD9IPnBud8-_cXeDGTzQCsfsgfuZMic-6U"

genai.configure(api_key=GEMINI_API_KEY)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'conversation_started' not in st.session_state:
    st.session_state.conversation_started = False

# Custom CSS for amazing UI
st.markdown("""
<style>
    .stApp {
        max-width: 900px;
        margin: 0 auto;
    }
    section[data-testid="stSidebar"] {
        display: none;
    }
    .stButton button {
        border-radius: 20px;
        font-weight: 500;
    }
    .suggestion-chip {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        display: inline-block;
        margin: 5px;
        cursor: pointer;
        font-size: 14px;
        transition: transform 0.2s;
    }
    .suggestion-chip:hover {
        transform: scale(1.05);
    }
    .feature-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stats-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title with gradient effect
st.markdown("""
<h1 style='text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
-webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3em;'>
🤖 AI Study Buddy
</h1>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 1.2em; color: #666;'>💬 Your intelligent AI-powered learning assistant</p>", unsafe_allow_html=True)
st.markdown("---")

# Show stats if conversation started
if st.session_state.messages:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""<div class='stats-box'>💬 Messages<br/>{len(st.session_state.messages)}</div>""", unsafe_allow_html=True)
    with col2:
        user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
        st.markdown(f"""<div class='stats-box'>❓ Questions<br/>{user_msgs}</div>""", unsafe_allow_html=True)
    with col3:
        ai_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        st.markdown(f"""<div class='stats-box'>✨ Responses<br/>{ai_msgs}</div>""", unsafe_allow_html=True)
    st.markdown("<br/>", unsafe_allow_html=True)

# Show example prompts if no conversation
if not st.session_state.messages:
    st.markdown("### ✨ Try asking me:")
    
    col1, col2 = st.columns(2)
    
    example_prompts = [
        "📚 Explain quantum physics simply",
        "💡 What is artificial intelligence?",
        "🧪 Summarize photosynthesis",
        "🎯 Create a quiz on World War 2",
        "💻 Teach me Python basics",
        "🌍 Explain climate change"
    ]
    
    for i, prompt in enumerate(example_prompts):
        if i % 2 == 0:
            with col1:
                if st.button(prompt, key=f"prompt_{i}", use_container_width=True):
                    # Trigger the prompt
                    st.session_state.example_prompt = prompt.split(" ", 1)[1]
        else:
            with col2:
                if st.button(prompt, key=f"prompt_{i}", use_container_width=True):
                    st.session_state.example_prompt = prompt.split(" ", 1)[1]
    
    st.markdown("---")
    
    # Features showcase
    st.markdown("### 🚀 Features:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-card'>
        <h4>💡 Explain Concepts</h4>
        <p>Get clear explanations of any topic</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='feature-card'>
        <h4>📝 Summarize Notes</h4>
        <p>Convert long texts to summaries</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='feature-card'>
        <h4>❓ Generate Quizzes</h4>
        <p>Create practice questions</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br/>", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle example prompt click
example_input = None
if 'example_prompt' in st.session_state and st.session_state.example_prompt:
    example_input = st.session_state.example_prompt
    st.session_state.example_prompt = None
    st.session_state.conversation_started = True

# Chat input
user_input = st.chat_input("Ask me anything... 💭")

# Process input (either from text or example button)
if user_input or example_input:
    current_input = user_input if user_input else example_input
    
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": current_input})
    st.session_state.conversation_started = True
    
    with st.chat_message("user"):
        st.markdown(current_input)
    
    # Generate AI response with streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("💭 Thinking..."):
            try:
                # Use gemini-2.5-flash (faster and has better quota availability)
                model = genai.GenerativeModel('models/gemini-2.5-flash')
                
                # Generate response with streaming
                response = model.generate_content(current_input, stream=True)
                
                # Stream the response
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        message_placeholder.markdown(full_response + "▌")
                
                # Show final response
                message_placeholder.markdown(full_response)
                
                # Add to chat history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                error_msg = f"⚠️ Sorry, I encountered an error: {str(e)}"
                message_placeholder.error(error_msg)
                st.info("💡 Tip: Try asking a different question or wait a moment before trying again.")
        
        # Rerun to update stats and clear example prompt trigger
        if example_input:
            st.rerun()

# Bottom controls
if st.session_state.messages:
    st.markdown("---")
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.conversation_started = False
            st.rerun()
    
    with col2:
        if st.button("📥 Export Chat", use_container_width=True):
            chat_export = {
                "export_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "total_messages": len(st.session_state.messages),
                "conversation": st.session_state.messages
            }
            st.download_button(
                label="💾 Download JSON",
                data=json.dumps(chat_export, indent=2),
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
    
    with col3:
        if st.button("📋 Copy Last Response", use_container_width=True):
            if st.session_state.messages:
                last_ai_msg = [m for m in st.session_state.messages if m["role"] == "assistant"]
                if last_ai_msg:
                    st.code(last_ai_msg[-1]["content"], language="text")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>🚀 <b>AI Study Buddy</b> - Intelligent Learning Platform</p>
    <p style='font-size: 0.9em;'>Developed by <b>Kush Radhanpura</b> | IBM Edunet Internship Project 2026</p>
    <p style='font-size: 0.85em;'>🎓 Empowering Students to Learn Better</p>
</div>
""", unsafe_allow_html=True)
