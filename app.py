import streamlit as st
from pages.dashboard import show_dashboard  
from pages.content_studio import show_content_studio
from pages.research import show_research
from pages.marketing import show_marketing


st.sidebar.title("AI Agency OS")


dashboard_page = st.Page(show_dashboard, title="Dashboard", icon="📊")
content_studio_page = st.Page(show_content_studio, title="Content Studio", icon="🎨")
research_page = st.Page(show_research, title="Research", icon="🔍")
marketing_page = st.Page(show_marketing, title="Marketing", icon="📈")
pages = [dashboard_page, content_studio_page, research_page, marketing_page]


pg = st.navigation(pages,position="hidden")


with st.sidebar:
    for p in pages:
        
        st.page_link(p, label=p.title, icon=p.icon)


pg.run()
