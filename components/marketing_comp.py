from datetime import datetime
import streamlit as st
from ai_agents.market_news import run_marketing_news_agent
import os
import asyncio

def run_marketing():
    # Load from cache if not in session state
    if "news" not in st.session_state:
        if os.path.exists("market_news_cache.json") and os.path.getsize("market_news_cache.json") > 0:
            from ai_agents.schemas.schemas import MarketIntelligenceReport
            with open("market_news_cache.json", "r", encoding="utf-8") as f:
                try:
                    st.session_state.news = MarketIntelligenceReport.model_validate_json(f.read())
                except Exception:
                    pass  # Ignore invalid JSON so the app doesn't crash

    # Header
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.header("Market Intelligence")
        st.caption("Stay ahead with the latest AI, marketing, SEO and social media updates.")
    with header_col2:
        if "news" in st.session_state and hasattr(st.session_state.news, 'generated_at') and st.session_state.news.generated_at:
            st.write(f":material/notifications: {st.session_state.news.generated_at}")
        else:
            st.write(":material/notifications: No Data")
            
        if st.button(":material/refresh: Refresh News"):
            with st.spinner("fetching latest news it may take a while..."):
                news = asyncio.run(run_marketing_news_agent())
                st.session_state.news = news
                # Save to local file for persistence
                with open("market_news_cache.json", "w", encoding="utf-8") as f:
                    f.write(news.model_dump_json())
            st.rerun()    


    # Today's Market Brief
    with st.container(border=True):
        st.subheader(":material/content_paste: Today's Market Brief")
        if "news" in st.session_state:
            for info in st.session_state.news.one_liner_headlines:      
                st.markdown(f"- {info}")


    # Main Content Columns
    if "news" in st.session_state:
        news = st.session_state.news
        
        col1, col2 = st.columns(2)
        
        with col1:
            for cat_news in news.categorized_news:
                with st.container(border=True):
                    st.subheader(f":material/article: {cat_news.category}")
                    for article in cat_news.articles:
                        st.markdown(f"**[{article.title}]({article.url})**")
                        st.caption(f"{article.summary} | {article.source} | {article.published_date}")
                        st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.subheader(":material/trending_up: Market Trends")
                for trend in news.market_trends:
                    st.markdown(f"**{trend.title}**")
                    st.write(trend.description)
                    st.markdown("<hr style='margin: 0.5em 0; border: 0.5px solid #444;'>", unsafe_allow_html=True)

            with st.container(border=True):
                st.subheader(":material/lightbulb: Opportunities for Agencies")
                for opp in news.opportunities:
                    st.markdown(f"**{opp.title}**")
                    st.write(opp.description)
                    st.markdown("`High Opportunity`")
                    st.markdown("<hr style='margin: 0.5em 0; border: 0.5px solid #444;'>", unsafe_allow_html=True)
                    
    else:
        st.info("No news data loaded. Click 'Refresh News' to fetch the latest market intelligence.")