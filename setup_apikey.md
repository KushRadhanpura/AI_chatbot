# 🔑 URGENT: API Key Security Setup

## ⚠️ Your Previous API Key Was Exposed!

### Immediate Actions Required:

#### 1️⃣ Regenerate Your API Key (DO THIS FIRST!)

1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. **Delete the old key** (the one that was exposed)
4. **Create a new API key**
5. Copy the new key

---

#### 2️⃣ For Local Testing:

**Option A: Use Streamlit Secrets (Recommended)**

1. Open file: `.streamlit/secrets.toml`
2. Replace `your_api_key_here` with your NEW API key:
   ```toml
   GEMINI_API_KEY = "your_new_api_key_here"
   ```
3. Save the file

**Option B: Use Environment Variable**

```bash
# Linux/Mac
export GEMINI_API_KEY="your_new_api_key_here"

# Windows (Command Prompt)
set GEMINI_API_KEY=your_new_api_key_here

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_new_api_key_here"
```

---

#### 3️⃣ For Streamlit Cloud Deployment:

When deploying on Streamlit Cloud:

1. Go to your app settings
2. Click "Secrets" section
3. Add:
   ```toml
   GEMINI_API_KEY = "your_new_api_key_here"
   ```
4. Save

---

## ✅ Security Checklist:

- [ ] Old API key deleted from Google AI Studio
- [ ] New API key generated
- [ ] New key added to `.streamlit/secrets.toml` locally
- [ ] `.gitignore` contains `.streamlit/secrets.toml`
- [ ] Changes pushed to GitHub (without the key)
- [ ] New key added to Streamlit Cloud secrets

---

## 🔒 Best Practices:

1. **NEVER** commit API keys to Git
2. **ALWAYS** use `.gitignore` for secrets files
3. **USE** environment variables or secrets management
4. **ROTATE** keys if exposed
5. **RESTRICT** API key usage (set quotas, allowed domains)

---

## 🆘 If You Need Help:

The app is now secure - it will only load API keys from:
- Streamlit secrets (`.streamlit/secrets.toml`)
- Environment variables

No hardcoded keys in the code anymore! 🎉

---

**Remember: After you get a new API key, add it to `.streamlit/secrets.toml` for local testing!**
