# 🤖 AI Study Buddy - Advanced Edition

**Developed by: Kush Radhanpura**

An intelligent, feature-rich study assistant that helps students learn, understand concepts, and test their knowledge using advanced AI technology.

## ✨ Features

### Core Capabilities
- 💡 **Explain Complex Concepts**: Get simple, clear explanations with examples
- 📝 **Summarize Long Texts**: Convert notes and articles into concise summaries
- ❓ **Generate Practice Quizzes**: Create custom quizzes on any topic
- 💬 **Natural Conversation**: Chat naturally about any subject

### Advanced Features
- ⚡ **Real-time Streaming**: See responses as they're generated
- 📊 **Conversation Stats**: Track your questions and responses
- 💾 **Export Chat History**: Download conversations in JSON format
- 📋 **Quick Copy**: Copy responses with one click
- 🎯 **Example Prompts**: Get started quickly with suggested questions
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations
- 📱 **Responsive Design**: Works perfectly on all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or download the project**
   ```bash
   cd ibm_internship
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Start chatting!** The app will open in your browser automatically

## 📦 Deployment on Streamlit Cloud

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit - AI Study Buddy"
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository, branch (main), and main file (app.py)
5. Click "Deploy"

### Step 3: Add API Key (Optional)
For deployed version, you can add secrets:
1. In Streamlit Cloud dashboard, go to your app settings
2. Click "Secrets"
3. Add:
   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```

## 🎯 How to Use

1. **Start Chatting**: Type your question or click on example prompts
2. **Watch Real-time Responses**: See AI typing responses in real-time
3. **View Stats**: Track your conversation with live statistics
4. **Export or Copy**: Save your chat history or copy specific responses
5. **Clear When Done**: Start fresh conversations anytime

### Example Questions

**Learn Concepts:**
- "Explain photosynthesis in simple terms"
- "What is machine learning and how does it work?"
- "How does gravity work?"

**Summarize Content:**
- Paste any long text or notes
- "Summarize the main points of the French Revolution"

**Create Quizzes:**
- "Create a quiz on World War 2 with 5 questions"
- "Generate Python programming practice questions"
- "Quiz me on cell biology"

**General Chat:**
- "Help me understand calculus"
- "Explain the water cycle"
- "What are the benefits of renewable energy?"

## 📁 Project Structure

```
ibm_internship/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .env.example          # Example environment file
```

## 🛠️ Tech Stack

- **Frontend**: Streamlit with custom CSS styling
- **AI Model**: Advanced AI (Latest & Fastest)
- **Language**: Python 3.10
- **Developer**: Kush Radhanpura
- **Features**: Real-time streaming, conversation context, export functionality

## 🔑 API Configuration

The app is pre-configured with AI capabilities. For custom deployment:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create an API Key
4. Configure it in the app settings

## 📝 What Makes This Special

- ⚡ **Lightning Fast**: Uses Gemini 2.5 Flash for instant responses
- 🎨 **Beautiful Design**: Modern UI with gradient colors and smooth animations
- 💾 **Data Export**: Download your entire conversation history
- 📊 **Smart Analytics**: Real-time stats about your learning session
- 🚀 **Production Ready**: Optimized for deployment on Streamlit Cloud
- 🔒 **Secure**: API key safely configured in the backend

## 🤝 Contributing

This is an IBM Edunet internship project. Feel free to fork and enhance!

## 📄 License

MIT License - Feel free to use for educational purposes

## 👨‍💻 Author

**Kush Radhanpura**

Built with ❤️ for IBM Edunet Internship Project

Advanced AI-powered learning platform designed to help students learn effectively.

---

## 🌟 Screenshots & Demo

The app features:
- 🎨 Modern gradient UI design
- ⚡ Real-time streaming responses
- 📊 Live conversation statistics
- 💾 Export and download capabilities
- 🎯 Quick-start example prompts
- 📱 Fully responsive design

**Enjoy learning with your AI Study Buddy! 🚀✨**
