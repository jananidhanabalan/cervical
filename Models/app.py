import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

texts = {   'select': {        
                'en': "Explore or Predict",
                'vn': "Tìm hiểu hay chẩn đoán"
            },
            'concern': {
                'en': 'Anh Ngo and Fleur Gahimbare',
                'vn': 'Anh Ngo & Fleur Gahimbare'
            },
            'predict': {
                'en': 'Predict',
                'vn': 'Chẩn đoán'
            },
            'explore': {
                'en': 'Explore',
                'vn': 'Tìm hiểu'
            }
}   

lan = st.sidebar.selectbox("Choose language", ['English', 'Tiếng Việt'])

if lan == 'Tiếng Việt':
    lan = 'vn'
else:
    lan = 'en'

def main(language):

    page = st.sidebar.selectbox(texts['select'][lan], (texts['predict'][lan], texts['explore'][lan]))
    st.sidebar.write(texts['concern'][lan])

    if page == texts['predict'][lan]:
        show_predict_page(lan)
    else:
        show_explore_page(lan)

main(lan)