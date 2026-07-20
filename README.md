<div align="center">

# 🧠 Memora Extension

### **Browse Everything. Forget Nothing.**

An AI-powered Chrome Extension that intelligently captures webpages, generates AI summaries, creates semantic embeddings, and stores everything as searchable memories.

---

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Chrome Extension](https://img.shields.io/badge/Chrome%20Extension-MV3-yellow?style=for-the-badge&logo=googlechrome)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-000000?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge)

</div>

---

# 📖 About

Memora Extension is an AI-powered Chrome extension that lets users save any webpage with a single click. Every saved page is processed using AI to generate concise summaries and semantic embeddings, making previously visited content instantly searchable through natural language.

Instead of relying on bookmarks or browser history, Memora builds a searchable knowledge base of everything you browse.

---

# ✨ Features

- 🔐 Secure JWT Authentication
- 🌐 Save Current Webpage
- 🤖 AI Generated Summary
- 🧠 Semantic Search using Embeddings
- 💾 Automatic Memory Storage
- 📚 ChromaDB Vector Database
- 🗄️ MySQL Database
- ⚡ FastAPI Backend
- 🏷️ Tags Support
- ⭐ Favorite Memories
- 🔍 Intelligent Memory Retrieval

---

# 🏗️ Architecture

```text
                Chrome Extension
                       │
                       ▼
            Extract Current Webpage
                       │
                       ▼
                FastAPI Backend
                       │
      ┌────────────────┼────────────────┐
      ▼                ▼                ▼
 Google Gemini      MySQL         ChromaDB
  AI Summary      Metadata      Vector Search
      │                │                │
      └────────────────┼────────────────┘
                       ▼
               Semantic Search
```

---

# 🚀 Tech Stack

## Extension

- Vanilla JavaScript
- HTML5
- CSS3
- Chrome Extension Manifest V3

## Backend

- FastAPI
- SQLAlchemy
- MySQL
- ChromaDB
- Sentence Transformers
- Google Gemini API
- JWT Authentication
- Pydantic

---

# 📂 Project Structure

```text
memora_extension/

├── backend/
│   ├── app/
│   ├── chroma_db/
│   ├── requirements.txt
│   └── main.py
│
├── extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   ├── popup.css
│   ├── api.js
│   ├── auth.js
│   ├── memory.js
│   ├── content.js
│   ├── background.js
│   └── icons/
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/snehal1805-dev/memora_extension.git

cd memora_extension
```

---

## Backend Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the backend

```bash
uvicorn app.main:app --reload
```

---

## Chrome Extension Setup

1. Open Chrome
2. Visit

```
chrome://extensions
```

3. Enable **Developer Mode**
4. Click **Load unpacked**
5. Select the **extension** folder

---

# 📸 Screenshots

## Login

> *(Add Screenshot Here)*

---

## Save Current Page

> *(Add Screenshot Here)*

---

## Success Message

> *(Add Screenshot Here)*

---

## Search Memories

> *(Add Screenshot Here)*

---

# 🔄 Workflow

```text
Open Any Website
        │
        ▼
Click Save
        │
        ▼
Extract Webpage Content
        │
        ▼
Generate AI Summary
        │
        ▼
Create Embeddings
        │
        ▼
Store Metadata in MySQL
        │
        ▼
Store Vectors in ChromaDB
        │
        ▼
Semantic Search Ready
```

---

# 🌟 Future Roadmap

- [ ] Auto Save Browsing History
- [ ] AI Chat with Memories
- [ ] Smart Collections
- [ ] Browser History Timeline
- [ ] Read Later
- [ ] Memory Analytics
- [ ] Cross Device Sync

---

# 👨‍💻 Developer

**Snehal Matole**

GitHub

https://github.com/snehal1805-dev

---

**Samruddhi Pawde**

Github

https://github.com/samruddhipawde

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further development.

---

<div align="center">

### 🧠 Memora

**Browse Everything. Forget Nothing.**

Made with ❤️ using FastAPI, AI and Chrome Extensions.

</div>