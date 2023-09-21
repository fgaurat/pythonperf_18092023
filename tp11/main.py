import streamlit as st
from PersonDAO import PersonDAO

def main():
    st.set_page_config(layout="wide")
    st.title('This is a title')
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    st.write('## This is a title')
    dao = PersonDAO("persons.db")
    p =dao.findAll()

    title = st.text_input('Movie title', 'Life of Brian')
    if st.button("Show"):
        st.write('The current movie title is', title)
    
    st.table(p)


if __name__=='__main__':
    main()
