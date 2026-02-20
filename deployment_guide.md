# 🚀 Deployment Guide - AI Study Buddy

## Option 1: Streamlit Cloud (RECOMMENDED - FREE)

### Prerequisites:
- GitHub account
- Streamlit Cloud account (free)

### Step-by-Step:

#### 1️⃣ Push to GitHub

```bash
# Initialize git (if not already done)
cd /home/kushsoni/Desktop/ibm_internship
git init

# Add all files
git add .

# Commit
git commit -m "AI Study Buddy - IBM Edunet Project by Kush Radhanpura"

# Create a new repository on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/ai-study-buddy.git
git branch -M main
git push -u origin main
```

#### 2️⃣ Deploy on Streamlit Cloud

1. Go to: https://share.streamlit.io/
2. Click "Sign in" → Sign in with GitHub
3. Click "New app"
4. Fill in:
   - **Repository**: Select your `ai-study-buddy` repo
   - **Branch**: main
   - **Main file path**: app.py
5. Click "Advanced settings" (optional)
6. Add secrets (copy from `.streamlit/secrets.toml`):
   ```toml
   GEMINI_API_KEY = "AIzaSyD9IPnBud8-_cXeDGTzQCsfsgfuZMic-6U"
   ```
7. Click "Deploy"!

#### 3️⃣ Your App is Live! 🎉

You'll get a URL like: `https://your-app-name.streamlit.app`

---

## Option 2: Local Deployment (For Testing)

```bash
# Run locally
streamlit run app.py
```

Access at: http://localhost:8501

---

## Option 3: Docker Deployment (Advanced)

Create `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Then:
```bash
docker build -t ai-study-buddy .
docker run -p 8501:8501 ai-study-buddy
```

---

## 📝 Important Notes:

### Security:
- ✅ API key is now handled securely via Streamlit secrets
- ✅ `.gitignore` excludes `.streamlit/secrets.toml`
- ⚠️ Never commit API keys to public GitHub repos

### For Submission:
- Share the live Streamlit Cloud URL
- Include GitHub repository link
- Add screenshots in PPT

---

## 🆘 Troubleshooting:

**Issue**: App doesn't start
- Check requirements.txt has all dependencies
- Verify API key is correct in secrets

**Issue**: Rate limit errors
- Gemini free tier has limits
- Wait a few minutes and try again

**Issue**: GitHub push fails
- Make sure you created the repo on GitHub.com first
- Check your GitHub credentials

---

## 📧 Support

Developed by: **Kush Radhanpura**
Project: IBM Edunet Internship

Good luck with your deployment! 🚀
