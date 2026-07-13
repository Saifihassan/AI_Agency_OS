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


class Source(BaseModel):
    title: str = Field(description="Title of the source")
    url: str = Field(description="Source URL")
    publisher: str = Field(description="Publisher or website name")


class Finding(BaseModel):
    title: str = Field(
        description="A short title describing the key finding."
    )

    explanation: str = Field(
        description="Explain the finding in 2-3 concise sentences."
    )

    why_it_matters: str = Field(
        description="Explain the business or market impact of this finding."
    )

    evidence: List[str] = Field(
        description="Supporting facts or statistics for this finding."
    )

    sources: List[Source] = Field(
        description="Sources supporting this finding."
    )


class ResearchAnalysis(BaseModel):
    report_title: str = Field(
        description="Title of the research report."
    )

    research_topic: str = Field(
        description="Topic or company researched."
    )

    executive_summary: str = Field(
        description="A concise overview of the research in 3-5 sentences."
    )

    findings: List[Finding] = Field(
        description="The 3-5 most important research findings."
    )


class StrategyRecommendation(BaseModel):
    title: str = Field(description="Title of the recommendation")
    description: str = Field(description="Detailed explanation of the practical action")
    business_impact: str = Field(description="Expected business impact or ROI")

class StrategyQuickWin(BaseModel):
    title: str = Field(description="Title of the quick win")
    action_steps: List[str] = Field(description="Actionable steps to implement immediately")

class StrategyLongTermOpportunity(BaseModel):
    title: str = Field(description="Title of the long term opportunity")
    description: str = Field(description="Description of the opportunity and why it matters")

class StrategyReport(BaseModel):
    strategic_overview: str = Field(description="A strategic overview based on the research findings")
    prioritized_recommendations: List[StrategyRecommendation] = Field(description="4-6 prioritized recommendations")
    quick_wins: List[StrategyQuickWin] = Field(description="Quick wins that can be implemented immediately")
    long_term_opportunities: List[StrategyLongTermOpportunity] = Field(description="Long-term opportunities identified")
    conclusion: str = Field(description="A concise conclusion")
