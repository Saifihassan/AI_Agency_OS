from pydantic import BaseModel, Field
from typing import List, Optional

class Article(BaseModel):
    headline: str

    article_url: str

    source: str

    published_date: str

    summary: str
class NewsSearcherOutput(BaseModel):
    articles: List[Article] = Field(description="List of raw articles found")



class AnalyzedStory(BaseModel):
    headline: str = Field(description="Headline of the story")
    url: str = Field(description="URL of the story")
    category: str = Field(description="Category of the story (e.g., AI, Marketing, SEO)")
    summary: str = Field(description="A concise summary in 2-3 sentences")
    why_it_matters: str = Field(description="Why this news matters for digital marketers or agencies")
    agency_opportunity: str = Field(description="One practical opportunity an agency can offer clients based on this news")
    sources: List[str] = Field(description="List of sources used")

class NewsAnalystOutput(BaseModel):
    analyzed_stories: List[AnalyzedStory] = Field(description="List of stories with detailed actionable intelligence")

class Headline(BaseModel):
    title: str = Field(description="The one-liner headline text")
    url: str = Field(description="The URL of the corresponding article")

class MarketIntelligenceReport(BaseModel):
    report_title: str = Field(description="Title of the final intelligence report")
    trends_and_insights: str = Field(description="High-level overview of the major trends found")
    analyzed_stories: List[AnalyzedStory] = Field(description="The final list of analyzed stories")
    actionable_intelligence: str = Field(description="Concluding thoughts on how to act on this intelligence")
    time_stamp: str = Field(description="Timestamp of when the report was generated")
    one_liner_headlines: List[Headline] = Field(description="List of one-liner headlines with URLs for the news searched, suitable for a quick market brief")


