from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class NewsArticle(BaseModel):
    title: str = Field(description="Headline of the article")
    category: str = Field(description="AI, Marketing, SEO, Social Media, Advertising, Startups, Business Technology")
    source: str = Field(description="Publisher")
    url: str = Field(description="Article URL")
    published_date: str = Field(description="Publication date")
    summary: str = Field(description="2-3 sentence factual summary")

class NewsResearch(BaseModel):
    articles: List[NewsArticle] = Field(
        description="Latest curated news articles"
    )

class CategorizedNews(BaseModel):
    category: str = Field(description="News category")
    articles: List[NewsArticle] = Field(
        description="Articles belonging to this category"
    )

class MarketOpportunity(BaseModel):
    title: str = Field(description="Opportunity title")
    description: str = Field(
        description="How agencies can capitalize on this opportunity"
    )

class MarketTrend(BaseModel):
    title: str = Field(description="Trend title")
    description: str = Field(
        description="Explanation of the trend"
    )

class MarketIntelligenceReport(BaseModel):
    generated_at: str = Field(description="Timestamp")

    one_liner_headlines: List[str] = Field(
        description="Short dashboard headlines"
    )

    categorized_news: List[CategorizedNews] = Field(
        description="News grouped by category"
    )

    market_trends: List[MarketTrend] = Field(
        description="Major trends observed"
    )

    opportunities: List[MarketOpportunity] = Field(
        description="Business opportunities for agencies"
    )



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


class CampaignPlan(BaseModel):
    business_summary: str
    target_audience: str
    campaign_goal: str
    campaign_angle: str
    tone_of_voice: str
    key_selling_points: List[str]
    primary_cta: str
    platforms: List[str]

class ContentGenerationRequest(BaseModel):
    campaign_plan: CampaignPlan
    requested_assets: List[str]

class CampaignAssets(BaseModel):
    campaign_strategy: Optional[str] = None
    marketing_copy: Optional[str] = None
    email_copy: Optional[str] = None
    social_posts: Optional[List[str]] = None
    cta_suggestions: Optional[List[str]] = None
    hashtags: Optional[List[str]] = None

class ProspectAnalysis(BaseModel):
    company_summary: str
    target_audience: str
    current_positioning: str
    identified_pain_points: List[str]
    outreach_angle: str
    value_proposition: str
    service_offered: str

class OutreachSequence(BaseModel):
    tone: Literal["Friendly", "Professional", "Consultative", "Direct", "Founder-to-Founder"]
    subject_lines: List[str]
    cold_email: str
    follow_up_email_1: str
    follow_up_email_2: str
    call_to_action: str

class CompanySnapshot(BaseModel):
    company_name: str = Field(description="Name of the company")
    company_overview: str = Field(description="Short overview of the company")
    industry: str = Field(description="Industry or category")
    target_audience: str = Field(description="Primary customer segments")
    market_position: str = Field(description="Leader, Challenger, Niche Player, Emerging, etc.")
    core_differentiator: str = Field(description="The company's primary competitive advantage")

class Opportunity(BaseModel):
    title: str = Field(description="Short opportunity title")
    description: str = Field(description="Explanation of the opportunity")

class CompetitiveAnalysis(BaseModel):
    company_snapshot: CompanySnapshot = Field(
        description="Overview of the analyzed company"
    )
    strengths: List[str] = Field(
        description="Company strengths"
    )
    weaknesses: List[str] = Field(
        description="Company weaknesses"
    )
    opportunities: List[Opportunity] = Field(
        description="Potential market or product opportunities"
    )
    recommended_strategy: str = Field(
        description="Actionable strategy for competing against this company"
    )