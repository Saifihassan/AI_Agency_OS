import streamlit as st

def run_outreach():
    st.title("Outreach Generation")
    st.write("Personalized email outreach generation for service offerings.")
    st.write("")

    col_left, col_right = st.columns([1, 2.5], gap="small")

    with col_left:
        with st.container(border=True):
            st.subheader("Campaign Parameters")

            
            st.caption("COMPANY WEBSITE")
            st.text_input("Company Website", label_visibility="collapsed", placeholder="https://example.com")
            
            # st.write("")
            st.caption("SERVICE BEING OFFERED")
            st.text_area("Service Being Offered", label_visibility="collapsed", placeholder="e.g., SEO Optimization,\nCustom Web Development...", height=100)
            
            # st.write("")
            st.button(":material/auto_awesome: Generate Outreach", use_container_width=True)

        st.write("")
        with st.container(border=True):
            st.caption("AGENT STATUS")
            st.write(":material/check_circle: Ready to Analyze")

    with col_right:
        # Top row of right column
        top_col1, top_col2 = st.columns(2)
        
        with top_col1:
            with st.container(border=True):
                st.markdown("#### :material/business: Company Summary")
                st.write("Awaiting input... The AI agent will extract core business value propositions, target audience, and current market positioning based on the provided URL.")

        with top_col2:
            with st.container(border=True):
                st.markdown("#### :material/ads_click: Identified Pain Points")
                st.markdown("- Awaiting website analysis...")

        # Bottom area of right column
        with st.container(border=True):
            header_col1, header_col2 = st.columns([6, 2])
            with header_col1:
                st.markdown("#### :material/mail: Generated Sequence")
                st.divider()
            with header_col2:
                # st.write(":material/content_copy: :material/edit:") # Copy and edit icons
               with st.container(horizontal=True,horizontal_alignment="right"):
                    st.button(":material/content_copy:")    
                    st.button(":material/edit:")
            
            # Empty state area
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