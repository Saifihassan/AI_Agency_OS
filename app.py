import streamlit as st
from pages.dashboard import show_dashboard  
from pages.content_studio import show_content_studio
from pages.research import show_research
from pages.marketing_page import show_marketing
from pages.outreach import show_outreach
from pages.competitior import show_competitor
from pages.Create_workspace import show_create_workspace
from Database.db import fetch_from_workspaces

records = fetch_from_workspaces()
if len(records) == 0:
    st.set_page_config(layout="centered", initial_sidebar_state="collapsed")
else:
    st.set_page_config(layout="wide", initial_sidebar_state="expanded")
if 'recent_modules' not in st.session_state:
    st.session_state.recent_modules = []
if 'module_usage' not in st.session_state:
    st.session_state.module_usage = {
        "Marketing": 0,
        "Campaign Studio": 0,
        "Research": 0,
        "Outreach": 0,
        "Competitor Analysis": 0
    }
create_workspace_page = st.Page(show_create_workspace, title="Create Workspace", icon=":material/add:")

def render_main_app(records):
    st.sidebar.markdown("<h1 style='font-size:30px; '>AI Agency OS</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h1 style='font-size:15px; '>Workspaces</h1>", unsafe_allow_html=True)
    st.sidebar.selectbox("Active Workspace", records, format_func=lambda record: record[1], key="active_workspace")    
    workspace_button = st.sidebar.button("+ Create a new Workspace")
    st.sidebar.divider()
    
    dashboard_page = st.Page(show_dashboard, title="Dashboard", icon=":material/dashboard:")
    content_studio_page = st.Page(show_content_studio, title="Content Studio", icon=":material/palette:")
    research_page = st.Page(show_research, title="Research", icon=":material/search:")
    marketing_page = st.Page(show_marketing, title="Marketing", icon=":material/campaign:")
    outreach_page = st.Page(show_outreach, title="Outreach", icon=":material/send:")
    competitor_page = st.Page(show_competitor, title="Competitor", icon=":material/query_stats:")
    
    pages = [dashboard_page, content_studio_page, research_page, marketing_page, outreach_page, competitor_page]
    all_pages = pages + [create_workspace_page]

    st.session_state.dashboard_page = dashboard_page
    st.session_state.content_studio_page = content_studio_page
    st.session_state.research_page = research_page
    st.session_state.marketing_page = marketing_page
    st.session_state.outreach_page = outreach_page
    st.session_state.competitor_page = competitor_page
    
    pg = st.navigation(all_pages, position="hidden")

    with st.sidebar:
        st.markdown("""
            <style>
            [data-testid="stPageLink"] a p {
                font-size: 20px !important;
            }
            [data-testid="stPageLink"] a {
                padding: 10px 15px !important;
            }
            </style>
        """, unsafe_allow_html=True)
        if workspace_button:
            st.switch_page(create_workspace_page)
        for p in pages:
            st.page_link(p, label=p.title, icon=p.icon)

    pg.run()

if len(records) == 0:
    all_pages = [create_workspace_page]
    pg = st.navigation(all_pages, position="hidden")
    pg.run()
else:
    render_main_app(records)