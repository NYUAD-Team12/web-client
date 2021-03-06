import streamlit as st
import streamlit_authenticator as stauth
import json
import requests
base_route = "https://resq-api.azurewebsites.net/api"
TOKEN = None
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

def login(data):
    url = base_route + '/auth/login'
    res = requests.post(url, json = data)
    if res.status_code == 200:
        st.session_state.logged_in = True
        st.success("Login successful!")
        if "token" not in st.session_state:
            st.session_state["token"] = res.json()["token"]
        else:
            st.session_state.token = res.json()["token"]
    else:
        st.error("Login failed!")

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
        data = {
            'username':username,
            'password':password
        }

        st.button("Login", on_click = login, args=(data, ))
