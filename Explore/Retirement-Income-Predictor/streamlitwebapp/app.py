import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
import requests


CatBoost = pickle.load(open('cat_base_model.pkl', 'rb'))
st.set_page_config(page_title="RETIREMENT INCOME PREDICTOR", page_icon=":tada:", layout="wide")


#-------------CREATING THE LOTTIE FUNCTION-------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#--------------USE LOCAL CSS TO STRUCTURE CONTACT US FORM-----------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)       
local_css("style/style.css")

#--------------LOAD ASSESTS FOR THE LOTTIE IMAGES------------------
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_l1qryt3o.json")
lottie_coding2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ksklhijl.json")
lottie_coding3 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ANc3UcnG19.json")

#-------------INSERTING THE COMPANY HEADER IMAGE-----------
image = Image.open('exploreai.png')
st.image(image)
st.subheader("Impact, at scale")


#-------------INSERTING THE OPTION MENU------------
selected = option_menu(
    menu_title = None, #-----requred
    options = ["Home", "About Us", "Contact Us"], #-----required
    icons = ["house", "info-circle", "envelope"],
    default_index = 0,
    orientation = "horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "white", "font-size": "18px"}, 
            "nav-link": {
                "font-size": "18px", 
                "text-align": "left", 
                "margin":"0px", 
                "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#152238"},
        }
    )




#---------------HEADER SECTION---------------
if selected == "Home":
    st.sidebar.title("RETIREMENT INCOME PREDICTOR")
    regressor_name = st.sidebar.selectbox("SELECT MODEL", ("CatBoost", "XGBoost", "Light GBM"))
    st.sidebar.header('INDIVIDUAL DATA')



#--------------CREATING FUNCTION FOR DATAFRAME--------------
    def user_info():
        Unnamed_0 = st.sidebar.number_input('USER ID')
        GENDER = st.sidebar.number_input('GENDER - Value between 0 & 1')
        RETIREMENT_AGE = st.sidebar.number_input('RETIREMENT AGE')
        RETIREMENT_FUND_VALUE = st.sidebar.number_input('RETIREMENT FUND VALUE - values between 500,000 & 15,000,000')
        DEPT_VALUE = st.sidebar.number_input('DEPT_VALUE - values between 32 & 250,000')
        CURRENT_NET_MONTHLY_INCOME = st.sidebar.number_input('CURRENT NET MONTHLY INCOME - values between 0 & 7,500')
        SPARE_CASH_VALUE = st.sidebar.number_input('SPARE CASH VALUE - values between 20 & 250,000')
        FINANCIALLY_SUPPORT_PARTNER = st.sidebar.number_input('FINANCIALLY SUPPORT PARTNER - 0 for Yes and 1 for No')
        FINANCIALLY_SUPPORT_CHILDREN = st.sidebar.number_input('FINANCIALLY SUPPORT CHILDREN  - 0 for Yes and 1 for No')
        YEARS_SUPPORTING_CHILD = st.sidebar.number_input('YEARS SUPPORTING CHILD - values between 0 & 4')
        CHILD_MONTHLY_SUPPORTING_VALUE = st.sidebar.number_input('CHILD MONTHLY SUPPORTING VALUE - values between 0 & 4,500')
        YEARS_SUPPORTING_SOMEONE_ELSE = st.sidebar.number_input('YEARS SUPPORTING SOMEONE ELSE - values between 0 & 4')
        OTHER_MONTHLY_SUPPORTING_VALUE = st.sidebar.number_input('OTHER MONTHLY SUPPORTING VALUE - values between 0 & 4,500')
        HAS_EMERGENCY_SAVINGS = st.sidebar.number_input('HAS EMERGENCY SAVINGS - 0 for Yes and 1 for No')
        CRITICAL_ILLNESS = st.sidebar.number_input('CRITICAL ILLNESS - 0 for Yes and 1 for No')
        ONGOING_COACHING_FEE = st.sidebar.number_input('ONGOING COACHING FEE - values between 0 & 3')
        CONFIDENCE_LEVEL = st.sidebar.number_input('CONFIDENCE LEVEL - values between 65 & 75')
        INITIAL_PLANNER_FEE_INCL_VAT_UT = st.sidebar.number_input('INITIAL PLANNER FEE UT - values between 0 & 5')
        INITIAL_PLANNER_FEE_INCL_VAT_LA_AND_LAP = st.sidebar.number_input('INITIAL PLANNER FEE LA AND LAP - values between 0 & 5')
        ONGOING_PLANNER_FEE_INCL_VAT_UT = st.sidebar.number_input('ONGOING PLANNER FEE UT - values between 0 & 3')
        ONGOING_PLANNER_FEE_INCL_VAT_LA_AND_LAP = st.sidebar.number_input('ONGOING PLANNER FEE LA AND LAP - values between 0 & 3')
        SPOUSE_GENDER = st.sidebar.number_input('SPOUSE GENDER  - 0 for Yes and 1 for No')
        SPOUSE_RETIREMENT_AGE = st.sidebar.number_input('SPOUSE RETIREMENT AGE')
        SPOUSE_DATE_OF_BIRTH = st.sidebar.number_input('SPOUSE DATE OF BIRTH')
        PERCENTAGE_SUCCESS = st.sidebar.number_input('PERCENTAGE SUCCESS - values between 0 & 100')
        SA_EQUITY_UNIT_TRUST = st.sidebar.number_input('SA EQUITY UNIT TRUST - values between 0 & 100')
        SA_BOND_UNIT_TRUST = st.sidebar.number_input('SA BOND UNIT TRUST - values between 0 & 100')
        SA_CASH_UNIT_TRUST = st.sidebar.number_input('SA CASH UNIT TRUST - values between 0 & 100')
        INTERNATIONAL_EQUITY_UNIT_TRUST = st.sidebar.number_input('INTERNATIONAL EQUITY UNIT TRUST - values between 0 & 100')
        INTERNATIONAL_BOND_UNIT_TRUST = st.sidebar.number_input('INTERNATIONAL BOND UNIT TRUST - values between 0 & 50')
        INTERNATIONAL_CASH_UNIT_TRUST = st.sidebar.number_input('INTERNATIONAL CASH UNIT TRUST - values between 0 & 10')
        SA_EQUITY_LAP = st.sidebar.number_input('SA EQUITY LAP - values between 0 & 100')
        SA_BOND_LAP = st.sidebar.number_input('SA BOND LAP - values between 0 & 100')
        SA_CASH_LAP = st.sidebar.number_input('SA CASH LAP - values between 0 & 100')
        INTERNATIONAL_EQUITY_LAP = st.sidebar.number_input('INTERNATIONAL EQUITY LAP - values between 0 & 100')
        INTERNATIONAL_BOND_LAP = st.sidebar.number_input('INTERNATIONAL BOND LAP - values between 0 & 100')
        INTERNATIONAL_CASH_LAP = st.sidebar.number_input('INTERNATIONAL CASH LAP - values between 0 & 10')
        LAP_EAC_PA_INCL_VAT = st.sidebar.number_input('LAP EAC PA - values between 0 & 10')
        LA_EAC_PA_INCL_VAT = st.sidebar.number_input('LA EAC PA - values between 0 & 10')
        UNIT_TRUST_EAC_PA_INCL_VAT = st.sidebar.number_input('UNIT TRUST EAC PA - values between 0 & 10')
        
        
        
        user_info_data = {
            'Unnamed_0': Unnamed_0,
            'GENDER': GENDER,
            'RETIREMENT_AGE':RETIREMENT_AGE,
            'RETIREMENT_FUND_VALUE':RETIREMENT_FUND_VALUE,
            'DEPT_VALUE':DEPT_VALUE,
            'CURRENT_NET_MONTHLY_INCOME':CURRENT_NET_MONTHLY_INCOME,
            'SPARE_CASH_VALUE':SPARE_CASH_VALUE,
            'FINANCIALLY_SUPPORT_PARTNER':FINANCIALLY_SUPPORT_PARTNER,
            'FINANCIALLY_SUPPORT_CHILDREN':FINANCIALLY_SUPPORT_CHILDREN,
            'FINANCIALLY_SUPPORT_CHILDREN':FINANCIALLY_SUPPORT_CHILDREN,
            'YEARS_SUPPORTING_CHILD':YEARS_SUPPORTING_CHILD,
            'CHILD_MONTHLY_SUPPORTING_VALUE':CHILD_MONTHLY_SUPPORTING_VALUE,
            'YEARS_SUPPORTING_SOMEONE_ELSE':YEARS_SUPPORTING_SOMEONE_ELSE,
            'OTHER_MONTHLY_SUPPORTING_VALUE':OTHER_MONTHLY_SUPPORTING_VALUE,
            'HAS_EMERGENCY_SAVINGS':HAS_EMERGENCY_SAVINGS,
            'CRITICAL_ILLNESS':CRITICAL_ILLNESS,
            'ONGOING_COACHING_FEE':ONGOING_COACHING_FEE,
            'CONFIDENCE_LEVEL':CONFIDENCE_LEVEL,
            'INITIAL_PLANNER_FEE_INCL_VAT_UT':INITIAL_PLANNER_FEE_INCL_VAT_UT,
            'INITIAL_PLANNER_FEE_INCL_VAT_LA_AND_LAP':INITIAL_PLANNER_FEE_INCL_VAT_LA_AND_LAP,
            'ONGOING_PLANNER_FEE_INCL_VAT_UT':ONGOING_PLANNER_FEE_INCL_VAT_UT,
            'ONGOING_PLANNER_FEE_INCL_VAT_LA_AND_LAP':ONGOING_PLANNER_FEE_INCL_VAT_LA_AND_LAP,
            'SPOUSE_GENDER':SPOUSE_GENDER,
            'SPOUSE_RETIREMENT_AGE':SPOUSE_RETIREMENT_AGE,
            'SPOUSE_DATE_OF_BIRTH':SPOUSE_DATE_OF_BIRTH,
            'PERCENTAGE_SUCCESS':PERCENTAGE_SUCCESS,
            'SA_EQUITY_UNIT_TRUST':SA_EQUITY_UNIT_TRUST,
            'SA_BOND_UNIT_TRUST':SA_BOND_UNIT_TRUST,
            'SA_CASH_UNIT_TRUST':SA_CASH_UNIT_TRUST,
            'INTERNATIONAL_EQUITY_UNIT_TRUST':INTERNATIONAL_EQUITY_UNIT_TRUST,
            'INTERNATIONAL_BOND_UNIT_TRUST':INTERNATIONAL_BOND_UNIT_TRUST,
            'INTERNATIONAL_CASH_UNIT_TRUST':INTERNATIONAL_CASH_UNIT_TRUST,
            'SA_EQUITY_LAP':SA_EQUITY_LAP,
            'SA_BOND_LAP':SA_BOND_LAP,
            'SA_CASH_LAP':SA_CASH_LAP,
            'INTERNATIONAL_EQUITY_LAP':INTERNATIONAL_EQUITY_LAP,
            'INTERNATIONAL_BOND_LAP':INTERNATIONAL_BOND_LAP,
            'INTERNATIONAL_CASH_LAP':INTERNATIONAL_CASH_LAP,
            'LAP_EAC_PA_INCL_VAT':LAP_EAC_PA_INCL_VAT,
            'LA_EAC_PA_INCL_VAT':LA_EAC_PA_INCL_VAT,
            'UNIT_TRUST_EAC_PA_INCL_VAT':UNIT_TRUST_EAC_PA_INCL_VAT
   }
        
        
        info_data = pd.DataFrame(user_info_data, index=[0])
        return info_data
        
    individual_data = user_info()





    income = CatBoost.predict(individual_data)
    st.header('TARGET MONTHLY INCOME')
    st.write(
        """
        This is the estimated amount someone must earn 
        to reach their desired Retirement Fund Value.
        """)
    st.subheader('R' + str(np.round(income[0])))
    
    st.write("##")
    st.write("[View Project Source Code >](https://github.com/daniel-datasci/Retirement-Income-Predictor)")

    

#---------------ABOUT US---------------------
if selected == "About Us":
    with st.container():
        st.header("About Us")
        st.write("""
                 ExploreAI builds AI-driven software and digital twins for global companies. 
                 We are proud of domain expertise in the utilities, insurance, banking, and telecommunications industries.
                 We are able to help you accelerate your digital teams: train your workforce, hire talent, or sponsor students through a data science programme. 
                 These offerings are powered by the ExploreAI Academy: a learning institution teaching data and AI skills for the next generation.
                 We have offices in London, Cape Town, Johannesburg, Durban, and Mauritius. 
                 We consult to clients in the UK, the US, the Nordics, and South Africa.
                 """)
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("##")
            st.write("##")
            st.write("##")
            
            st.subheader(
                """
                Providing AI Solutions On A large Scale:
                - Are You Lokking For A Way To Transform Your Business Throught AI Powered Solutions? 
                - Are You Looking To Experience Cutting Edge Business Technology?
                - Are You Looking To Give Your Employees Top Notch Training On Technology Application?
                """) 
                 
        with right_column:
            st_lottie(lottie_coding, height=450, key="coding")
    st.write("##")
    st.write("[View Project Source Code >](https://github.com/daniel-datasci/Retirement-Income-Predictor)")



#---------------CONTACT US---------------------
if selected == "Contact Us":
    with st.container():
        st.header("Get In Touch With Us!") 
        st.write("##")
        
        contact_form = """
        <form action="https://formsubmit.co/danifedibah@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value"false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message Here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        
        left_column, right_column = st.columns(2)
        with left_column:
            selected1 = option_menu(
                menu_title = None, #-----requred
                options = ["", "", "", "", ""], #-----required
                icons = ["envelope", "telephone", "linkedin", "twitter", "instagram"],
                default_index = 0,
                orientation = "horizontal",
                styles={
                        "container": {"padding": "0!important", "background-color": "white"},
                        "icon": {"color": "black", "font-size": "30px"}, 
                        "nav-link": {
                            "font-size": "0px", 
                            "text-align": "left", 
                            "margin":"0px", 
                            "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "white"},
                    }
                )
            st.markdown(contact_form, unsafe_allow_html=True)
            
            
            
        with right_column:
            st.write("##")
            st_lottie(lottie_coding2, height=300)
            
    st.write("##")
    
    st.write("[View Project Source Code >](https://github.com/daniel-datasci/Retirement-Income-Predictor)")
   
