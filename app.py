from git import Tree
import streamlit as st
from pages.dashboard import show_dashboard  
from pages.content_studio import show_content_studio
from pages.research import show_research
from pages.marketing_page import show_marketing
from pages.outreach import show_outreach
from pages.competitior import show_competitor
st.set_page_config(
    layout="wide"
)

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
st.sidebar.markdown("<h1 style='font-size:25px; '>AI Agency OS</h1>", unsafe_allow_html=True)

dashboard_page = st.Page(show_dashboard, title="Dashboard", icon=":material/dashboard:")
content_studio_page = st.Page(show_content_studio, title="Content Studio", icon=":material/palette:")
research_page = st.Page(show_research, title="Research", icon=":material/search:")
marketing_page = st.Page(show_marketing, title="Marketing", icon=":material/campaign:")
outreach_page = st.Page(show_outreach, title="Outreach", icon=":material/send:")
competitor_page = st.Page(show_competitor, title="Competitor", icon=":material/query_stats:")
pages = [dashboard_page, content_studio_page, research_page, marketing_page, outreach_page, competitor_page]

st.session_state.dashboard_page = dashboard_page
st.session_state.content_studio_page = content_studio_page
st.session_state.research_page = research_page
st.session_state.marketing_page = marketing_page
st.session_state.outreach_page = outreach_page
st.session_state.competitor_page = competitor_page
pg = st.navigation(pages,position="hidden")


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
    for p in pages:
        # with st.container(height="stretch"):
            st.page_link(p, label=p.title, icon=p.icon)


pg.run()
# st.button("Red Button")
# st.progress(50)
# st.slider("Test", 0, 100)