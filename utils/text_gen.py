def generate_report_text(research, strategy):
    lines = []
    lines.append(f"# {research.report_title}")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append(research.executive_summary)
    lines.append("")
    lines.append("## Strategic Overview")
    lines.append(strategy.strategic_overview)
    lines.append("")
    lines.append("## Conclusion")
    lines.append(strategy.conclusion)
    lines.append("")
    
    lines.append("## Key Findings")
    for finding in research.findings:
        lines.append(f"### {finding.title}")
        lines.append(finding.explanation)
        lines.append(f"**Why it matters:** {finding.why_it_matters}")
        lines.append("")
        
    lines.append("## Recommendations")
    for rec in strategy.prioritized_recommendations:
        lines.append(f"### {rec.title}")
        lines.append(rec.description)
        lines.append(f"**Business Impact:** {rec.business_impact}")
        lines.append("")
        
    return "\n".join(lines)
