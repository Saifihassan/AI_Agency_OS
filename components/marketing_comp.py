from datetime import datetime
import streamlit as st
from ai_agents.market_news import run_marketing_news_agent
import os
import asyncio

def run_marketing():
    from Database.db import insert_market_news, fetch_market_news
    
    workspace = st.session_state.get("active_workspace")
    workspace_id = workspace[0] if workspace else None

    news = None
    if workspace_id:
        report_data = fetch_market_news(workspace_id)
        if report_data:
            from ai_agents.schemas.schemas import MarketIntelligenceReport
            try:
                news = MarketIntelligenceReport.model_validate_json(report_data)
            except Exception:
                pass

    # Header
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.header("Market Intelligence")
        st.caption("Stay ahead with the latest AI, marketing, SEO and social media updates.")
    with header_col2:
        if news and hasattr(news, 'generated_at') and news.generated_at:
            st.write(f":material/notifications: {news.generated_at}")
        else:
            st.write(":material/notifications: No Data")
            
        if st.button(":material/refresh: Refresh News"):
            st.session_state.recent_modules.insert(0, "Marketing")
            st.session_state.module_usage["Marketing"] += 1
            with st.spinner("fetching latest news it may take a while..."):
                workspace = st.session_state.get("active_workspace")
                workspace_name = workspace[1] if workspace else "General"
                industry = workspace[3] if workspace and len(workspace) > 3 else "technology"
                fetched_news = asyncio.run(run_marketing_news_agent(workspace_name, industry))
                # Save to database
                if workspace_id:
                    insert_market_news(workspace_id, fetched_news.model_dump_json())
            st.rerun()    


    # Today's Market Brief
    with st.container(border=True):
        st.subheader(":material/content_paste: Today's Market Brief")
        if news:
            import re
            def get_best_url(headline, news):
                best_url = "#"
                max_score = 0
                headline_words = set(re.findall(r'\w+', headline.lower()))
                for cat in news.categorized_news:
                    for article in cat.articles:
                        text_words = set(re.findall(r'\w+', (article.title + " " + article.summary).lower()))
                        score = len(headline_words.intersection(text_words))
                        if score > max_score and score > 2:
                            max_score = score
                            best_url = article.url
                return best_url

            for info in news.one_liner_headlines:      
                url = get_best_url(info, news)
                st.markdown(f"- <a href='{url}' style='color: white;'>{info}</a>", unsafe_allow_html=True)


    # Main Content Columns
    if news:
        col1, col2 = st.columns(2)
        
        with col1:
            for cat_news in news.categorized_news:
                with st.container(border=True):
                    st.subheader(f":material/article: {cat_news.category}")
                    for article in cat_news.articles:
                        st.markdown(f"<a href='{article.url}' style='color: white; font-weight: bold; text-decoration: none;' target='_blank'>{article.title}</a>", unsafe_allow_html=True)
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