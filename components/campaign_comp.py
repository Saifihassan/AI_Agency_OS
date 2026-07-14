import streamlit as st
import asyncio
from ai_agents.campaign import run_campaign_agent

@st.dialog("Copy Content", width="large")
def copy_text_dialog(text):
    st.code(text, language="markdown")

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
            
            st.write("**Website URL or Business Description**")
            website = st.text_area("Website URL", label_visibility="collapsed", placeholder="https://example.com")
            
            st.write("**Campaign Goal**")
            campaign_goal = st.text_input("Campaign Goal",label_visibility="collapsed")
            
            st.write("**Target Platform**")
            target_platforms = st.multiselect(
                "Target Platform", 
                ["Google Ads", "Email", "Instagram", "X", "LinkedIn", "Facebook"], 
                default=["Google Ads", "Email", "LinkedIn"], 
                label_visibility="collapsed"
            )

            st.write("")
            if st.button(":material/auto_awesome: Generate Campaign", use_container_width=True):
                if not website and not campaign_goal:
                    st.warning("Please provide a website or business description, and a campaign goal.")
                elif not target_platforms:
                    st.warning("Please select at least one target platform.")
                else:
                    with st.spinner("Generating Campaign Assets..."):
                        try:
                            assets = asyncio.run(run_campaign_agent(website, campaign_goal, target_platforms))
                            st.session_state.campaign_assets = assets
                            st.success("Campaign generated successfully!")
                            print(assets)
                        except Exception as e:
                            st.error(f"Error generating campaign: {e}")

    with col_right:
        assets = st.session_state.get("campaign_assets")

        # Top strategy card
        with st.container(border=True):
            strat_col1, strat_col2 = st.columns([5, 1])
            with strat_col1:
                st.markdown("#### :material/ads_click: Campaign Strategy")
            with strat_col2:
                st.caption("DRAFT")
            
            strategy_text = assets.campaign_strategy if assets and assets.campaign_strategy else "Run the campaign generator to populate your strategy."
            st.write(strategy_text)

        # Create Tabs for better organization
        tab1, tab2, tab3 = st.tabs(["Copywriting", "Social Media", "CTAs & Assets"])
        
        with tab1:
            with st.container(border=True):
                st.markdown("#### :material/description: Marketing Copy")
                with st.container(border=True):
                    marketing_text = assets.marketing_copy if assets and assets.marketing_copy else "*No marketing copy generated yet.*"
                    st.write(marketing_text)
                    st.write("")
                    st.write("")
                if st.button("Copy to clipboard", key="copy_marketing"):
                    copy_text_dialog(marketing_text)

            with st.container(border=True):
                st.markdown("#### :material/mail: Email Copy")
                with st.container(border=True):
                    email_text = assets.email_copy if assets and assets.email_copy else "*No email copy generated yet.*"
                    st.write(email_text)
                if st.button("Copy to clipboard", key="copy_email"):
                    copy_text_dialog(email_text)

        with tab2:
            if assets and assets.social_posts:
                for i, post in enumerate(assets.social_posts):
                    with st.container(border=True):
                        st.markdown(f"#### :material/chat: Post {i+1}")
                        with st.container(border=True):
                            st.write(post)
                        if st.button("Copy to clipboard", key=f"copy_social_{i}"):
                            copy_text_dialog(post)
            else:
                st.info("No social posts generated yet.")
                
            if assets and assets.hashtags:
                with st.container(border=True):
                    st.markdown("#### :material/tag: Hashtags")
                    st.markdown("**" + " ".join(assets.hashtags) + "**")

        with tab3:
            with st.container(border=True):
                st.markdown("#### :material/ads_click: CTA Suggestions")
                if assets and assets.cta_suggestions:
                    for cta in assets.cta_suggestions:
                        st.write(cta)
                        st.divider()
                else:
                    st.info("No CTA suggestions generated yet.")

