import streamlit as st
from utils.pdf_gen import generate_pdf
from utils.text_gen import generate_report_text

@st.dialog("Copy Report Text", width="large")
def copy_text_dialog(text):
    st.code(text, language="markdown")

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
                        print(st.session_state.research_report)
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
        if "research_report" in st.session_state and st.session_state.research_report:
            report_data = st.session_state.research_report
            
            if not isinstance(report_data, dict):
                # Handle old session state data gracefully
                # st.warning("The report format has been updated to include more details. Please click 'Generate Research' again to view the new layout.")
                st.session_state.research_report = None
                st.rerun()
            
            research = report_data["research"]
            strategy = report_data["strategy"]
            
            # Report Container
            with st.container(border=True):
                # Top Bar
                top_col1, top_col2, top_col3 = st.columns([5, 2, 2])
                with top_col1:
                    st.caption(":material/circle: REPORT GENERATED ")
                with top_col2:
                    if st.button(":material/content_copy: Copy Text", use_container_width=True):
                        copy_text_dialog(generate_report_text(research, strategy))
                with top_col3:
                    pdf_bytes = generate_pdf(research, strategy)
                    st.download_button(
                        label=":material/download: Download PDF",
                        data=pdf_bytes,
                        file_name="research_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
                
                st.subheader(research.report_title)
                st.write("")
                
                # Create Tabs for better organization
                tab1, tab2, tab3 = st.tabs(["Overview", "Findings", "Recommendations"])
                
                with tab1:
                    # Executive Summary
                    with st.container(border=True):
                        st.markdown("#### :material/description: Executive Summary")
                        st.write(research.executive_summary)

                    # Strategic Overview
                    with st.container(border=True):
                        st.markdown("#### :material/explore: Strategic Overview")
                        st.write(strategy.strategic_overview)
                        
                    # Conclusion
                    with st.container(border=True):
                        st.markdown("#### :material/flag: Conclusion")
                        st.write(strategy.conclusion)
                        
                    # Sources
                    st.write("")
                    st.caption("DATA SOURCES PROCESSED")
                    all_sources = []
                    for finding in research.findings:
                        if hasattr(finding, 'sources') and finding.sources:
                            all_sources.extend(finding.sources)
                    
                    unique_sources = {source.url: source for source in all_sources}.values()
                    
                    if unique_sources:
                        pills_html = '''
                        <style>
                        .source-pill {
                            display: inline-block;
                            padding: 4px 12px;
                            margin: 4px 4px 4px 0;
                            border-radius: 16px;
                            background-color: rgba(128, 128, 128, 0.1);
                            border: 1px solid rgba(128, 128, 128, 0.2);
                            text-decoration: none !important;
                            font-size: 13px;
                            color: inherit !important;
                            transition: all 0.2s;
                        }
                        .source-pill:hover {
                            background-color: rgba(128, 128, 128, 0.2);
                            border-color: rgba(128, 128, 128, 0.4);
                        }
                        </style>
                        <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-top: 8px;">
                        '''
                        
                        for source in unique_sources:
                            # Using publisher as the pill text, but if it's too long or empty, fallback to title
                            display_text = source.publisher if source.publisher else source.title
                            # Truncate if too long
                            if len(display_text) > 30:
                                display_text = display_text[:27] + "..."
                            
                            pills_html += f'<a href="{source.url}" target="_blank" class="source-pill" title="{source.title}">{display_text}</a>'
                            
                        pills_html += '</div>'
                        st.markdown(pills_html, unsafe_allow_html=True)

                with tab2:
                    # Key Findings
                    if research.findings:
                        st.markdown("#### :material/search: Key Findings")
                        for finding in research.findings:
                            with st.container(border=True):
                                st.markdown(f"**{finding.title}**")
                                st.write(finding.explanation)
                                st.caption(f"**Why it matters:** {finding.why_it_matters}")

                with tab3:
                    # Recommendations
                    if strategy.prioritized_recommendations:
                        st.markdown("#### :material/check_circle: Recommendations")
                        for rec in strategy.prioritized_recommendations:
                            with st.container(border=True):
                                st.markdown(f"**{rec.title}**")
                                st.write(rec.description)
                                st.caption(f"**Business Impact:** {rec.business_impact}")

                    # Quick Wins & Long-term Opportunities
                    qw_col, lto_col = st.columns(2)
                    with qw_col:
                        if strategy.quick_wins:
                            with st.container(border=True):
                                st.markdown("#### :material/flash_on: Quick Wins")
                                for qw in strategy.quick_wins:
                                    st.markdown(f"**{qw.title}**")
                                    for step in qw.action_steps:
                                        st.markdown(f"- {step}")
                    with lto_col:
                        if strategy.long_term_opportunities:
                            with st.container(border=True):
                                st.markdown("#### :material/trending_up: Long Term Opportunities")
                                for lto in strategy.long_term_opportunities:
                                    st.markdown(f"**{lto.title}**")
                                    st.write(lto.description)
        else:
            # Placeholder State before report is generated
            with st.container(border=True):
                # Top Bar
                top_col1, top_col2, top_col3 = st.columns([5, 2 ,2])
                with top_col1:
                    st.caption(":material/circle: REPORT STATUS")
                with top_col2:
                    st.button(":material/content_copy: Copy Text", use_container_width=True, disabled=True)
                with top_col3:
                    st.button(":material/download: Download PDF", use_container_width=True, disabled=True)
                
                st.info("Fill out the form on the left and click 'Generate Research' to view the AI-powered research report here.")