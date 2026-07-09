import streamlit as st


def run_marketing():
    # Header
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.header("Market Intelligence")
        st.caption("Stay ahead with the latest AI, marketing, SEO and social media updates.")
    with header_col2:
        st.write(":material/notifications: June 8, 2025")
        st.button(":material/refresh: Refresh News")

    # Today's Market Brief
    with st.container(border=True):
        st.subheader(":material/content_paste: Today's Market Brief")
        st.markdown("- :material/local_fire_department: OpenAI launches GPT-5 Enterprise with improved reasoning and context handling. **2h ago**")
        st.markdown("- :material/trending_up: LinkedIn engagement rates are up 12% across all industries. **4h ago**")
        st.markdown("- :material/campaign: Google Ads introduces AI Max for Search Campaigns. **6h ago**")
        st.markdown("- :material/photo_camera: Instagram expands Reels to 3 minutes for all users globally. **8h ago**")
        st.markdown("- :material/smart_toy: Runway releases new Gen-3 video model with major realism upgrade. **10h ago**")
        st.markdown("[View Full Summary ->](#)")

    # Main Content Columns
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            # with st.container(horizontal=True,gap="large"):

            title_col, link_col = st.columns([3, 1])
            with title_col:
                st.subheader(":material/smart_toy: AI News")
            with link_col:
                st.markdown("<div style='margin-top:10px;'><a href='#' >View All-></a></div>", unsafe_allow_html=True)
            st.markdown("OpenAI launches GPT-5 Enterprise **2h ago**")
            st.markdown("Anthropic introduces Claude 4 **5h ago**")
            st.markdown("Google Gemini 2.5 Pro updated **7h ago**")
            
        with st.container(border=True):
            title_col, link_col = st.columns([3, 1])
            with title_col:
                st.subheader(":material/search: SEO Updates")
            with link_col:
                st.markdown("<div style='margin-top:10px;'><a href='#' >View All-></a></div>", unsafe_allow_html=True)

            st.markdown("Google June 2025 Core Update rolling out **2h ago**")
            st.markdown("AI Overviews appear in more search queries **5h ago**")
            st.markdown("New ranking factors observed in SERPs **8h ago**")
            
        with st.container(border=True):
            st.subheader(":material/trending_up: Trending Topics")
            st.markdown("`AI Agents` `B2B SaaS` `UGC` `Short-form Video` `Cold Outreach` `Automation` `Local SEO`")

    with col2:
        with st.container(border=True):
            title_col, link_col = st.columns([3, 1])
            with title_col:
                st.subheader(":material/rocket_launch: Marketing News")
            with link_col:
                st.markdown("<div style='margin-top:10px;'><a href='#' >View All-></a></div>", unsafe_allow_html=True)

            st.markdown("Meta adds new AI tools for advertisers **3h ago**")
            st.markdown("TikTok launches new ad placement options **6h ago**")
            st.markdown("Email open rates are rising again in 2025 **9h ago**")
            
        with st.container(border=True):
            title_col, link_col = st.columns([3, 1])
            with title_col:
                st.subheader(":material/link: Social Media Updates")
            with link_col:
                st.markdown("<div style='margin-top:10px;'><a href='#' >View All-></a></div>", unsafe_allow_html=True)

            st.markdown("Instagram tests new carousel format **3h ago**")
            st.markdown("LinkedIn introduces AI content suggestions **6h ago**")
            st.markdown("YouTube expands partnerships program **10h ago**")
            
        with st.container(border=True):
            title_col, link_col = st.columns([4, 1])
            with title_col:
                st.subheader(":material/lightbulb: Opportunities for Agencies")
            with link_col:
                st.markdown("<div style='margin-top:10px;'><a href='#' >View All-></a></div>", unsafe_allow_html=True)
            
            opp1, opp2 = st.columns(2)
            with opp1:
                with st.container(border=True):
                    st.markdown("**Short-form video content is trending**")
                    st.caption("Engagement is up across LinkedIn, TikTok and Instagram. Suggest to clients.")
                    st.markdown("`High Opportunity`")
            with opp2:
                with st.container(border=True):
                    st.markdown("**Google AI Overviews are expanding**")
                    st.caption("More visibility shifts are happening. Offer SEO audits to clients.")
                    st.markdown("`High Opportunity`")