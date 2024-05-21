from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import tempfile

load_dotenv()
openai_api_key = os.environ['OPENAI_API_KEY']


def load_document(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        # Copy the uploaded file to a temporary file
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name  # Get the path of the saved temp file

    # Now, you can use the path with your loader
    loader = PyPDFLoader(tmp_path)
    document = loader.load()
    return document


# laod the pdf document
def summarize(document):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(document)
    return summary


def main():
    doc_name = 'HR_Policy_Manual.pdf'
    load_doc = load_document(doc_name)
    gen_summary = summarize(load_doc)
    print(gen_summary)


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0",port=8000)
    main()