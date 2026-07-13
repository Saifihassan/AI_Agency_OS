import streamlit as st

def run_research():
    st.title("Research Reports")
    st.write("Generate and view detailed AI-powered industry and topic research.")
    st.write("")

    col_left, col_right = st.columns([1, 2.5], gap="small")

    with col_left:
        # New Research Query Box
        with st.container(border=True):
            # st.caption("NEW RESEARCH QUERY")
            
            st.write("**Research Topic**")
            research_topic = st.text_area("Research Topic", label_visibility="collapsed", placeholder="e.g., Impact of Generative AI on B2B SaaS marketing strategies in 2024...", height=100)
            
            st.write("**Website URL**")
            website_url = st.text_input("Website URL", label_visibility="collapsed", placeholder="https://example.com")
            
            st.write("**Research Depth**")
            st.selectbox("Research Depth", ["Standard Analysis", "Deep Dive", "Quick Summary"], label_visibility="collapsed")
            
            if st.button(":material/auto_awesome: Generate Research", use_container_width=True):
                with st.spinner("Generating Research..."):
                    import asyncio
                    from ai_agents.research import run_flow
                    try:
                        report = asyncio.run(run_flow(research_topic, website_url))
                        st.session_state.research_report = report
                        st.success("Research generated successfully!")
                    except Exception as e:
                        st.error(f"Error generating research: {e}")


        st.write("")

        # Recent Reports
        with st.container(border=True):
            st.caption("RECENT REPORTS")
            st.write("")
            st.markdown("[Competitor Analysis: Acme C... →](#)")
            st.write("")
            st.markdown("[Q3 E-commerce Trends →](#)")
            
    with col_right:
        # Report Container
        with st.container(border=True):
            # Top Bar
            top_col1, top_col2, top_col3 = st.columns([5, 2 ,2])
            with top_col1:
                st.caption(":material/circle: REPORT GENERATED ")
            with top_col2:
                st.button(":material/content_copy: Copy Text", use_container_width=True)
            with top_col3:
                st.button(":material/download: Download PDF", use_container_width=True)
            
            st.subheader("Generative AI in B2B SaaS Marketing (2024 Outlook)")
            st.write("")
            
            # Executive Summary
            with st.container(border=True):
                st.markdown("#### :material/description: Executive Summary")
                st.write("The integration of Generative AI into B2B SaaS marketing workflows is accelerating, shifting from experimental pilot programs to core operational necessities. Early adopters are reporting significant decreases in content production costs while simultaneously seeing a marginal increase in MQL quality due to enhanced personalization capabilities at scale. The primary challenge identified is maintaining brand voice consistency across high-volume AI-generated outputs.")

            # Key Insights
            ki_col1, ki_col2 = st.columns(2)
            with ki_col1:
                with st.container(border=True):
                    st.markdown("#### :material/lightbulb: Key Insight 1")
                    st.write("Hyper-personalization engines are outperforming generic automated outbound sequences by 3.4x in response rates.")
            with ki_col2:
                with st.container(border=True):
                    st.markdown("#### :material/trending_up: Key Insight 2")
                    st.write("SEO strategies are pivoting from pure keyword density to topical authority mapping, as LLM-based search behaviors emerge.")

            # Recommendations
            with st.container(border=True):
                st.markdown("#### :material/check_circle: Recommendations")
                st.markdown("- Develop a proprietary, fine-tuned model trained specifically on historical high-performing marketing collateral to ensure brand consistency.")
                st.markdown("- Reallocate budget from low-tier freelance content production towards technical AI workflow specialists and prompt engineers.")

            st.write("")
            st.caption("DATA SOURCES PROCESSED")
            ds_col1, ds_col2, ds_col3 = st.columns([1, 1, 1])
            with ds_col1:
                with st.container(border=True):
                    st.write("Gartner Reports (2023-...)")
            with ds_col2:
                with st.container(border=True):
                    st.write("Forrester B2B...")
            with ds_col3:
                st.write("") # empty space for the remaining width