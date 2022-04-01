import streamlit as st
import pandas as pd
import requests
from src.user import TOKEN
base_route = "https://resq-api.azurewebsites.net/api"

def display_jobs():
    data = {
        'username':'admin',
    }
    job_list = requests.get(base_route+'/user/project', json = data).json()

    for job in job_list:
        st.header(job['project_name'])
        st.write(job['project_description'])
        # display skill table
        df = pd.DataFrame({
            'Required Skills': job['skills'],
            'Skill prioritiy': job['priority']
        })
        st.write(df)

def add_job():
    job_name = st.text_input("Job Title:")
    job_description = st.text_area("Description:")
    skill_list = requests.get(base_route+'/skill').json()
    skill_names = []
    for i in skill_list:
        skill_names.append(i['skill_name'])
    col1_1, col1_2 = st.columns((8,1))
    required_skills = []
    with col1_1:
        required_skills += st.multiselect("Skills", skill_names) # assign skills
    with col1_2:
        st.text('') # vertically align
        st.text('')
        add_skill = st.button("➕")

    col2_1, col2_2 = st.columns((8,1))
    with col2_1:
        if add_skill:
            st.session_state.button = 1
        if st.session_state.button == 1:
            with st.form("Add New Skill"):
                skill_name = st.text_input("Add a new skill manually")
                skill_description = st.text_area("Description")
                data = {
                    'skill_name':skill_name,
                    'skill_description':skill_description
                }
                submitted = st.form_submit_button("Submit")
                if submitted:  
                    rec = requests.post(base_route+'/skill', json = data)
                    st.session_state.button = 0
                    if rec.status_code == 200:
                        st.success("Skill added successfully!")
                    else:
                        st.error("Skill failed to add!")

    skill_priorities = [] # assign skill priorities
    for skill in required_skills:
        col3_1, col3_2 = st.columns((1,1))
        with col3_1:
            st.write(skill)
        with col3_2:
            skill_priorities.append(st.number_input("Skill Priority", min_value=0, max_value=10, step=1, key=skill))
    
    if st.button("Submit"):
        st.write(st.session_state.token)
        data = {
            'username' : "admin",
            'project_name':job_name,
            'project_description':job_description,
            'skills':required_skills,
            'priority':skill_priorities
        }
        rec = requests.post(base_route+'/project', json = data)
        if rec.status_code == 200:
            st.success("Job added successfully!")
        else:
            st.error("Job failed to add!")

class Job:
    @staticmethod
    def write():
        if "button" not in st.session_state:
            st.session_state.button = None

        st.title("Dashboard")
        if st.button("+ Add Job"):
            st.session_state.button = 0
        if st.session_state.button != None:
            add_job()

        display_jobs()