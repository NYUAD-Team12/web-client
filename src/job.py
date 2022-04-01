import streamlit as st
import pandas as pd
import requests
base_route = "https://resq-api.azurewebsites.net/api"

def get_table():
    url = base_route + '/projects'

    df = pd.DataFrame({
        'Job Title': ['Reconstruction of the building'],
        'Number of People Needed': [150],
        'Required Skills': [['Architectural Planning', 'Moving Resources']],
        'Skill Level': [10]
    })
    return df

def display_jobs():
    col1, col2 = st.columns((2, 3))
    with col1:
        st.header("#1 Building Reconstruction")
    with col2:
        st.write(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur elementum nulla ornare nisi elementum, at sodales arcu fringilla. Maecenas sed efficitur risus. Vestibulum imperdiet orci vestibulum nisl dictum, sit amet mattis odio sodales. Fusce ipsum lacus, consequat at gravida at, maximus elementum tellus. Quisque cursus mauris sed lectus volutpat fringilla. Nulla feugiat tristique neque et pharetra. Proin in odio vel elit sodales venenatis. Ut dignissim tellus eu varius tempus."
        )

def add_job():
    # with st.form("Add New Job"):
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
                        'skill_description':skill_description,
                        'priority':1
                    }
                    rec = requests.post(base_route+'/skill', json = data)

    # skill_priorities = [] # assign skill priorities
    # for skill in required_skills:
    #     col3_1, col3_2 = st.columns((1,1))
    #     with col3_1:
    #         st.write(skill)
    #     with col3_2:
    #         skill_priorities.append(st.number_input("Skill Priority", min_value=0, max_value=10, step=1, key=skill))
    
    if st.button("Submit"):
    auth = {
        'Bearer Token:'
    }
    data = {
        'project_name':job_name,
        'project_description':job_description,
        'project_reward':1,
        'skills':skill_names
    }
    rec = requests.post(base_route+'/project', json = data)

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
        
        df = get_table()
        st.write(df) # will display the dataframe