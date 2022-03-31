import streamlit as st
import streamlit_authenticator as stauth
import json
import requests
base_route = "https://resq-api.azurewebsites.net/api"

def signup():
    st.title("Sign Up")
    with st.form("Sign Up"):
        username = st.text_input("Username:")
        password = st.text_input("Password:")
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        new_user = {
            'name':name,
            'email':email,
            'username':username,
            'password':password
        }
        submitted = st.form_submit_button("Submit")
        if submitted:
            # send post request to the database
            url = base_route + '/auth/signup'
            response = requests.post(url, json = new_user)
            if response.status_code == 200:
                st.success("Signup successful!")

def login():
    st.session_state.logged_in = True

class User:
    @staticmethod
    def write():
        if "load_state" not in st.session_state:
            st.session_state.load_state = False

        # if signup button is clicked, signup
        if st.button('Sign Up') or st.session_state.load_state:
            st.session_state.load_state = True
            signup()
        
        # login
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        data ={
                'username':username,
                'password':password
            }

        if st.button("Login", on_click = login):
            url = base_route + '/auth/login'
            res = requests.post(url, json = data)
            if res.status_code == 200:
                st.success("Login successful!")
            else:
                st.error("Login failed!")
            st.write(res.json())
