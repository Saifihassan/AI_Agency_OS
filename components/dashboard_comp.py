import streamlit as st

def run_dashboard():
    # Top Header section
    st.markdown("<h2>Good Morning, Hassan! 👋</h2>", unsafe_allow_html=True)
    st.caption("Here's what's happening in your marketing world today.")
    st.markdown("<br>", unsafe_allow_html=True)

    # Main Layout
    left_col, right_col = st.columns([1.3, 1], gap="medium")

    with left_col:
        with st.container(border=True):
            st.markdown("<h4>📈 Today's Market Brief</h4>", unsafe_allow_html=True)
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

            market_item("🤖", "OpenAI announced new pricing for GPT-4o", "2h ago")
            market_item("🟡", "Google rolls out AI Overviews globally", "4h ago")
            market_item("🚀", "Instagram tests new Reels length up to 3 minutes", "6h ago")
            market_item("🎯", "TikTok engagement rate is up 18% this week", "8h ago")
            
            st.write("")
            st.markdown("View full market intelligence →")

    with right_col:
        with st.container(border=True):
            st.markdown("<h4>⚡ Quick Actions</h4>", unsafe_allow_html=True)
            st.write("")
            
            bc1, bc2 = st.columns(2)
            with bc1:
                st.button("🌐 Market Intelligence", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button("🚀 Campaign Studio", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button("🎯 Competitor Analysis", use_container_width=True)
            
            with bc2:
                st.button("🔍 New Research", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button("✉️ Outreach", use_container_width=True)
                st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                st.button("📊 View Reports", use_container_width=True)
    
    RecentActivity,AIActivity=st.columns([2,2],border=True)
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
        recent_activity_item("🤖", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item("🤖", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item("🤖", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item("🤖", "OpenAI announced new pricing for GPT-4o", "2h ago")
        recent_activity_item("🤖", "OpenAI announced new pricing for GPT-4o", "2h ago")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: left;'>View all market news</div>", unsafe_allow_html=True)


    with AIActivity:
        st.markdown("### AI Usage")
        def ai_acitivity_item(icon,text,number):
            col1,col2,col3=st.columns([1,10,3])
            with col1:
                st.write(icon)
            with col2:
                st.write(text)
            with col3:
                st.write(number)
        ai_acitivity_item("🧠","Models", 3250)
        