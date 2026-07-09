import streamlit as st


st.set_page_config(
    layout="wide",
    
)
def run_dashboard():
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
                    st.write(text)
                with c3:
                    st.caption(f"<div style='text-align: right;'>{time}</div>", unsafe_allow_html=True)
                st.markdown("<hr style='margin: 0.2em 0; border: 0.5px solid #444;'>", unsafe_allow_html=True)

            market_item(":material/smart_toy:", "OpenAI announced new pricing for GPT-4o", "2h ago")
            market_item(":material/new_releases:", "Google rolls out AI Overviews globally", "4h ago")
            market_item(":material/rocket_launch:", "Instagram tests new Reels length up to 3 minutes", "6h ago")
            market_item(":material/ads_click:", "TikTok engagement rate is up 18% this week", "8h ago")
            
            # st.write("")
            st.markdown("View full market intelligence →", unsafe_allow_html=True)

    with right_col:
        with st.container(border=True):
            st.subheader(":material/bolt: Quick Actions")
            st.write("")
            
            bc1, bc2 = st.columns(2)
            with bc1:
                st.button(":material/language: Market Intelligence", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button(":material/rocket_launch: Campaign Studio", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button(":material/ads_click: Competitor Analysis", use_container_width=True)
            
            with bc2:
                st.button(":material/search: New Research", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button(":material/mail: Outreach", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button(":material/bar_chart: View Reports", use_container_width=True)
    
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

        