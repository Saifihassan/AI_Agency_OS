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

class VerifiedStory(BaseModel):
    title: str = Field(description="Title of the verified story")
    url: str = Field(description="URL of the verified story")
    source: str = Field(description="Source of the verified story")
    published_date: str = Field(description="Date the story was published")
    short_description: str = Field(description="A short description of the story")
    confidence_score: str = Field(description="Confidence score: 'High Confidence' or 'Medium Confidence'")

class NewsVerifierOutput(BaseModel):
    verified_stories: List[VerifiedStory] = Field(description="List of verified stories, with duplicates and low confidence stories removed")

class AnalyzedStory(BaseModel):
    headline: str = Field(description="Headline of the story")
    category: str = Field(description="Category of the story (e.g., AI, Marketing, SEO)")
    summary: str = Field(description="A concise summary in 2-3 sentences")
    why_it_matters: str = Field(description="Why this news matters for digital marketers or agencies")
    agency_opportunity: str = Field(description="One practical opportunity an agency can offer clients based on this news")
    confidence: str = Field(description="Confidence score inherited from the verifier")
    sources: List[str] = Field(description="List of all verified sources used")

class NewsAnalystOutput(BaseModel):
    analyzed_stories: List[AnalyzedStory] = Field(description="List of stories with detailed actionable intelligence")

class MarketIntelligenceReport(BaseModel):
    report_title: str = Field(description="Title of the final intelligence report")
    trends_and_insights: str = Field(description="High-level overview of the major trends found")
    analyzed_stories: List[AnalyzedStory] = Field(description="The final list of analyzed stories")
    actionable_intelligence: str = Field(description="Concluding thoughts on how to act on this intelligence")
