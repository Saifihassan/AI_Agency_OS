import streamlit as st

def run_campaign():
    # Title Section
    st.title("Campaign Studio")
    st.write("Design high-converting marketing campaigns driven by data.")
    st.write("")

    # Main layout columns
    col_left, col_right = st.columns([1, 3], gap="small")

    with col_left:
        with st.container(border=True):
            st.subheader("Campaign Parameters")
            st.write("")
            
            st.write("**Website URL**")
            st.text_input("Website URL", label_visibility="collapsed", placeholder="https://example.com")
            
            st.write("**Campaign Goal**")
            st.selectbox("Campaign Goal", ["Lead Generation", "Brand Awareness", "Sales"], label_visibility="collapsed")
            
            st.write("**Target Platform**")
            st.multiselect(
                "Target Platform", 
                ["Google Ads", "Meta", "LinkedIn", "Email", "Social Media"], 
                default=["Google Ads", "Meta", "LinkedIn", "Email", "Social Media"], 
                label_visibility="collapsed"
            )

            st.write("")
            st.button(":material/auto_awesome: Generate Campaign", use_container_width=True)

    with col_right:
        # Top strategy card
        with st.container(border=True):
            strat_col1, strat_col2 = st.columns([5, 1])
            with strat_col1:
                st.markdown("#### :material/ads_click: Campaign Strategy")
            with strat_col2:
                st.caption("DRAFT")
            
            st.write("Focus on high-intent search queries related to \"AI automation tools\". Utilize exact match keywords for core offerings while testing broad match modifier for discovery. Landing page should emphasize speed and ROI.")

        # Content columns
        content_col1, content_col2 = st.columns(2)
        
        with content_col1:
            with st.container(border=True):
                st.markdown("#### :material/description: Marketing Copy")
                with st.container(border=True):
                    st.write("*\"Stop wasting hours on manual tasks. Deploy our AI Agency OS today and scale your operations 10x faster. Start your free trial now.\"*")
                    # Adding empty space to match the height
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("")
                st.button("Copy to clipboard", key="copy_marketing")

            with st.container(border=True):
                st.markdown("#### :material/mail: Email Copy")
                with st.container(border=True):
                    st.write("*Subject: Scale your agency 10x with AI OS*")
                    st.write("")
                    st.write("*Hi there, are you still manually handling tasks? Our AI Agency OS is designed to automate your workflow...*")
                st.button("Copy to clipboard", key="copy_email")

        with content_col2:
            with st.container(border=True):
                st.markdown("#### :material/ads_click: CTA Suggestions")
                st.write("Start Scaling Today")
                st.divider()
                st.write("Deploy AI Now")
                st.divider()
                st.write("Get Your Demo")
            
            with st.container(border=True):
                st.markdown("#### :material/link: Social Media Posts")
                with st.container(border=True):
                    st.write("*:material/rocket_launch: Stop wasting time on manual tasks! Deploy AI Agency OS and watch your productivity soar. #AIAgency #Automation*")
                    st.write("")
                st.button("Copy to clipboard", key="copy_social")

            with st.container(border=True):
                st.markdown("#### :material/tag: Hashtags")
                st.markdown("**#AIAgency #Automation**")
                st.markdown("**#MarketingTech #Growth**")

