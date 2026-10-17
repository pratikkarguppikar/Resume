#!/usr/bin/env python3
"""Generate an ATS-friendly PDF resume for Pratik Karguppikar.

Produces a clean, single-column, selectable-text PDF (no tables, no columns,
standard fonts) so applicant tracking systems parse it reliably.
"""
from __future__ import annotations

from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUTPUT = "Pratik-Karguppikar-Resume.pdf"

NAVY = "#1a1a2e"
ACCENT = "#0f4c81"
RULE = "#c9ccd1"


def _styles():
    base = getSampleStyleSheet()
    styles = {}
    styles["name"] = ParagraphStyle(
        "name", parent=base["Normal"], fontName="Helvetica-Bold",
        fontSize=20, leading=23, alignment=TA_CENTER, textColor=NAVY,
        spaceAfter=2,
    )
    styles["title"] = ParagraphStyle(
        "title", parent=base["Normal"], fontName="Helvetica-Bold",
        fontSize=10.5, leading=13, alignment=TA_CENTER, textColor=ACCENT,
        spaceAfter=4,
    )
    styles["contact"] = ParagraphStyle(
        "contact", parent=base["Normal"], fontName="Helvetica",
        fontSize=8.8, leading=12, alignment=TA_CENTER, textColor="#333333",
    )
    styles["auth"] = ParagraphStyle(
        "auth", parent=base["Normal"], fontName="Helvetica-Bold",
        fontSize=8.8, leading=12, alignment=TA_CENTER, textColor=NAVY,
        spaceAfter=2,
    )
    styles["section"] = ParagraphStyle(
        "section", parent=base["Normal"], fontName="Helvetica-Bold",
        fontSize=11, leading=13, textColor=ACCENT, spaceBefore=8,
        spaceAfter=3,
    )
    styles["role"] = ParagraphStyle(
        "role", parent=base["Normal"], fontName="Helvetica-Bold",
        fontSize=9.8, leading=12, textColor=NAVY, spaceBefore=5,
    )
    styles["dates"] = ParagraphStyle(
        "dates", parent=base["Normal"], fontName="Helvetica-Oblique",
        fontSize=8.6, leading=11, textColor="#555555", spaceAfter=2,
    )
    styles["body"] = ParagraphStyle(
        "body", parent=base["Normal"], fontName="Helvetica",
        fontSize=9.2, leading=12.6, alignment=TA_LEFT, textColor="#1f1f1f",
        spaceAfter=2,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", parent=base["Normal"], fontName="Helvetica",
        fontSize=9.2, leading=12.6, alignment=TA_LEFT, textColor="#1f1f1f",
        leftIndent=9, bulletIndent=0, spaceAfter=1.5,
    )
    return styles


def _rule():
    return HRFlowable(width="100%", thickness=0.6, color=RULE,
                      spaceBefore=2, spaceAfter=3)


def _section(story, s, title):
    story.append(Paragraph(title, s["section"]))
    story.append(_rule())


def _bullets(story, s, items):
    for it in items:
        story.append(Paragraph(it, s["bullet"], bulletText="\u2022"))


def build():
    s = _styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=16 * mm, rightMargin=16 * mm,
        topMargin=12 * mm, bottomMargin=12 * mm,
        title="Pratik Karguppikar - Resume",
        author="Pratik Karguppikar",
    )
    story = []

    # Header
    story.append(Paragraph("Pratik Karguppikar", s["name"]))
    story.append(Paragraph(
        "Detection Engineering&nbsp; |&nbsp; Cloud Security&nbsp; |&nbsp; "
        "Application Security", s["title"]))
    story.append(Paragraph(
        "1902 Gateway Tower, 28 Western Gateway, London E16 1YN", s["contact"]))
    story.append(Paragraph(
        "+44 7796 375358&nbsp; |&nbsp; pratikarguppikar29@gmail.com&nbsp; |&nbsp; "
        "linkedin.com/in/Pratik-Karguppikar", s["contact"]))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "Work Authorization: UK dependent visa with full right to work. "
        "No sponsorship required.", s["auth"]))
    story.append(Spacer(1, 3))

    # Summary
    _section(story, s, "PROFESSIONAL SUMMARY")
    story.append(Paragraph(
        "Security engineer with 8+ years across detection engineering, threat "
        "hunting, and security automation, backed by hands-on cloud security "
        "(AWS, Azure) and application security (SAST, DAST, SCA) work. I build "
        "TTP-focused detections in Sigma, YARA, and Python mapped to MITRE ATT&amp;CK, "
        "and I run them as detection-as-code in Splunk and Elasticsearch across "
        "endpoint, network, and cloud telemetry. Comfortable owning SOAR-driven "
        "incident response, third-party and supply-chain risk management, and "
        "compliance work such as PCI DSS 4.0. I delivered detections at Morgan "
        "Stanley and BNP Paribas, and today I help architect an AI-assisted security "
        "operations platform that ties together 40+ security services.", s["body"]))

    # Skills
    _section(story, s, "TECHNICAL SKILLS")
    skills = [
        ("Detection Engineering &amp; Threat Hunting", "Detection-as-Code, MITRE "
         "ATT&amp;CK, Cyber Kill Chain, Sigma, YARA, Hypothesis-driven threat hunting, "
         "Threat intelligence (CTI), Alert tuning, Attack simulation (Atomic Red Team, "
         "Caldera)"),
        ("SIEM, SOAR &amp; Log Analysis", "Splunk (SPL), Splunk Enterprise Security, "
         "Elasticsearch, Kibana, Microsoft Sentinel, KQL, Elasticsearch Query DSL, "
         "SOAR automation, Grok, Regex"),
        ("Endpoint &amp; Network Security", "Microsoft Defender for Endpoint, "
         "CrowdStrike, Trend Micro, EDR telemetry analysis and deployment, Sysmon, "
         "auditd, Zeek, IDS/IPS, Packet analysis (Wireshark), TCP/IP"),
        ("Cloud Security &amp; Infrastructure", "AWS (GuardDuty, WAF, CloudTrail, "
         "IAM), Azure, Cloud security monitoring, Cloud log collection for SIEM, "
         "Docker, Kubernetes, Terraform (Infrastructure as Code)"),
        ("Application Security", "SAST (Static Application Security Testing), DAST "
         "(Dynamic Application Security Testing), SCA (Software Composition Analysis), "
         "CI/CD pipeline security, OWASP Top 10, Burp Suite"),
        ("Governance, Risk &amp; Compliance", "Incident response (NIST/SANS "
         "lifecycle), Alert triage and investigation, Third-party and supply-chain "
         "risk management (SecurityScorecard, BitSight), PCI DSS 4.0, Static and "
         "dynamic malware analysis, PE file triage (PeStudio, PEiD), Sandboxing "
         "(Cuckoo Sandbox, ANY.RUN)"),
        ("Automation &amp; Scripting", "Python, PowerShell, Bash, REST API "
         "integration, Log parsing, Security automation, Anomaly detection, "
         "AI-assisted automation, Jupyter Notebook"),
    ]
    for label, body in skills:
        story.append(Paragraph(f"<b>{label}:</b> {body}", s["body"]))

    # Experience
    _section(story, s, "PROFESSIONAL EXPERIENCE")

    story.append(Paragraph(
        "Senior Security Engineer, Verint Systems (Remote)", s["role"]))
    story.append(Paragraph("August 2023 to Present", s["dates"]))
    _bullets(story, s, [
        "Built an enterprise security operations platform that connects 40+ "
        "security services through unified Python APIs, so teams can enrich, "
        "correlate, and respond to alerts across tools from one place",
        "Wrote and tuned detection rules mapped to MITRE ATT&amp;CK in Splunk and "
        "CrowdStrike using Sigma, KQL, and Python, managing them as detection-as-code "
        "and refining them with triage feedback to cut false positives",
        "Ran hypothesis-driven threat hunts with teammates across endpoint, cloud, "
        "and identity telemetry, turning findings into new detections and documented "
        "hunt playbooks",
        "Rolled out Endpoint Detection and Response (EDR) across 20,000+ devices "
        "through automation, improving threat visibility and supporting PCI DSS 4.0 "
        "compliance",
        "Led third-party and supply-chain risk management with SecurityScorecard, "
        "lifting the enterprise security posture rating from 72 to 95",
        "Piloted and rolled out BitSight for third-party risk, streamlining vendor "
        "security assessments and saving around $26K a year",
        "Added SAST, DAST, and SCA scanning to CI/CD pipelines, noticeably reducing "
        "the vulnerabilities that reached production",
        "Built AI-driven change advisory and ticket-resolution systems that flag "
        "risk and track SLA compliance across the estate",
        "Created an automated security task-distribution system that handles 500+ "
        "tasks a month through Jira workflows and containerized deployments",
    ])

    story.append(Paragraph(
        "Senior Associate, Threat Hunt and Detection Engineering, "
        "Morgan Stanley (Bengaluru, India)", s["role"]))
    story.append(Paragraph("March 2022 to July 2023", s["dates"]))
    _bullets(story, s, [
        "Developed TTP-focused detection analytics in Sigma, YARA, and Python mapped "
        "to MITRE ATT&amp;CK, managed as detection-as-code in Splunk and CrowdStrike "
        "to catch adversary activity across the firm's networks",
        "Built alerts from raw and aggregated telemetry and enrichment sources, "
        "aligned to MITRE ATT&amp;CK tactics and techniques and mapped to internal "
        "security use cases",
        "Automated triage and investigation workflows that pivot across Sysmon "
        "(Windows), auditd (Linux), and CmdReporter (macOS) telemetry",
        "Ran proactive threat hunts, investigated phishing, access-control "
        "violations, endpoint events, and network anomalies, and responded to "
        "security incidents",
    ])

    story.append(Paragraph(
        "Information Security Engineer, Logging and Detection, "
        "BNP Paribas (Mumbai, India)", s["role"]))
    story.append(Paragraph("December 2020 to March 2022", s["dates"]))
    _bullets(story, s, [
        "Wrote Grok parsing patterns to ingest IT infrastructure logs into "
        "Elasticsearch",
        "Built SIEM use cases and Kibana dashboards for real-time threat detection",
        "Created Elasticsearch Query DSL queries and Sigma rules mapped to MITRE "
        "ATT&amp;CK, strengthening enterprise threat detection coverage",
    ])

    story.append(Paragraph(
        "Senior Associate, Security Intelligence, Netsurion "
        "Technologies Private Limited (Bengaluru, India)", s["role"]))
    story.append(Paragraph("December 2017 to December 2020", s["dates"]))
    _bullets(story, s, [
        "Analysed customer-submitted malicious process samples using static and "
        "dynamic analysis, including memory dump analysis, and wrote detailed "
        "reports",
        "Built SIEM and Kibana dashboards, threat hunting rules, and security use "
        "cases for managed security service clients, and tuned alerts to catch "
        "threats in real time",
        "Wrote PowerShell and Python integrations that pulled security data from "
        "cloud infrastructure and network devices into the SIEM for monitoring",
        "Deployed and ran attack simulation frameworks (Red Canary's Atomic Red "
        "Team, Caldera) to validate security controls against emerging techniques",
    ])

    # Education
    _section(story, s, "EDUCATION")
    story.append(Paragraph(
        "<b>Bachelor of Engineering (BE), Computer Science</b>, "
        "Visvesvaraya Technological University, Bengaluru, India", s["body"]))
    story.append(Paragraph("August 2013 to May 2017", s["dates"]))

    doc.build(story)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build()
