import streamlit as st
import streamlit_authenticator as stauth
import json
import pandas as pd
import random
import requests
base_route = "https://resq-api.azurewebsites.net/api"
TOKEN = None

def signup(volunteer):
    url = base_route + '/vol'
    response = requests.post(url, json = volunteer)
    if response.status_code == 200:
        st.success("Signup successful!")
    else:
        st.write(response.text)
        st.error("There was an error in connection.")


class Volunteer:
    @staticmethod
    def write():
        # sign up
        full_name = st.text_input("Your Full Name:")
        email = st.text_input("Your Email Address:")
        skill_list = requests.get(base_route+'/skill').json()
        skill_names = []
        if 'message' not in skill_list:
            for i in skill_list:
                skill_names.append(i['skill_name'])
        col1_1, col1_2 = st.columns((8,1))
        selected_skills = []
        with col1_1:
            selected_skills += st.multiselect("What are you skilled in?", skill_names) # assign skills
        with col1_2:
            st.text('') # vertically align
            st.text('')
            add_skill = st.button("➕")

        col2_1, col2_2 = st.columns((8,1))
        with col2_1:
            if add_skill:
                with st.form("Add New Skill"):
                    skill_name = st.text_input("Add a new skill manually")
                    skill_description = st.text_area("Description")
                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        data = {
                            'skill_name':skill_name,
                            'skill_description':skill_description
                        }
                        rec = requests.post(base_route+'/skill', json = data)
                        selected_skills.append(skill_name)
        skill_rating = {} # assign skill rating
        for skill in selected_skills:
            col3_1, col3_2 = st.columns((1,1))
            with col3_1:
                for i in range(3):
                    st.write("\n")
                st.write(skill)
            with col3_2:
                skill_rating[skill] = st.number_input("Rate your skill (1-10):", min_value=0, max_value=5, step=1, key=skill)
        volunteer = {"name": full_name, "email": email, "skills": skill_rating, "username": full_name+str(random.randint(0,10))}
        for i in range(4):
            st.text("\n")

        st.button("Sign Up as a Volunteer", on_click=signup, args=(volunteer, ))