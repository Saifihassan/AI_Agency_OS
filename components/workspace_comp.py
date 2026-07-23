import streamlit as st 
from pages.dashboard import run_dashboard
from Database.db import add_to_workspace

def run_workspace():
    st.title("Create a new workspace")
    st.divider()

    name = st.text_input("Enter Clients Name")
    
    website= st.text_input("Enter clients website url")

    industry= st.text_input("specify the industry")
    
    create_workspace_btn = st.button("+ Create Workspace")

    dashboard_page = st.Page(run_dashboard, title="Dashboard", icon=":material/dashboard:")

    if create_workspace_btn:
        if name:
            workspace_id = add_to_workspace(name, website, industry)
            st.session_state.active_workspace_id = workspace_id
            st.switch_page(dashboard_page)
        else:
            st.error("Please enter a Client Name.")
        
