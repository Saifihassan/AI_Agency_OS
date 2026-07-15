import streamlit as st
import os

st.set_page_config(
    layout="wide",
    
)
def run_dashboard():
    # Load news from cache if not in session state
    if "news" not in st.session_state:
        if os.path.exists("market_news_cache.json") and os.path.getsize("market_news_cache.json") > 0:
            from ai_agents.schemas.schemas import MarketIntelligenceReport
            with open("market_news_cache.json", "r", encoding="utf-8") as f:
                try:
                    st.session_state.news = MarketIntelligenceReport.model_validate_json(f.read())
                except Exception:
                    pass
    # Top Header section
    st.header("Good Morning, Hassan! :material/waving_hand:")
    st.caption("Here's what's happening in your marketing world today.")
    st.markdown("<br>", unsafe_allow_html=True)

    # Main Layout
    left_col, right_col = st.columns([5, 3], gap="medium")

    with left_col:
        with st.container(border=True):
            st.subheader(":material/trending_up: Today's Market Brief")
            st.write("")
            
            # Helper for Market Brief items
            def market_item(icon, text, time):
                c1, c2, c3 = st.columns([1, 15, 3])
                with c1:
                    st.write(icon)
                with c2:
                    st.markdown(text, unsafe_allow_html=True)
                with c3:
                    st.caption(f"<div style='text-align: right;'>{time}</div>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 0.2em 0; border: 0.5px solid #444;'>", unsafe_allow_html=True)

            if "news" in st.session_state and st.session_state.news:
                icons = [":material/smart_toy:", ":material/new_releases:", ":material/rocket_launch:", ":material/ads_click:", ":material/article:"]
                # Get up to 4 headlines
                headlines = st.session_state.news.one_liner_headlines[:4]
                for idx, item in enumerate(headlines):
                    icon = icons[idx % len(icons)]
                    linked_title = f"<span style='color:inherit; text-decoration:none;'>{item}</span>"
                    market_item(icon, linked_title, "Recent")
            else:
                st.write("No market news loaded yet.")
                st.caption("Go to the Marketing page and refresh to load the latest news.")
            
            # st.write("")
            if "marketing_page" in st.session_state:
                st.page_link(st.session_state.marketing_page, label="View full market intelligence →")

    with right_col:
        with st.container(border=True):
            st.subheader(":material/bolt: Quick Actions")
            st.write("")
            
            bc1, bc2 = st.columns(2)
            with bc1:
                if st.button(":material/language: Market Intelligence", use_container_width=True):
                    st.switch_page(st.session_state.marketing_page)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                if st.button(":material/rocket_launch: Campaign Studio", use_container_width=True):
                    st.switch_page(st.session_state.content_studio_page)
            
            with bc2:
                if st.button(":material/search: New Research", use_container_width=True):
                    st.switch_page(st.session_state.research_page)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                if st.button(":material/mail: Outreach", use_container_width=True):
                    st.switch_page(st.session_state.outreach_page)
            
            st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
            if st.button(":material/ads_click: Competitor Analysis", use_container_width=True):
                st.switch_page(st.session_state.competitor_page)
    
    RecentActivity,AIActivity=st.columns([4,2],border=True)
    with RecentActivity:
        st.markdown("#### Recent Activity")
        def recent_activity_item(icon, text, time):
            with st.container(border=True,gap="medium"):
                c1,c2,c3=st.columns([1,15,3])
                with c1:
                    st.write(icon)
                with c2:
                    st.write(text)
                with c3:
                    st.caption(f"<div style='text-align: right;'>{time}</div>", unsafe_allow_html=True)
            # st.markdown("<hr style='margin: 0.2em 0; border: 0.5px solid #444;'>", unsafe_allow_html=True)
        recent_activity_item(":material/smart_toy:", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item(":material/smart_toy:", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item(":material/smart_toy:", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item(":material/smart_toy:", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item(":material/smart_toy:", "OpenAI announced new pricing for GPT-4o", "2h ago")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: left; margin-bottom:30px'>View all market news</div>", unsafe_allow_html=True)


    with AIActivity:
        st.markdown("### AI Usage")
        def ai_activity_item(icon_name,text,number):
            with st.container(border=True):
                col1,col2,col3=st.columns([1,5,3], vertical_alignment="center")
                with col1:
                    st.markdown(f"<div style='text-align:center;margin-bottom:10px'><span style='font-family: \"Material Symbols Rounded\"; font-size: 1.25rem;'>{icon_name}</span></div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div style='text-align:center;margin-bottom:10px'>{text}</div>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<div style='text-align:center;margin-bottom:10px font-size:15px;'>{number}</div>", unsafe_allow_html=True)
        ai_activity_item("psychology","Generated reports",38)
        ai_activity_item("psychology","Generated reports",38)
        ai_activity_item("psychology","Generated reports",38)
        ai_activity_item("psychology","Generated reports",38)
        ai_activity_item("psychology","Generated reports",38)

        