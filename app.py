from summarization import load_document, summarize
import streamlit as st
import os


def main():
    st.title("Document Summarizer")

    with st.sidebar:
        # File uploader allows user to add their own document
        uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:

        file_name_input = uploaded_file.name
        print('file_name_input', file_name_input)
        file_name_input, file_extension = os.path.splitext(file_name_input)
        # Assuming the document is not too large, you can read it directly
        # You might need to adjust the load_document function to handle Streamlit's UploadedFile object
        document = load_document(uploaded_file)
        if st.button("Summarize"):
            summary = summarize(document)
            st.write("Summary:")
            st.write(summary)


if __name__ == "__main__":
    main()
