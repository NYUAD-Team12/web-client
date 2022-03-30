import streamlit as st
from streamlit import config
from src.home import Home as home
from src.about import About as about


def write_page(page):  # pylint: disable=redefined-outer-name
    #if page == dash:
    #    return page.dash_write(name='MSFT', start='2019-06-03', stop='2021-06-03')
    return page.write()
PAGES={ 
    'Home':home,
    'About':about

    }
    # , 'CryptoCurrency':crypto}

def main():
    choice=st.sidebar.radio("Click on the pages to explore",tuple(PAGES.keys()))


    if choice ==None:
        write_page(home) 
    else:
        page=PAGES[choice]
        write_page(page)


if __name__ == "__main__":
    st.set_page_config(page_title="NYUAD",layout="wide",page_icon="")
    main()
