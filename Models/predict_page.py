from dis import code_info
import streamlit as st
import numpy as np
import pandas as pd
from hinselmann import hinselmann_model
from schiller import schiller_model
from citology import citology_model
from biopsy import biopsy_model


texts = {   'header': {         
                'en':'CSC 410: Cervical Cancer Detection Page',
                'vn':'CSC 410: Chẩn Đoán Ung Thư Cổ Tử Cung'
            },
            'subheader': {      
                'en':'Information collected from respondents is kept ***strictly confidential***.',
                'vn':'Thông tin thu thập từ người dùng được ***bảo mật tuyệt đối***.'
            },
            'subheader1': {     
                'en':'We do not collect your information, nor your test result.',
                'vn':'Chúng tôi không thu thập thông tin từ người dùng, kể cả kết quả dự đoán từ website.'
            },
            'age': {            
                'en': 'Enter your age',
                'vn': 'Nhập tuổi của bạn'
            },
            'sexual_partner': { 
                'en': 'How many sexual partners have you had?',
                'vn': 'Bạn đã và đang quan hệ tình dục với bao nhiêu người?'
            },
            'intercourse': {    
                'en': 'When was your first sexual intercourse (age)? (If N/A, put 0)',
                'vn': 'Bạn quan hệ tình dục lần đầu tiên vào năm bao nhiêu tuổi? (Điền 0 nếu không có thông tin)'
            },
            'pregnancy': {      
                'en': 'How many times have you been pregnant?',
                'vn': 'Bạn đã, và đang mang thai bao nhiêu lần?'
            },
            'hmc':  {           
                'en': 'Have you used Hormonal Contraceptive?',
                'vn': 'Bạn có đang sử dụng thuốc tránh thai nội tiết tố không?'
            },
            'hmc_year': {       
                'en': 'If yes, how long have you used hormonal contraceptive (year)?',
                'vn': 'Nếu có, bạn đã sử dụng thuốc tránh thai nổi tiết tố bao lâu (năm)?'
            },
            'IUD':  {           
                'en': 'Have you used IUD?',
                'vn': 'Bạn có đã, hoặc đang sử dụng vòng tránh thai không?'
            },
            'cancer': {         
                'en': 'Have you had any types of cancer?',
                'vn': 'Bạn đã, hoặc đang mắc các bệnh ung thư nào không?'
            },
            'yes':  {           
                'en': 'Yes',
                'vn': 'Có'},
            'no':  {            
                'en': 'No',
                'vn': 'Không'
            },                                
            'side_header': {    
                'en': 'Cervical Cancer Detection',
                'vn': 'Chẩn Đoán Ung Thư Cổ Tử Cung'
            },
            'side_subhead': {   
                'en': '### We need some information to predict your cervical health status',
                'vn': '### Chúng tôi cần một vài thông tin để dự đoán tình trạng sức khỏe cổ tử cung của bạn'
            },
            'predict':  {       
                'en': 'Predict',
                'vn': 'Chẩn đoán'
            },
            'negative': {       
                'en': 'Negative',
                'vn': 'Âm tính'
            },
            'positive': {       
                'en': 'Positive',
                'vn': 'Dương tính'
            },
            '1_4_test': {       
                'en': '1/4 tests predicts that you are at risk of having cervical cancer.',
                'vn': '1/4 bài test dự đoán bạn đang có nguy cơ mắc ung thư cổ tử cung.'
            },
            'morethan4': {      
                'en': '/4 tests predict that you are at risk of having cervical cancer.',
                'vn': '/4 bài test dự đoán bạn đang có nguy cơ mắc ung thư cổ tử cung.'
            },
            '0_test':   {       
                'en': 'You are predictedly negative with cervical cancer. Please have regular check-ups.',
                'vn': 'Bạn được dự đoán âm tính với ung thư cổ tử cung. Vui lòng kiểm tra sức khỏe định kỳ.'
            }       
        }
                       


def user_input(lan):

    st.header(texts['header'][lan])

    st.subheader(texts['subheader'][lan])
    st.write(texts['subheader1'][lan])

    age = st.number_input(texts['age'][lan], min_value=0, max_value=100)
    
    sexual_partner = st.slider(texts['sexual_partner'][lan], 0, 20)

    first_intercourse = st.number_input(texts['intercourse'][lan], min_value=0, max_value=100)

    pregnancy = st.slider(texts['pregnancy'][lan], 0, 10)

    hmc = st.selectbox(texts['hmc'][lan], [texts['no'][lan], texts['yes'][lan]])

    if hmc == texts['yes'][lan]:
        hmc = 1
        hmc_year = st.number_input(texts['hmc_year'][lan])
    else:
        hmc = 0
        hmc_year = 0

    IUD = st.selectbox(texts['IUD'][lan], [texts['no'][lan], texts['yes'][lan]])
    if IUD == texts['yes'][lan]:
        IUD = 1
    else:
        IUD = 0

    cancer = st.selectbox(texts['cancer'][lan], [texts['no'][lan], texts['yes'][lan]])
    if cancer == texts['yes'][lan]:
        cancer = 1
    else:
        cancer = 0


    hinselmann = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year, IUD, cancer]).reshape(1, 8)
    schiller = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year, IUD]).reshape(1, 7)
    citology = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year]).reshape(1, 6)
    biopsy = np.array([age, sexual_partner, first_intercourse, pregnancy, hmc, hmc_year, IUD, cancer]).reshape(1, 8)

    return {'hinselmann': hinselmann, 'schiller': schiller, 'citology': citology, 'biopsy': biopsy}

def check_cancer(lan, result):
    count = 0
    for i in result:
        if i == texts['positive'][lan]:
            count += 1
    
    if count == 1:
        return texts['1_4_test'][lan]
    elif count > 1:
        return f'{count}{texts["morethan4"][lan]}'

    return texts['0_test'][lan]

def show_predict_page(lan):

    st.sidebar.title(texts['side_header'][lan])

    st.sidebar.write(texts['side_subhead'][lan])

    info = user_input(lan)

    st.write(pd.DataFrame(info['hinselmann'],columns=['Age','Number of sexual partners',
       'First sexual intercourse', 'Num of pregnancies','Hormonal Contraceptives',
       'Hormonal Contraceptives (years)', 'IUD','Dx:Cancer']))

    if st.button(texts['predict'][lan]):
        # hinselmann_test
        model_hinselmann = hinselmann_model()
        prediction_hinselmann = model_hinselmann.predict(info['hinselmann'])
        if prediction_hinselmann == np.array([0]):
            prediction_hinselmann = texts['negative'][lan]
        else: 
            prediction_hinselmann = texts['positive'][lan]
        # st.subheader(f"Your Hinselmann test predicted result is: {prediction_hinselmann}")

        # schiller_test
        model_schiller = schiller_model()
        prediction_schiller = model_schiller.predict(info['schiller'])
        if prediction_schiller == np.array([0]):
            prediction_schiller = texts['negative'][lan]
        else: 
            prediction_schiller = texts['positive'][lan]
        # st.subheader(f"Your Schiller test predicted result is: {prediction_hinselmann}")

        # citology_test
        model_citology = citology_model()
        prediction_citology = model_citology.predict(info['citology'])
        if prediction_citology == np.array([0]):
            prediction_citology = texts['negative'][lan]
        else: 
            prediction_citology = texts['positive'][lan]
        # st.subheader(f"Your Citology test predicted result is: {prediction_hinselmann}")
        
        # biopsy_test
        model_biopsy = biopsy_model()
        prediction_biopsy = model_biopsy.predict(info['biopsy'])
        if prediction_biopsy == np.array([0]):
            prediction_biopsy = texts['negative'][lan]
        else: 
            prediction_biopsy = texts['positive'][lan]
        # st.subheader(f"Your Biopsy test predicted result is: {prediction_hinselmann}")


        result_collection = np.array([prediction_hinselmann, prediction_schiller, 
                                prediction_citology, prediction_biopsy])
        result = pd.DataFrame(result_collection.reshape(1,4),
                                columns=['Hinselmann test', 'Schiller test', 'Citology test', 'Biopsy test'],index=['Result'])
        
        st.table(result)

        st.header(check_cancer(lan, result_collection))

if __name__ == "__main__":
    show_predict_page()