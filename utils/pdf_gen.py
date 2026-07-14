from fpdf import FPDF

def sanitize_text(text: str) -> str:
    if not text:
        return ""
    replacements = {
        '—': '-',
        '–': '-',
        '“': '"',
        '”': '"',
        '‘': "'",
        '’': "'",
        '…': '...',
        '\u200b': '',
        '\xa0': ' ',
        '•': '-',
        '™': '(TM)',
        '©': '(C)',
        '®': '(R)'
    }
    for search, replace in replacements.items():
        text = text.replace(search, replace)
    
    return text.encode('latin-1', 'replace').decode('latin-1')

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('helvetica', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Research Report', 0, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

def generate_pdf(research, strategy):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Title
    pdf.set_font('helvetica', 'B', 16)
    pdf.multi_cell(0, 10, sanitize_text(research.report_title), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    # Executive Summary
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'Executive Summary', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('helvetica', '', 12)
    pdf.multi_cell(0, 10, sanitize_text(research.executive_summary), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    # Strategic Overview
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'Strategic Overview', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('helvetica', '', 12)
    pdf.multi_cell(0, 10, sanitize_text(strategy.strategic_overview), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    # Conclusion
    pdf.set_font('helvetica', 'B', 14)
    pdf.cell(0, 10, 'Conclusion', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('helvetica', '', 12)
    pdf.multi_cell(0, 10, sanitize_text(strategy.conclusion), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    # Findings
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'Key Findings', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    for finding in research.findings:
        pdf.set_font('helvetica', 'B', 12)
        pdf.multi_cell(0, 8, sanitize_text(finding.title), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('helvetica', '', 12)
        pdf.multi_cell(0, 8, sanitize_text(finding.explanation), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('helvetica', 'I', 11)
        pdf.multi_cell(0, 8, sanitize_text(f"Why it matters: {finding.why_it_matters}"), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)
        
    # Recommendations
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'Recommendations', new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    for rec in strategy.prioritized_recommendations:
        pdf.set_font('helvetica', 'B', 12)
        pdf.multi_cell(0, 8, sanitize_text(rec.title), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('helvetica', '', 12)
        pdf.multi_cell(0, 8, sanitize_text(rec.description), new_x="LMARGIN", new_y="NEXT")
        pdf.set_font('helvetica', 'I', 11)
        pdf.multi_cell(0, 8, sanitize_text(f"Business Impact: {rec.business_impact}"), new_x="LMARGIN", new_y="NEXT")
        pdf.ln(5)
        
    # Output to bytes
    return bytes(pdf.output())
