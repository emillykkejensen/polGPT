# PolGPT - Chat with Members of Parliament

This Streamlit app allows you to chat with Members of Parliament (MPs) using the PolGPT chatbot. The chatbot has access to meeting minutes from the Parliament.


## Getting Started

### 1. Use Docker:

```bash
docker run -e PINECONE_API_KEY=xxxxxxxxx -e PINECONE_ENV=xxxxxxxxx -e PINECONE_INDEX=xxxxxxxxx ghcr.io/emillykkejensen/polgpt:main
```


### 2. Clone the Repository

```bash
clone git@github.com:emillykkejensen/PolGPT.git
```

Then install Poetry:
[How to install Poetry](https://python-poetry.org/docs/)


install dependencies:
```bash
poetry update
```

Set Pinecone API key, environment and index name:
```python
os.environ["PINECONE_API_KEY"] = "xxxxxxxxx"
os.environ["PINECONE_ENV"] = "xxxxxxxxx"
os.environ["PINECONE_INDEX"] = "xxxxxxxxx"
```

and run streamlit:
```bash
streamlit run streamlit_app.py
```