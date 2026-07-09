import streamlit as st

def run_competitor():
    st.title("Competitor Analysis")
    st.write("Deep dive into competitor strengths, weaknesses, and market opportunities using advanced OS intelligence.")
    st.write("")

    # Top Box
    with st.container(border=True):
        st.caption("TARGET COMPANY WEBSITE")
        col1, col2 = st.columns([4, 1], gap="medium")
        with col1:
            st.text_input("Target Company Website", label_visibility="collapsed", placeholder="https://competitor.com")
        with col2:
            st.button(":material/search: Analyze Competitors", use_container_width=True)

    st.write("")

    # Middle Section
    mid_col1, mid_col2 = st.columns([2, 1], gap="small")

    with mid_col1:
        with st.container(border=True):
            header1, header2 = st.columns([4, 1])
            with header1:
                st.markdown("#### :material/ads_click: MARKET POSITION")
            with header2:
                st.caption("Live Data")
            # Competitor 1
            c1, c2, c3 = st.columns([1, 6, 3], vertical_alignment="center")
            with c1:
                st.markdown("<div style='text-align: center;'><h3>A</h3></div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div style='text-align: center;'><b>Acme Corp</b><br><small style='color: gray;'>Market Share: 34%</small></div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div style='text-align: center;'><span style='font-family: \"Material Symbols Rounded\"; vertical-align: middle; color: #ff4b4b;'>error</span> <span style='vertical-align: middle;'>High Threat</span></div>", unsafe_allow_html=True)
                
            st.write("")
            
            # Competitor 2
            c1, c2, c3 = st.columns([1, 6, 3], vertical_alignment="center")
            with c1:
                st.markdown("<div style='text-align: center;'><h3>B</h3></div>", unsafe_allow_html=True)
            with c2:
                st.markdown("<div style='text-align: center;'><b>Beta Industries</b><br><small style='color: gray;'>Market Share: 21%</small></div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div style='text-align: center;'><span style='font-family: \"Material Symbols Rounded\"; vertical-align: middle; color: #ffa421;'>warning</span> <span style='vertical-align: middle;'>Moderate</span></div>", unsafe_allow_html=True)

    with mid_col2:
        with st.container(border=True):
            st.markdown("#### :material/trending_up: STRENGTHS")
            st.divider()
            st.markdown(":material/check: Strong brand recognition in EU markets.")
            st.write("")
            st.markdown(":material/check: Highly optimized supply chain logistics.")
            st.write("")
            st.markdown(":material/check: Proprietary AI routing algorithms.")

    st.write("")

    # Bottom Section
    bot_col1, bot_col2, bot_col3 = st.columns(3, gap="small")

    with bot_col1:
        with st.container(border=True):
            st.markdown("#### :material/trending_down: WEAKNESSES")
            st.divider()
            st.markdown(":material/warning: High customer churn rate in Q3.")
            st.write("")
            st.markdown(":material/warning: Outdated mobile application UI.")
            st.write("")
            st.markdown(":material/warning: Slow response times in customer support.")

    with bot_col2:
        with st.container(border=True):
            st.markdown("#### :material/lightbulb: OPPORTUNITIES")
            st.divider()
            with st.container(border=True):
                st.write("**Market Gap**")
                st.caption("Lack of mid-tier enterprise pricing models.")
            with st.container(border=True):
                st.write("**Feature Request**")
                st.caption("High demand for direct CRM integrations.")

    with bot_col3:
        with st.container(border=True):
            st.markdown("#### :material/bolt: STRATEGIC ACTION")
            st.divider()
            st.write("Launch targeted ad campaign highlighting our superior mobile experience and dedicated 24/7 support to capture dissatisfied Acme Corp users.")
            st.write("")
            st.write("")
            st.button("Draft Campaign", use_container_width=True)
