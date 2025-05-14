import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS 
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter

from openai import RateLimitError, AuthenticationError, OpenAIError

def setup_langchain(content):
    # 1. Loading OpenAI API key explicitly
    load_dotenv()  # Loading from .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        print("❌ OPENAI_API_KEY not found in .env")
        return "API key missing. Please check your .env file."

    print(f"✅ Loaded API key: {openai_api_key[:8]}...")

    # 2. Splitting content into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    docs = splitter.create_documents([content])

    # 3. Creating embeddings
    try:
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vectorstore = FAISS.from_documents(docs, embeddings)
    # except RateLimitError:
    #     print("⚠️ Embedding rate limit hit or quota exhausted.")
    #     return "Quota exceeded. Please wait and try again."
    except AuthenticationError:
        print("❌ Authentication failed. Invalid API key.")
        return "Authentication failed. Please check your API key."
    except OpenAIError as e:
        print(f"❌ OpenAI API error: {e}")
        return f"OpenAI error: {e}"
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return f"Unexpected error: {e}"

    # 4. Setting up memory and retriever
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 5. Creating QA chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=openai_api_key),
        retriever=retriever,
        memory=memory,
        verbose=True
    )

    return qa_chain
