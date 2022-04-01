import streamlit as st
import streamlit_authenticator as stauth
import json
import requests
base_route = "https://resq-api.azurewebsites.net/api"
TOKEN = None

def signup(volunteer):
    st.title("Sign Up as Volunteer")
    with st.form("Sign Up"):
        new_user = {
            'name':name,
            'email':email,
            'skills':username,
        }
        submitted = st.form_submit_button("Submit")
        if submitted:
            # send post request to the database
            url = base_route + '/auth/signup'
            response = requests.post(url, json = new_user)
            if response.status_code == 200:
                data = response.json()["token"]
                st.success("Signup successful!")


class Volunteer:
    @staticmethod
    def write():
        # sign up
        full_name = st.text_input("Your Full Name:")
        email = st.text_input("Your Email Address:")
        skill_list = requests.get(base_route+'/skill').json()
        skill_names = []
        for i in skill_list:
            skill_names.append(i['skill_name'])
        col1_1, col1_2 = st.columns((8,1))
        required_skills = []
        with col1_1:
            required_skills += st.multiselect("What are you skilled in?", skill_names) # assign skills
        with col1_2:
            add_skill = st.button("➕")

        col2_1, col2_2 = st.columns((8,1))
        with col2_1:
            if add_skill:
                with st.form("Add New Skill"):
                    skill_name = st.text_input("Add a new skill manually")
                    skill_description = st.text_area("Description")

                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        # auth = {
                        #     'Authorization': 'Bearer ' + st.session_state.token
                        # }
                        data = {
                            'skill_name':skill_name,
                            'skill_description':skill_description,
                            'priority':1
                        }
                        rec = requests.post(base_route+'/skill', json = data)
        skill_rating = st.text_input("Rate your skill:")