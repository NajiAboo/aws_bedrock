import streamlit as st
import ingenstion as data


st.set_page_config(page_title="Q&A with RAG")
st.markdown("<p> Q&A with RAG</p",unsafe_allow_html=True)


if 'vector_store' not in st.session_state:
    with st.spinner("Please wait.. we are loading data "):
        st.session_state.vector_store = data.create_index()


input_text = st.text_area("input text", label_visibility="collapsed")
go_button = st.button("RAG", type="primary")


if go_button:
    with st.spinner("We are getitng the answer"):
        response = data.rag_response(index=st.session_state.vector_store, question=input_text)
        st.write(response)