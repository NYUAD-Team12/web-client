import streamlit as st
from streamlit import config
from src.home import Home as home
from src.user import User as user
from src.job import Job as job
from src.volunteer import Volunteer as volunteer

def write_page(page):
    #    return page.dash_write(name='MSFT', start='2019-06-03', stop='2021-06-03')
    return page.write()

def logout():
    st.session_state.logged_in = False

def main():
    PAGES = {}
    st.session_state.token = None
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        PAGES = { 
        'Home':home,
        'User':user,
        'Volunteer Signup': volunteer,
        }
    if not st.session_state["logged_in"]:
        PAGES = { 
        'Home':home,
        'User':user,
        'Volunteer Signup': volunteer,
        }
    if st.session_state["logged_in"]:
        PAGES = {'Home':home, 'Dashboard':job,}
        st.sidebar.button('Log Out', on_click = logout)

    choice=st.sidebar.radio("Click on the pages to explore",tuple(PAGES.keys()))


    if choice == None:
        write_page(home)
    else:
        page=PAGES[choice]
        write_page(page)


if __name__ == "__main__":
    st.set_page_config(page_title="NYUAD",layout="wide",page_icon="")
    main()
