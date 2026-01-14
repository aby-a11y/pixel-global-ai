# PixelGlobal AI Chatbot

**Repository:** https://github.com/aby-a11y/pixel-global-ai

A Flask-based AI chatbot powered by LangChain and OpenAI, with ChromaDB for vector embeddings.

## Local Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Ingest data into ChromaDB
python ingest.py

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser.

## Railway Deployment

### Steps:

1. **Push to GitHub**
   - Make sure all files are committed
   - ```bash
     git add .
     git commit -m "Ready for Railway deployment"
     git push
     ```

2. **Create Railway Project**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub"
   - Select your repository
   - Railway will automatically detect the Procfile

3. **Set Environment Variables**
   - In Railway Dashboard → Your Project → Variables
   - Add: `OPENAI_API_KEY=your_actual_api_key_here`
   - Save

4. **Deploy**
   - Railway will automatically deploy when you push to GitHub
   - Check the deployment logs in Railway Dashboard

### Important Files for Railway:

- **Procfile** - Tells Railway to run `python app.py`
- **requirements.txt** - All Python dependencies
- **.env.example** - Template for environment variables
- **DATA/** - Knowledge base (required)
- **db/** - ChromaDB vector store (will be created on first run)

### Folder Structure:

```
PixelGlobal_chatbot/
├── app.py                 # Main Flask app (RUNS ON RAILWAY)
├── chatbot.py             # CLI chatbot (local only)
├── ingest.py              # Data ingestion script
├── Procfile               # Railway configuration (NEW)
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template (NEW)
├── README.md              # This file
├── DATA/
│   ├── knowledge.txt      # Company knowledge base
│   └── SERVICES.csv       # Service pricing
├── db/                    # ChromaDB vector store
├── static/                # CSS, JS
└── templates/             # HTML templates
```

## Features

✅ AI-powered Q&A chatbot
✅ Vector search with ChromaDB
✅ Service pricing information
✅ Case studies support
✅ Company information retrieval
✅ Web UI with Flask

## Issues Fixed

- ✅ Virtual environment setup
- ✅ Retriever search parameters (k=10)
- ✅ Company information retrieval
- ✅ Railway deployment configuration
- ✅ Environment variable handling
