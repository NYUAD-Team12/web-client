import streamlit as st
import streamlit_authenticator as stauth
import json
import requests

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
            url = 'sample_url'
            response = requests.post(url, json = new_user)


class User:
    @staticmethod
    def write():
        if "load_state" not in st.session_state:
            st.session_state.load_state = False

        # load existing user data
        names = ['John Smith', 'Rebecca Briggs'] # temp data
        emails = ['jsmith@gmail.com', 'rbriggs@gmail.com']
        usernames = ['jsmith', 'rbriggs']
        passwords = ['123', '456']
        
        # if signup button is clicked, signup
        if st.button('Sign Up') or st.session_state.load_state:
            st.session_state.load_state = True
            signup()
        
        # login
        hashed_passwords = stauth.Hasher(passwords).generate() # generate hashed password
        authenticator = stauth.Authenticate(names, usernames, hashed_passwords, # create authenticator class using user credentials
                    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
        name, authentication_status, username = authenticator.login('Login', 'main')

        if st.session_state['authentication_status']: # if already logged in
            authenticator.logout('Logout', 'main') # logout
            st.write('Welcome *%s*' % (st.session_state['name']))
            st.title('Some content')
        elif st.session_state['authentication_status'] == False: # if wrong authentication entered
            st.error('Username/password is incorrect')
        elif st.session_state['authentication_status'] == None: # if not logged in
            st.warning('Please enter your username and password')
