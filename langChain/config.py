import os
from dotenv import load_dotenv

load_dotenv()


os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = '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'
os.environ["OPENAI_API_KEY"] = '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'
os.environ['GOOGLE_API_KEY'] = 'AIzaSyDOFJ0_MKoCK4qAfiyFGTXDjKXrZhIH2e4'
