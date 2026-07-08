from streamlit.proto import ButtonGroup_pb2
import streamlit as st

def run_campaign():
    campaignheading,buttons=st.columns([6,3])
    with campaignheading:                       # heading with button to save or export the campaign 
        st.header("Campaign Studio")
        st.caption("Create a complete marketing campaign in minutes with AI")
    with buttons:                            # Save Campaign and Export all buttons
        with st.container(horizontal=True):
            st.button("New Campaign",use_container_width=True)
            st.button("Export all",use_container_width=True)
    st.markdown("<br>",unsafe_allow_html=True)
    with st.container():                    # container with url, goal, audience, platforms and generate button
        url,goal,audience,platforms,generate_button=st.columns(5)

        with url:                               # text input for website URL
            st.text_input("Website URL",placeholder="https://www.example.com")
        
        with goal:
            st.text_input("Campaign Goal",placeholder="e.g. Increase sales by 20%")
        
        with audience:
            st.text_input("Target Audience",placeholder="e.g. Small business owners in Pakistan")
        
        with platforms:
            st.text_input("Platforms",placeholder="e.g. Facebook, Instagram, LinkedIn")
        
        with generate_button:
            st.button("Generate Campaign",use_container_width=True)

    st.markdown("<br>",unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown('''
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <div style="width: 40px; height: 40px; border-radius: 50%; background-color: rgba(139, 92, 246, 0.15); display: flex; align-items: center; justify-content: center; margin-right: 15px;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8B5CF6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/>
                        <path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/>
                        <path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/>
                        <path d="M10 6h4"/>
                        <path d="M10 10h4"/>
                        <path d="M10 14h4"/>
                        <path d="M10 18h4"/>
                    </svg>
                </div>
                <h3 style="margin: 0; padding: 0; font-size: 16px; font-weight: 600; color: #F5F3FF; margin-right: 15px;">Brand Summary</h3>
                <span style="background-color: rgba(16, 185, 129, 0.15); color: #10B981; padding: 2px 10px; border-radius: 12px; font-size: 12px; font-weight: 500;">Researched</span>
            </div>
        ''', unsafe_allow_html=True)

        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.caption("Business")
            st.write("AI Marketing Platform")
            
        with col2:
            st.caption("Industry")
            st.write("SaaS / Marketing")
            
        with col3:
            st.caption("USP")
            st.write("AI-powered marketing automation for agencies")
            
        with col4:
            st.caption("Tone of Voice")
            st.write("Professional, Innovative, Helpful")
            
        with col5:
            st.caption("Target Audience")
            st.write("Marketing managers, Agencies, SMBs")


    tab1,tab2,tab3,tab4 =st.tabs(["Campaign Strategy","Social Media Posts","Email Campaign","Ads"])
    
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            with st.container(border=True):
                st.markdown("#### 🎯 Campaign Strategy")
                st.markdown("**✔️ Objective**")
                st.caption("Generate qualified leads")
                st.markdown("**✔️ Messaging**")
                st.caption("AI simplifies marketing and drives real results")
                st.markdown("**✔️ Offer**")
                st.caption("Book a demo and get started")
                st.markdown("**✔️ Timeline**")
                st.caption("2 Weeks Campaign")
                st.button("View Full Strategy", use_container_width=True)
        with c2:
            with st.container(border=True):
                cols = st.columns([3, 1])
                cols[0].markdown("#### 📄 Landing Page Outline")
                cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>View All</a>", unsafe_allow_html=True)
                
                cc1, cc2 = st.columns([2, 3])
                cc1.markdown("**Hero Section**")
                cc2.caption("Attention + Value Proposition")
                cc1.markdown("**Features**")
                cc2.caption("Key features and capabilities")
                cc1.markdown("**Benefits**")
                cc2.caption("How it solves customer problems")
                cc1.markdown("**Testimonials**")
                cc2.caption("Client reviews and case studies")
                cc1.markdown("**CTA Section**")
                cc2.caption("Clear call to action")

    with tab2:
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.container(border=True):
                cols = st.columns([3, 1])
                cols[0].markdown("#### 🔗 Social Media Posts")
                cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>View All</a>", unsafe_allow_html=True)
                
                with st.container(border=True):
                    sc1, sc2 = st.columns([3, 2])
                    sc1.markdown("🟦 LinkedIn Post")
                    sc2.button("Copy", key="copy_li")
                with st.container(border=True):
                    sc1, sc2 = st.columns([3, 2])
                    sc1.markdown("🟧 Instagram Post")
                    sc2.button("Copy", key="copy_ig")
                with st.container(border=True):
                    sc1, sc2 = st.columns([3, 2])
                    sc1.markdown("⬛ X (Twitter) Post")
                    sc2.button("Copy", key="copy_x")
                with st.container(border=True):
                    sc1, sc2 = st.columns([3, 2])
                    sc1.markdown("🟦 Facebook Post")
                    sc2.button("Copy", key="copy_fb")
        with c2:
            with st.container(border=True):
                cols = st.columns([3, 1])
                cols[0].markdown("#### #️⃣ Hashtags")
                cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>Copy All</a>", unsafe_allow_html=True)
                
                st.markdown("`#AIMarketing` `#MarketingAutomation`")
                st.markdown("`#LeadGeneration` `#DigitalMarketing`")
                st.markdown("`#MarketingTips` `#AIForBusiness`")
                st.markdown("`#GrowthHacking` `#SaaS` `#BusinessGrowth`")
        with c3:
            with st.container(border=True):
                cols = st.columns([3, 1])
                cols[0].markdown("#### 📅 Content Calendar")
                cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>View Calendar</a>", unsafe_allow_html=True)
                
                cal1, cal2, cal3, cal4, cal5 = st.columns(5)
                with cal1:
                    st.caption("Mon  \nJun 9")
                    st.markdown("🟦")
                    st.caption("Post")
                with cal2:
                    st.caption("Tue  \nJun 10")
                    st.markdown("🟧")
                    st.caption("Post")
                with cal3:
                    st.caption("Wed  \nJun 11")
                    st.markdown("✉️")
                    st.caption("Email")
                with cal4:
                    st.caption("Thu  \nJun 12")
                    st.markdown("🇬")
                    st.caption("Ad")
                with cal5:
                    st.caption("Fri  \nJun 13")
                    st.markdown("🟦")
                    st.caption("Post")

    with tab3:
        c1, c2 = st.columns(2)
        with c1:
            with st.container(border=True):
                cols = st.columns([3, 1])
                cols[0].markdown("#### ✉️ Email Campaign")
                cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>View All</a>", unsafe_allow_html=True)
                st.markdown("**Subject Line**")
                st.caption("Boost Your Leads with AI-Powered Marketing")
                st.markdown("**Preview**")
                st.caption("Hi {first_name}, Marketing is evolving fast, and AI is leading...")
                st.markdown("**CTA Button**")
                st.button("Book a Free Demo", key="email_cta")
                
                ec1, ec2 = st.columns(2)
                ec1.button("📑 Copy All", use_container_width=True)
                ec2.button("🔄 Regenerate", use_container_width=True)
        with c2:
            with st.container(border=True):
                cols = st.columns([3, 1])
                cols[0].markdown("#### ⚡ CTA Suggestions")
                cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>Copy All</a>", unsafe_allow_html=True)
                
                st.markdown("**Book a Free Demo >**")
                st.markdown("**Get Your Custom Proposal >**")
                st.markdown("**Start Your Free Trial >**")
                st.markdown("**Talk to an AI Expert >**")

    with tab4:
        with st.container(border=True):
            cols = st.columns([3, 1])
            cols[0].markdown("#### 🇬 Google Ads")
            cols[1].markdown("<a href='#' style='display: block; text-align: right; color: #8B5CF6; font-size: 14px; margin-top: 10px; text-decoration: none;'>View All</a>", unsafe_allow_html=True)
            
            st.markdown("**Headlines (3)**")
            gc1, gc2 = st.columns([3, 2])
            with gc1:
                st.caption("AI Marketing That Drives Results  \nAutomate. Optimize. Grow.  \nMore Leads. Less Effort.")
            gc2.button("Copy", key="copy_headlines")
            
            st.markdown("**Descriptions (2)**")
            gc1, gc2 = st.columns([3, 2])
            with gc1:
                st.caption("AI-powered marketing for agencies and SMBs.  \nGet more leads and grow your business.")
            gc2.button("Copy", key="copy_desc")
            
            st.markdown("**Keywords**")
            st.caption("ai marketing, lead generation, marketing automation, digital marketing, ai for agencies, +2 more")
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([4, 2, 2, 2])
        
        with col1:
            st.markdown("#### ✨ Your campaign is ready!")
            st.caption("We've generated a complete marketing campaign with 14+ assets.")
            
        with col2:
            st.markdown("#### 👥 14+")
            st.caption("Assets Generated")
            
        with col3:
            st.markdown("#### 🎯 6")
            st.caption("Channels Covered")
            
        with col4:
            st.markdown("#### 📅 2 Weeks")
            st.caption("Campaign Plan")
