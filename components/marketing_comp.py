from datetime import datetime
from agents import Runner
import streamlit as st
from ai_agents.market_news import market_intelligence_agent
import os
import asyncio
async def run_marketing_agent():
    result = await Runner.run(market_intelligence_agent,"most recent news of tech,marketing,startup,AI and how can it help marketing")
    result.final_output.time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return result.final_output


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
        if "news" in st.session_state and st.session_state.news.time_stamp:
            st.write(f":material/notifications: {st.session_state.news.time_stamp}")
        else:
            st.write(":material/notifications: No Data")
            
        if st.button(":material/refresh: Refresh News"):
            with st.spinner("Fetching latest news..."):
                news = asyncio.run(run_marketing_agent())
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
                st.markdown(f"- [{info.title}]({info.url})")


    # Main Content Columns
    if "news" in st.session_state:
        news = st.session_state.news
        
        # Group stories by category
        categories = {}
        opportunities = []
        for story in news.analyzed_stories:
            cat = story.category
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(story)
            if story.agency_opportunity:
                opportunities.append((story.headline, story.agency_opportunity))
                
        cat_names = list(categories.keys())
        half = len(cat_names) // 2 + len(cat_names) % 2
        col1_cats = cat_names[:half]
        col2_cats = cat_names[half:]

        col1, col2 = st.columns(2)
        
        with col1:
            for cat in col1_cats:
                with st.container(border=True):
                    st.subheader(f":material/article: {cat} News")
                    for story in categories[cat]:
                        srcs = ", ".join(story.sources)
                        st.markdown(f"**[{story.headline}]({story.url})**")
                        st.caption(f"{story.summary} | {srcs})")
                        
            with st.container(border=True):
                st.subheader(":material/trending_up: Trends & Insights")
                st.markdown(news.trends_and_insights)

        with col2:
            for cat in col2_cats:
                with st.container(border=True):
                    st.subheader(f":material/article: {cat} News")
                    for story in categories[cat]:
                        srcs = ", ".join(story.sources)
                        st.markdown(f"**[{story.headline}]({story.url})**")
                        st.caption(f"{story.summary} | {srcs})")

            with st.container(border=True):
                st.subheader(":material/lightbulb: Opportunities for Agencies")
                
                # Show up to 4 opportunities
                for i in range(0, min(len(opportunities), 4), 2):
                    opp_cols = st.columns(2)
                    for j, opp_col in enumerate(opp_cols):
                        if i + j < len(opportunities):
                            headline, opp = opportunities[i + j]
                            with opp_col:
                                with st.container(border=True):
                                    st.markdown(f"**{headline}**")
                                    st.caption(opp)
                                    st.markdown("`High Opportunity`")
                                    
            with st.container(border=True):
                st.subheader(":material/strategy: Actionable Intelligence")
                st.markdown(news.actionable_intelligence)
                    
    else:
        st.info("No news data loaded. Click 'Refresh News' to fetch the latest market intelligence.")