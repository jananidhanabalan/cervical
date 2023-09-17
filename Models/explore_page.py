import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

texts = {   'header1': {        
                'en': '## What is Cervical Cancer?',
                'vn': '## Ung Thư Cổ Tử Cung Là Gì?'
            },
            'definition_head': {     
                'en': '### Cervical cancer is the fourth most common cancer in women compared to other types of cancer. However, you can protect yourself by early detecting this disease.',
                'vn': '### Ung thư cổ tử cung là một trong bốn loại ung thư phổ biến nhất ở phụ nữ so với các loại ung thư khác. Tuy nhiên, bạn hoàn toàn có thể bảo vệ bản thân mình bằng cách phát hiện sớm căn bệnh này.'
            },
            'sub2header1': {    
                'en': 'Overview of Cervical Cancer',
                'vn': 'Tổng quát về bệnh ung thư cổ tử cung'
            },
            'definition': {
                'en': """Cervical cancer is a type of cancer in which abnormal cell growth occurs in the cervix, the lower part of the uterus. 
            The cervix connects the uterus to the vagina. The figure depicts a cervix with abnormal cell growth developing into a tumor
            Cervical cancer is the fourth most common cancer in women compared to other types of cancer, with an estimated 604 000 new cases and 342 000 deaths in 2020. 
            About 90% of the new cases and deaths worldwide in 2020 occurred in low- and middle-income countries.""",
                'vn': """Ung thư cổ tử cung là một loại ung thư khi các tế bào bất thường phát triển ở khu vực cổ tử cung, bộ phận bên dưới tử cung.
            Cổ tử cung kết nối tử cung và âm đạo. Hình vẽ mô tả cổ tử cung có tế bào phát triển bất thường phát triển thành khối u. 
            Ung thư cổ tử cung là loại ung thư phổ biến thứ tư ở phụ nữ so với các loại ung thư khác, ước tính có khoảng 604,000 ca mắc mới và 342,000 ca tử vong vào năm 2020.
            Khoảng 90% các trường hợp mắc mới và tử vong trên toàn thế giới vào năm 2020 xảy ra ở các nước có thu nhập thấp và trung bình."""
            },
            'readmore': {
                'en': 'Read more...',
                'vn': 'Xem thêm...'
            },
            'method_head': {
                'en': '## How does this model work?',
                'vn': '## Kết quả được tính toán như thế nào?'
            },
            'method': {
                'en': """
            Early detection of cervical cancer is crucial to reduce this disease's deadliness. 
            Several predictive models are built based on data collected from 858 women from [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets/cervical+cancer+risk+factors) with 32 features and 4 targets, 
            which are also the 4 most common tests for cervical cancer: Hinselmann, Schiller, Cytology, and Biopsy. 
    
            This dataset suffers from imbalance with only less than 9% positive patients and approximately 20% missing values. 
            Besides, 32 attributes appear redundant to feed a predictive model, which may lead to potential overfitting. Therefore, several machine learning approaches have been deployed to deal with the aforementioned problems, 
            such as feature engineering, resampling, and feature selection. The developer found that Support Vector Machine Classification, with the support of Border-SMOTE and Meta-transformer for selecting features based on importance weights for the Hinselmann, 
            shows the most outstanding performance, with 8 chosen features, generating an accuracy of 98.18%.""",
                'vn': """
            Phát hiện sớm bệnh ung thư cổ tử cung có thể giúp gia tăng cơ hội chữa lành. Một số phương pháp dự đoán đã được xây dựng dựa trên giữ liệu thu thập được từ 858 phụ nữ từ [UCI Machine Learning Repository](https://archive-beta.ics.uci.edu/ml/datasets/cervical+cancer+risk+factors)
            với 32 đặc điểm khác nhau và 4 kết quả xét nghiệm cần dự đoán, cũng là 4 phương pháp xét nghiệm ung thư cổ tử cung phổ biến nhất: Hinselmann, Schiller, Cytology, và Biopsy.

            Dữ liệu thu được có sự mất cân bằng với chỉ 9% số bệnh nhân dương tính và khoảng 20% dữ liệu thiếu thông tin.
            Bên cạnh đó, chúng ta không cần dùng toàn bộ 32 đặc tính để xây dựng mô hình dự đoán vì có thể dẫn tới việc kết quả trở nên thiếu chính xác. Vì vậy, một vài cách tiếp cận sử dụng trí tuệ nhân tạo đã được sử dụng để giải quyết những vấn đề nếu trên,
            bao gồm xử lí dữ liệu thô, giải quyết sự thiếu cân bằng dữ liệu, và loại bỏ đặc tính. Người phát triển mô hình nhận thấy phân loại sử dụng Support Vector Machine, với sự hỗ trợ của phương pháp Border-SMOTE và lựa chọn đặc tính dựa trên mức độ quan trọng cho phương pháp xét nghiệm Hinselmann
            cho ra kết quả tốt nhất, chỉ với 8 đặc tính được lựa chọn với độ chính xác là 98.18%."""
            },
            'table1': {
                'en': 'Table 1. Models with best performance for each target',
                'vn': 'Bảng 1. Mô hình với kết quả dự đoán tốt nhất cho mỗi bài xét nghiệm'
            },
            'factor_head': {
                'en': '## What Are the Risk Factors for Cervical Cancer?',
                'vn': '## Đâu là những yếu tố gây nên ung thư cổ tử cung?'
            },
            'factor_intro': {
                'en': """There are several factor that may increase your chance of having cervical cancer. 
            Each test mentioned above weights each factor differently. However, they all come to consensus with 8 most important risk factors, 
            which are asked in the predict page:""",
                'vn': """Có nhiều yếu tố làm tăng khả năng mắc ung thư cổ tử cung. Mỗi phương pháp xét nghiệm cho thấy độ quan trọng của từng yếu tố là khác nhau. Tuy nhiên,
            tất cả các phương pháp xét nghiệm đều cho thấy có 8 yếu tố quyết định hàng đầu, cũng là 8 yếu tố được hỏi ở trang dự đoán:"""
            },
            'factor': {
                'en': 
                """         
                            1. Age

                            2. Number of sexual partners

                            3. First sexual intercourse

                            4. Number of pregnancies

                            5. Use of hormonal contraceptives  

                            6. Duration of hormonal contraceptives usage

                            7. Use of IUD    

                            8. Presense of other types of cancer""",
                'vn': 
                """         
                            1. Độ tuổi

                            2. Số người quan hệ tình dục 

                            3. Tuổi khi lần đầu quan hệ tình dục

                            4. Số lần mang thai

                            5. Sử dụng thuốc tránh thai nội tiết tố 

                            6. Thời gian sử dụng thuốc tránh thai nội tiết tố

                            7. Sử dụng vòng tránh thai   
                            
                            8. Các bệnh ung thư nền khác"""
            }

}   

def show_explore_page(lan):
    st.markdown(texts['header1'][lan])
    st.markdown(texts['definition_head'][lan])

    st.write('')

    with st.container():
        image_col, text_col = st.columns((1,1))
        with image_col:
            st.image("https://www.quellerfisher.com/blog/wp-content/uploads/sites/464/2018/02/Cervical-cancer-simple-illustration.jpg")
            st.markdown("""
            [Fig. 1.](https://www.quellerfisher.com/blog/wp-content/uploads/sites/464/2018/02/Cervical-cancer-simple-illustration.jpg) Cervical Cancer illustration""")

        with text_col:
            st.subheader(texts['sub2header1'][lan])
            st.write(texts['definition'][lan])
            st.markdown(f"[{texts['readmore'][lan]}](https://www.cdc.gov/cancer/cervical/basic_info/)")

    
    st.markdown("##")
    st.markdown(texts['method_head'][lan])
 
    st.markdown(texts['method'][lan])

    st.markdown(texts['table1'][lan])

    st.write()
    
    st.markdown("""
|    Test    |                        Model                        | No of Features | Accuracy | Precision | Sensitivity | Specificity |   F-1  |
|------------|:---------------------------------------------------:|:--------------:|:--------:|:---------:|:-----------:|:-----------:|:------:|
| Hinselmann |      SVM      + Borderline-SMOTE + Meta-transformer |        8       |  98.18%  |   98.76%  |    97.55%   |    98.80%   | 98.15% |
|  Schiller  | Random Forest + Borderline-SMOTE + Meta-transformer |        7       |  96.17%  |   96.58%  |    95.27%   |    96.97%   | 95.92% |
|  Citology  |      SVM      + Borderline-SMOTE + Meta-transformer |        6       |  97.54%  |   97.65%  |    97.65%   |    97.42%   | 96.74% |
|   Biopsy   | Random Forest + Borderline-SMOTE + Meta-transformer |        8       |  96.57%  |  100.00%  |    93.13%   |   100.00%   | 96.44% |
    
    """)

    st.markdown('')
    st.markdown(texts['factor_head'][lan])

    st.markdown(texts['factor_intro'][lan])
    
    st.markdown(texts['factor'][lan])

    st.markdown('')

    with st.container():
        image1, image2 = st.columns((1,1))
        with image1:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289427117_1157939874938728_5142108399346703256_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=730e14&_nc_ohc=XcRilQctbN8AX_8c58A&tn=pP2okOx80sPGDgTM&_nc_ht=scontent-ort2-1.xx&oh=00_AT_-jxKAWqIVylOhUSZiIEdygvWZr9WVFpttJXP9imnPyQ&oe=62B4BB5B", caption='Fig. 2. Feature Importances - Hinselmann Test')
        with image2:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289285787_1157939858272063_2451351868148193044_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=730e14&_nc_ohc=jKlWEfvhlosAX8AaPPm&_nc_ht=scontent-ort2-1.xx&oh=00_AT8Hg843oVK2muBqyc66YBuiGXaRlDk3ntkOWegXvp_mWQ&oe=62B5AA43", caption='Fig. 3. Feature Importances - Schiller Test')

    with st.container():
        image1, image2 = st.columns((1,1))
        with image1:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289344790_1157939864938729_5397285092162796601_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_ohc=SilmKlWKiusAX8Qymyz&tn=pP2okOx80sPGDgTM&_nc_ht=scontent-ort2-1.xx&oh=00_AT-cUO_Ktj6sKFse8a2JGsovoPfXtdGu-86K8znjk_MBFw&oe=62B56702", caption='Fig. 4. Feature Importances - Citology Test')
        with image2:
            st.image("https://scontent-ort2-1.xx.fbcdn.net/v/t39.30808-6/289295916_1157939861605396_8182708816788922842_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_ohc=Gefp71s1K8gAX8FrAww&tn=pP2okOx80sPGDgTM&_nc_ht=scontent-ort2-1.xx&oh=00_AT_qsToD-peR_9U_uUHCZ3Ww0BUA_p9pBMuCPAks9EQ_WQ&oe=62B3ED34", caption='Fig. 5. Feature Importances - Biopsy Test')

    
    
    
    
    
    
    
    
    
    
    
    
