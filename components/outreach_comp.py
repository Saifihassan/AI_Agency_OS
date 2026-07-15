import streamlit as st
import asyncio
from ai_agents.outreach_agent import run_outreach_agent

@st.dialog("Copy Outreach Sequence")
def show_copy_dialog(full_text):
    st.write("Click the copy icon in the top right of the box below to copy your sequence.")
    st.code(full_text, language="markdown")

def run_outreach():
    st.title("Outreach Generation")
    st.write("Personalized email outreach generation for service offerings.")
    st.write("")

    col_left, col_right = st.columns([1, 2.5], gap="small")

    with col_left:
        with st.container(border=True):
            st.subheader("Campaign Parameters")
            
            st.caption("COMPANY WEBSITE")
            website = st.text_input("Company Website", label_visibility="collapsed", placeholder="https://example.com")
            
            st.caption("SERVICE BEING OFFERED")
            service = st.text_area("Service Being Offered", label_visibility="collapsed", placeholder="e.g., SEO Optimization,\nCustom Web Development...", height=100)
            
            st.caption("OUTREACH TONE")
            outreachtone = st.selectbox("Outreach Tone", ["Friendly", "Professional", "Consultative", "Direct", "Founder-to-Founder"], label_visibility="collapsed")
            
            generate_clicked = st.button(":material/auto_awesome: Generate Outreach", use_container_width=True)

        st.write("")
        with st.container(border=True):
            st.caption("AGENT STATUS")
            if generate_clicked:
                st.write(":material/sync: Analyzing and Generating...")
            elif st.session_state.get("outreach_result"):
                st.write(":material/check_circle: Generation Complete")
            else:
                st.write(":material/check_circle: Ready to Analyze")

    if generate_clicked:
        with st.spinner("Running Agents..."):
            res = asyncio.run(run_outreach_agent(website, service, outreachtone))
            st.session_state.outreach_result = res
            
    result = st.session_state.get("outreach_result")

    with col_right:
        tab1, tab2, tab3 = st.tabs(["Company Summary", "Pain Points", "Outreach Sequence"])
        
        with tab1:
            with st.container(border=True):
                st.markdown("#### :material/business: Company Summary")
                if result:
                    st.write(result["prospect_analysis"].company_summary)
                    st.markdown("**Target Audience:**")
                    st.write(result["prospect_analysis"].target_audience)
                else:
                    st.write("Awaiting input... The AI agent will extract core business value propositions, target audience, and current market positioning based on the provided URL.")

        with tab2:
            with st.container(border=True):
                st.markdown("#### :material/ads_click: Identified Pain Points")
                if result:
                    for pain_point in result["prospect_analysis"].identified_pain_points:
                        st.markdown(f"- {pain_point}")
                else:
                    st.markdown("- Awaiting website analysis...")

        with tab3:
            with st.container(border=True):
                header_col1, header_col2 = st.columns([6, 2])
                with header_col1:
                    st.markdown("#### :material/mail: Generated Sequence")
                    st.divider()
                with header_col2:
                    copy_all = st.button(":material/content_copy: Copy All", use_container_width=True)
                
                if result:
                    seq = result["outreach_sequence"]
                    
                    if copy_all:
                        full_text = "Subject Lines:\n" + "\n".join([f"- {s}" for s in seq.subject_lines]) + f"\n\nCold Email:\n{seq.cold_email}\n\nFollow-up 1:\n{seq.follow_up_email_1}\n\nFollow-up 2:\n{seq.follow_up_email_2}\n\nCTA:\n{seq.call_to_action}"
                        show_copy_dialog(full_text)
                    
                    st.markdown("##### Subject Lines")
                    for subject in seq.subject_lines:
                        st.markdown(f"- {subject}")
                    st.write("")
                    
                    st.markdown("##### Cold Email")
                    st.write(seq.cold_email)
                    st.write("")
                    
                    st.markdown("##### Follow-up 1")
                    st.write(seq.follow_up_email_1)
                    st.write("")
                    
                    st.markdown("##### Follow-up 2")
                    st.write(seq.follow_up_email_2)
                    st.write("")
                    
                    st.markdown("##### CTA")
                    st.write(seq.call_to_action)

                else:
                    with st.container(border=True):
                        st.write("")
                        st.write("")
                        st.write("")
                        cols = st.columns([1, 2, 1])
                        with cols[1]:
                            st.markdown("<div style='text-align: center; color: gray; margin-bottom: 0px; font-size: 50px;'><span style='font-family: \"Material Symbols Rounded\"; font-size: 50px;'>description</span></div>", unsafe_allow_html=True)  
                            st.markdown("<p style='text-align: center; color: gray;'>Fill out the parameters and generate outreach to see the personalized email body, subject line variations, and follow-up sequence here.</p>", unsafe_allow_html=True)
                        st.write("")
                        st.write("")
                        st.write("")
                
                st.caption(":material/info: Follow-up suggestions will appear alongside the main email body.")