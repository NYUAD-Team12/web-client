import streamlit as st
import pandas as pd

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
    title = st.text_input("Job Title:")
    description = st.text_area("Description:")
    skill_list = ["Architecture Design", "Moving Resources", "CAD"] # get skill list
    required_skills = st.multiselect("Skills", skill_list)
    st.write(required_skills) # test
    
class Job:
    @staticmethod
    def write():
        if "load_state" not in st.session_state:
            st.session_state.load_state = False

        st.title("Dashboard")
        if st.button("+ Add Job") or st.session_state.load_state:
            st.session_state.load_state = True
            add_job()
        display_jobs()
        
        df = get_table()
        st.write(df) # will display the dataframe