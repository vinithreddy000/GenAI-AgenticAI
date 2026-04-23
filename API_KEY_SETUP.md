# 🔐 API Key Configuration Guide

## Overview

This repository uses an **external configuration file** to store API keys securely. The config file is stored **outside the git repository** to prevent accidental commits of sensitive data.

## ✅ Current Setup

### Configuration File Location
```
/Users/vinith.singareddy@gmail.com/groq_config.py
```

**This file is NOT in the git repository!**

### File Structure
```python
# groq_config.py
GROQ_API_KEY = "your-actual-api-key-here"
```

---

## 🚀 How It Works

All notebooks import the API key from this external config file:

```python
import sys
sys.path.insert(0, '/Users/vinith.singareddy@gmail.com')
from groq_config import GROQ_API_KEY

# Use the API key
client = Groq(api_key=GROQ_API_KEY)
```

### Benefits

✅ **Security**: API key never gets committed to git  
✅ **Convenience**: Update key in one place, all notebooks use it  
✅ **Clean Code**: No hardcoded secrets in notebooks  
✅ **GitHub Safe**: Passes secret scanning checks  

---

## 📁 Files Modified

The following notebooks now import from the external config:

* `GenAI/Day 1.ipynb` (Cell 2 & Cell 3)
* `GenAI/Day 2.ipynb` (Cell 3)
* Future notebooks will follow the same pattern

---

## 🔧 Setup Instructions

### For New Users Cloning This Repo:

1. **Create the config file** in your user directory:
   ```bash
   nano /Users/<your-username>/groq_config.py
   ```

2. **Add your API key**:
   ```python
   # groq_config.py
   GROQ_API_KEY = "your-groq-api-key-here"
   ```

3. **Save the file** (Ctrl+O, then Ctrl+X in nano)

4. **Update notebook imports** if your username is different:
   ```python
   sys.path.insert(0, '/Users/YOUR_USERNAME')
   ```

5. **Run the notebooks** - they'll automatically use your API key!

---

## 🛡️ Security Best Practices

### ✅ DO:
* Keep `groq_config.py` in your user folder (outside git)
* Add sensitive files to `.gitignore`
* Use environment variables for production deployments
* Rotate API keys regularly

### ❌ DON'T:
* Commit API keys to git (even in comments)
* Share your `groq_config.py` file
* Hardcode API keys in notebooks
* Push config files to public repos

---

## 🔄 Updating Your API Key

1. Open the config file:
   ```bash
   nano /Users/vinith.singareddy@gmail.com/groq_config.py
   ```

2. Update the key:
   ```python
   GROQ_API_KEY = "new-api-key-here"
   ```

3. Save - all notebooks will automatically use the new key!

---

## 🐛 Troubleshooting

### Error: `ModuleNotFoundError: No module named 'groq_config'`

**Solution:**
* Make sure the config file exists at `/Users/vinith.singareddy@gmail.com/groq_config.py`
* Check the `sys.path.insert()` line has the correct path

### Error: `AttributeError: module 'groq_config' has no attribute 'GROQ_API_KEY'`

**Solution:**
* Open `groq_config.py` and verify it has:
  ```python
  GROQ_API_KEY = "your-key"
  ```
* Make sure the variable name is exactly `GROQ_API_KEY` (case-sensitive)

### Error: API authentication failed

**Solution:**
* Verify your Groq API key is valid
* Check for extra spaces or quotes in the config file
* Get a new API key from [console.groq.com](https://console.groq.com)

---

## 📝 Alternative Approaches

If you prefer different methods:

### Option 1: Environment Variables
```bash
export GROQ_API_KEY="your-key"
```

Then in notebooks:
```python
import os
api_key = os.getenv("GROQ_API_KEY")
```

### Option 2: Databricks Secrets (for production)
```python
api_key = dbutils.secrets.get(scope="groq", key="api_key")
```

### Option 3: .env File with python-dotenv
```python
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```

---

## 📚 Related Files

* `.gitignore` - Excludes sensitive files from git
* `groq_config.py` - External config (outside repo)
* `GenAI/Day 1.ipynb` - Uses external config
* `GenAI/Day 2.ipynb` - Uses external config

---

## 🤝 Contributing

When contributing to this repo:

1. **Never commit API keys** - use the external config approach
2. **Test with placeholder keys** before pushing
3. **Update this README** if you change the config approach

---

**Last Updated:** April 23, 2026  
**Maintained By:** Vinith Singareddy