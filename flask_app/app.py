from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import flask_app.utils

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    


    # get the data/query from streamlit app
    print("Received query")
    data = request.get_json()
    query = data["query"]
    
    # Step 1: Search and scrape articles based on the query
    print("Step 1: searching articles")
    task = flask_app.utils
    fetched_results = task.search_articles(query)
    
    # Step 2: Concatenate content from the scraped articles
    print("Step 2: concatenating content")
    content = task.content_scrape(fetched_results)

    # Step 3: Generate an answer using the LLM
    print("Step 3: generating answer")
    answer = task.generate_answer(content, query)

    # return the jsonified text back to streamlit
    return answer

if __name__ == '__main__':
    app.run(host='localhost')
