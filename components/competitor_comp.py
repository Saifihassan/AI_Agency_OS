import streamlit as st
import asyncio
from ai_agents.competitor import run_competitor_agent

def run_competitor():
    st.title("Competitor Analysis")
    st.write("Deep dive into competitor strengths, weaknesses, and market opportunities using advanced OS intelligence.")
    st.write("")

    # Top Box
    with st.container(border=True):
        st.caption("TARGET COMPANY WEBSITE")
        col1, col2 = st.columns([4, 1], gap="medium")
        with col1:
            website = st.text_input("Target Company Website", placeholder="https://competitor.com", label_visibility="collapsed")
        with col2:
            analyze_clicked = st.button(":material/search: Analyze Competitors", use_container_width=True)

    if analyze_clicked:
        st.session_state.recent_modules.insert(0, "Competitor Analysis")
        st.session_state.module_usage["Competitor Analysis"] += 1
        with st.spinner("Analyzing Competitor..."):
            res = asyncio.run(run_competitor_agent(website))
            st.session_state.competitor_result = res
            
    result = st.session_state.get("competitor_result")

    st.write("")

    # Middle Section
    mid_col1, mid_col2 = st.columns([2, 1], gap="small")

    with mid_col1:
        with st.container(border=True):
            header1, header2 = st.columns([4, 1])
            with header1:
                st.markdown("#### :material/business: COMPANY SNAPSHOT")
            with header2:
                st.caption("Live Data" if result else "Waiting...")
            
            st.write("")
            if result:
                snap = result.company_snapshot
                
                r1, r2 = st.columns([1.2, 2])
                r1.markdown("**Company:**")
                r2.markdown(snap.company_name)
                
                r1, r2 = st.columns([1.2, 2])
                r1.markdown("**Category:**")
                r2.markdown(snap.industry)
                
                r1, r2 = st.columns([1.2, 2])
                r1.markdown("**Primary Audience:**")
                r2.markdown(snap.target_audience)
                
                r1, r2 = st.columns([1.2, 2])
                r1.markdown("**Market Position:**")
                r2.markdown(f"<span style='background-color: #e8f5e9; color: #2e7d32; padding: 2px 6px; border-radius: 4px; font-size: 12px; font-weight: bold;'>{snap.market_position}</span>", unsafe_allow_html=True)
                
                r1, r2 = st.columns([1.2, 2])
                r1.markdown("**Core Differentiator:**")
                r2.markdown(snap.core_differentiator)
                
                st.write("")
                st.markdown("**Overview:**")
                st.write(snap.company_overview)
            else:
                st.write("Awaiting input... The AI agent will extract a comprehensive company snapshot based on the provided URL.")
                st.write("")

    with mid_col2:
        with st.container(border=True):
            st.markdown("#### :material/trending_up: STRENGTHS")
            st.divider()
            if result:
                for strength in result.strengths:
                    st.markdown(f":material/check: {strength}")
                    st.write("")
            else:
                st.write("Awaiting input...")

    st.write("")

    # Bottom Section
    with st.container(border=True):
        tab1, tab2, tab3 = st.tabs([":material/trending_down: Weaknesses", ":material/lightbulb: Opportunities", ":material/bolt: Recommended Strategy"])

        with tab1:
            if result:
                for weakness in result.weaknesses:
                    st.markdown(f":material/warning: {weakness}")
                    st.write("")
            else:
                st.write("Awaiting input...")

        with tab2:
            if result:
                for opp in result.opportunities:
                    with st.container(border=True):
                        st.write(f"**{opp.title}**")
                        st.caption(opp.description)
            else:
                st.write("Awaiting input...")

        with tab3:
            st.markdown("**What should I do to compete against this company?**")
            if result:
                st.write(result.recommended_strategy)
            else:
                st.write("Awaiting input...")
            st.write("")
            st.button("Draft Campaign", use_container_width=True)
