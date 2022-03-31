import streamlit as st
import pandas as pd
import requests
base_route = "https://resq-api.azurewebsites.net/api"

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
    job_title = st.text_input("Job Title:")
    job_description = st.text_area("Description:")
    skill_list = requests.get(base_route+'/skill') # get skill list
    col1_1, col1_2 = st.columns((8,1))
    required_skills = []
    with col1_1:
        required_skills += st.multiselect("Skills", skill_list) # assign skills
    with col1_2:
        add_unique_skill = st.button("➕")

    if add_unique_skill:
        st.session_state.button = 1

    col2_1, col2_2 = st.columns((8,1))
    with col2_1:
        if st.session_state.button != None:
            with st.form("Add New Skill"):
                unique_skill = st.text_input("Add a new skill manually")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    required_skills.append(unique_skill)

    skill_priorities = [] # assign skill priorities
    for skill in required_skills:
        col3_1, col3_2 = st.columns((1,1))
        with col3_1:
            st.write(skill)
        with col3_2:
            skill_priorities.append(st.number_input("Skill Priority", min_value=0, max_value=10, step=1, key=skill))
    

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