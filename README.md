# Confidant

# LLM-Based Web Search Assistant (RAG Pipeline with LangChain)

This project is an end-to-end system that retrieves live web content, processes it, and generates intelligent responses using a Large Language Model (LLM). It employs a Retrieval-Augmented Generation (RAG) approach to answer user queries based on real-time internet data.

---

## 🔧 Project Structure

```
llm_search_template/
├── flask_app/
│   ├── __init__.py
│   ├── app.py              # Flask backend API
│   └── utils.py            # Core functions: search, scrape, preprocess, LLM
├── streamlit_app/
│   └── app.py              # Front-end interface using Streamlit
├── .env                    # API keys and environment variables
├── requirements.txt        # Dependencies
├── README.md               # Project instructions (this file)
```

---

## 🚀 Features

- 🔍 Live web search using SerpAPI
- 🧠 Text summarization and Q&A using OpenAI (or any LLM)
- 🕸️ Web scraping with BeautifulSoup for relevant paragraphs/headings
- 💬 Interactive Streamlit interface
- 🧩 LangChain memory integration (bonus)

---

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/llm-search-template.git
cd llm-search-template
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_key_here
SERPAPI_API_KEY=your_serpapi_key_here
```

---

## ⚙️ How It Works

### 1. Streamlit Frontend (`streamlit_app/app.py`)
- Takes user query via input box
- Shows “Typing…” status
- Sends query to Flask API (`/api`) using `requests.post`

### 2. Flask Backend (`flask_app/app.py`)
- Receives the query
- Calls helper functions from `utils.py`:
  - `search_web(query)`: Uses SerpAPI to fetch top URLs
  - `scrape_and_clean(urls)`: Extracts headings and paragraphs using BeautifulSoup
  - `generate_response(content, query)`: Uses OpenAI to answer based on context

### 3. Display Result
- The response is returned to Streamlit and displayed to the user.
- Clears the "Typing..." message once the response is ready.

---

## 🌍 Deployment Guide

### Local

1. Run backend:
   ```bash
   cd flask_app
   flask run
   ```

2. Run frontend:
   ```bash
   cd ../streamlit_app
   streamlit run app.py
   ```

### External Hosting

If deployed (e.g., on Render, AWS, Railway):
- Replace `http://localhost:5000/api` in Streamlit with your deployed backend URL.

---

## 🧠 Bonus: LangChain Integration

If enabled, LangChain allows the assistant to remember past queries in the same session.

- Adds conversational context
- Helps follow-up questions make sense
- Requires setting up a simple memory chain using `ConversationBufferMemory`

---

## 📌 Example Flow

1. User asks: “What are the latest advancements in cancer treatment?”
2. System:
   - Searches the web for relevant articles
   - Extracts readable content
   - Sends processed content + query to OpenAI
3. LLM responds with a synthesized answer based on fresh content.

---

## ✅ Future Enhancements

- Add authentication
- Save user sessions
- Support file uploads and voice queries
- Integrate vector databases (e.g., FAISS) for custom corpora

---

## 🙌 Acknowledgements

- [OpenAI](https://openai.com/)
- [SerpAPI](https://serpapi.com/)
- [LangChain](https://github.com/hwchase17/langchain)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
