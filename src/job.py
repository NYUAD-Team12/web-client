import streamlit as st
import pandas as pd
import requests
from src.user import TOKEN
import plotly.express as px
base_route = "https://resq-api.azurewebsites.net/api"


def optimize():
    st.write("Optimized.")
    return None
    # volunteer_allocation = requests.get(base_route + 'quantom/sim')
    # return volunteer_allocation
    
def display_jobs(volunteer_allocation = None):
    data = {
        'username':'admin',
    }
    job_list = requests.get(base_route+'/user/project', json = data).json()
    if 'message' in job_list:
        st.header("No Current Tasks")
        st.write("Click add task to create a new task.")
    else:
        # if volunteer_allocation != None:
        #     optimized = True
        #  if optimized:
            # st.subheader("Volunteers Distribution")
            # df = pd.DataFrame({
            #     'Locations':job['project_name'],
            #     'Num. of Volunteers Allocated':volunteer_allocation[job['project_name']]
            # })
            # fig = px.line(df, x = "Skills Needed", y = "Avg. of User Skills")
            # st.plotly_chart(fig)

        for job in job_list:
            st.header(job['project_name'])
            st.write(job['project_description'])
            # display skill table
            df = pd.DataFrame({
                'Required Skills': job['skills'],
                'Skill Prioritiy': job['priority']
            })
            st.write(df)

            # display volunteer allocation
            # if optimized:
            #     st.write("Num. of Volunteers Allocated: " + len(job['project_name']))

def add_job():
    job_name = st.text_input("Location:")
    job_description = st.text_area("Task Description:")
    skill_list = requests.get(base_route+'/skill').json()
    skill_names = []
    if 'message' not in skill_list:
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
            st.success("Task added successfully!")
        else:
            st.error("Task failed to add!")

class Job:
    @staticmethod
    def write():
        if "button" not in st.session_state:
            st.session_state.button = None

        st.title("Dashboard")
        col1, col2 = st.columns((1, 1))
        with col1:
            if st.button("+ Add Task"):
                st.session_state.button = 0
        with col2:
            if st.button("Optimize"):
                st.session_state.button = 2
        
        if st.session_state.button == 2:
            volunteer_allocation = optimize()
        if st.session_state.button == 0:
            add_job()
        display_jobs()