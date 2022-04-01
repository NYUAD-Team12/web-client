import streamlit as st
import pandas as pd
import plotly.express as px

# st.subheader("Skill Distribution")
# df = pd.DataFrame({
#     'Skills Needed': ["vehicle operation", "nursing", "repairing", "cleaning"],
#     'Avg. of User Skill Level':[1, 8, 5, 7]
# })
# fig = px.line(df, x = "Skills Needed", y = "Avg. of User Skills")
# st.plotly_chart(fig)

volunteer_allocation = {
    "Yemen":{
        0:"Maria8"
    },
    "Lebanon":{
        0:"Bob3"
    },
    "Ukraine":{
        0:"Anna1",
        1:"Ahmed0"
    }
}
if volunteer_allocation != None:
    optimized = True
if optimized:
    df = pd.DataFrame(volunteer_allocation)
    st.write(df)
    # st.subheader("Volunteers Distribution")
    # df = pd.DataFrame({
    #     'Locations':volunteer_allocation.keys(),
    #     'Num. of Volunteers Allocated':len(volunteer_allocation.values())
    # })
    # fig = px.line(df, x = "Locations", y = "Num. of Volunteers Allocated")
    # st.plotly_chart(fig)