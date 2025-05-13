from serpapi import GoogleSearch
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bf
import requests
from flask_app.rag import setup_langchain


load_dotenv()

fetched_results = []


def search_articles(query):
    
    global fetched_results

    params = {
        "engine": "google",
        "q": query,
        "api_key": os.getenv("SEARCH_API_KEY") 
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Accessing top results
    for result in results.get("organic_results", []):
        page = [result.get("title"),result.get("link")]
        fetched_results.append(page) 
    
    return fetched_results # returns a list like [[page title, URL],[page title, URL]....]

def content_scrape(fetched_results):
    """Takes a list of search results page title and their URLs and scraps the headings and paragraphs out of them"""
    content = "" # The final string that will be given to LLM

    for result in fetched_results:
        url = result[1]
        response = requests.get(url,timeout = 10)
        soup = bf(response.text,"html.parser")
        elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6','p'])
        
        for tag in elements:
            text = tag.get_text(strip=True)
            if not text:
                continue  # skipping empty text
            if tag.name.startswith('h'):
                content += f"\n\n### {text}\n"
            elif tag.name == 'p':
                content += f"{text}\n"
        
    return content.strip()

qa_chain = None  # Global so memory persists between calls

def generate_answer(content, query):
    global qa_chain

    if qa_chain is None:
        qa_chain = setup_langchain(content)

    if isinstance(qa_chain, str):  # Checking if error message returned
        return qa_chain

    return qa_chain.run(query)

