"""Contains the context used to render repeated parts of the site."""

from django.http import HttpRequest


def global_context(
    request: HttpRequest,
) -> dict:
    """Context processor that provides global context for all templates.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: The global context dictionary.
    """
    return {
        "title": "Emiliano Garcia | Cybersecurity Professional",
        "name": "Emiliano Garcia",
        "headline": "Cybersecurity Engineer | Specialized in DevSecOps, Automation, & Infrastructure as Code (IaC)",
        "status": "Available for New Projects (Madrid, Spain)",
        "skills": [
            "Python",
            "Security Automation",
            "CI/CD (Azure DevOps and GitHub Actions)",
            "Edge Security & Content Delivery (Akamai & Cloudflare)",
            "Infrastructure as Code (IaC)",
            "DDoS Mitigation",
            "Threat Hunting",
            "Trellix DLP",
            "Cloud Security",
            "SIEM Tools (Splunk & Wazuh)",
        ],
        "certifications": [
            {
                "name": "Akamai Automation and DevOps",
                "link": "https://www.credly.com/badges/eee249f5-2eb1-4095-9c62-e134d98d9722",
            },
            {
                "name": "Akamai Web Application & API Protection",
                "link": "https://www.credly.com/badges/fc157702-9d85-4ebb-975c-b2c84e9e8232",
            },
            {
                "name": "Akamai Web Performance Foundations",
                "link": "https://www.credly.com/badges/6abdd5e7-7cc9-4d7c-b733-b89240b07adb",
            },
            {
                "name": "CompTIA Cloud+",
                "link": "https://www.credly.com/badges/83dea2c7-5aef-40a7-a38b-234dbe5a9f0f/public_url",
            },
            {
                "name": "GIAC Security Essentials (GSEC)",
                "link": "https://www.credly.com/badges/ee786c6a-136a-4d22-85d6-885fe9cf3ecc",
            },
            {
                "name": "GIAC Cloud Security Essentials (GCLD)",
                "link": "https://www.credly.com/badges/e1685605-c023-4e24-a050-0e198ce55a75/public_url",
            },
            {
                "name": "Cisco CCNA",
                "link": "https://www.credly.com/badges/42216b34-457a-4e93-b1ae-b7d8018cc175",
            },
            {
                "name": "Certified Wireless Technician (CWT)",
                "link": "https://certified.certitrek.com/a8cbcc08-d71a-4338-8936-80ac674f5361#acc.6T79aoXj",
            },
            {
                "name": "eJPT",
                "link": "https://certs.ine.com/e73d7050-aa0e-4fdf-9ef4-600d5d85fcee#acc.pUjDIWEJ",
            },
            {
                "name": "GIAC Foundational Cybersecurity Technologies (GFACT)",
                "link": "https://www.credly.com/badges/afb1b17a-9623-466c-af08-de7e43b7d342/public_url",
            },
        ],
        "location": "Madrid, Spain",
        "education": [
            {
                "degree": "B.S. in Network Engineering and Security",
                "institution": "Western Governors University",
                "year": "02/2024 – 08/2024",
            },
            {
                "degree": "A.A.S. in Information Systems Cybersecurity",
                "institution": "Collin College",
                "year": "08/2022 – 12/2023",
            },
        ],
        "experiences": [
            {
                "position": "Cybersecurity Engineer",
                "company": "GM Financial",
                "location": "Irving, TX, USA",
                "period": "10/2024 – Present",
                "achievements": [
                    "Architected a hybrid IaC pipeline using Python and Terraform to automate the onboarding of Akamai CDN and CPS configurations, reducing application onboarding time from hours to minutes while eliminating 100% of manual configuration drift.",
                    "Automated Akamai WAF signature updates from implementation to validation using Python and Azure DevOps (CI/CD), including integrations with the ServiceNow API to ensure full compliance with corporate change management policy.",
                    "Automated Akamai third-party certificate renewals by developing Python tooling integrated with the Venafi, Akamai CPS, and ServiceNow APIs.",
                    "Developed a configuration validation tool using Python and Azure DevOps that audits Akamai WAF/CDN configurations for drift.",
                    "Executed emergency mitigation of one of the largest recorded DDoS attacks in Akamai's history (1+ Tbps) by deploying advanced TLS Fingerprinting techniques.",
                    "Scaled an Identity Threat Detection and Response (ITDR) solution across all active directory domains and Entra ID, encompassing over 30,000 devices.",
                    "Engineered Trellix DLP classifications for Latin American regions using advanced Regex and keyword patterns.",
                ],
            },
            {
                "position": "Cybersecurity Analyst",
                "company": "InfoDefense",
                "location": "Remote",
                "period": "06/2023 – 10/2024",
                "achievements": [
                    "Performed security monitoring and threat-hunting operations for multiple customers using Wazuh (SIEM) + ELK stack.",
                    "Effectively triaged, remediated, and resolved security incidents across diverse environments.",
                    "Developed Python and Bash scripts, along with Ansible playbooks, to automate tasks.",
                    "Implemented a vulnerability management program by conducting vulnerability assessments using OpenVAS.",
                    "Enhanced infrastructure security by deploying MFA across infrastructure for NIST SP 800-171 (CMMC) compliance.",
                    "Secured networks and servers by developing hardened standards and procedures.",
                ],
            },
            {
                "position": "SOC Analyst",
                "company": "Mint-Technologies",
                "location": "Fairview, TX, USA",
                "period": "08/2022 – 10/2022",
                "achievements": [
                    "Leveraged AbuseIPDB, VirusTotal, and AlienVault OTX for threat hunting.",
                    "Performed threat hunting for multiple customers using the AlienVault USM Appliance.",
                    "Investigated and escalated security alerts about malware and phishing.",
                ],
            },
        ],
        "projects": [
            {
                "name": "Personal Portfolio",
                "period": "03/2026 – Present",
                "description": "This site! Built with Django and Tailwind CSS, deployed via a CI/CD pipeline featuring automated security scans, tests, and Podman container builds.",
                "url": "https://github.com/AeshEmi1/portfolio",
            },
            {
                "name": "Home/VPS Lab",
                "period": "01/2023 – Present",
                "description": "The Linux server hosting this site (and others)! Previously used as an SSH Honeypot. Is also used as a callback server for bug bounties.",
            },
            {
                "name": "Searxng-SE",
                "period": "03/2025 - 08/2025",
                "description": "A fork of SearxNG that added TLS support for the backend flask application.",
                "url": "https://github.com/AeshEmi1/searxng-se",
            },
            {
                "name": "Bug Bounty Scripts",
                "period": "03/2025 – 08/2025",
                "description": "A collection of scripts used to automate reconnaissance. These tools focus on subdomain enumeration and origin discovery.",
                "url": "https://github.com/AeshEmi1/bug-bounty-scripts",
            },
        ],
        "defensive_engineering": {
            "threat_mitigation_and_response": [
                {
                    "category": "DDoS Mitigation",
                    "description": "Managed the emergency mitigation of a 1+ Tbps DDoS attack—one of the largest in Akamai’s history—utilizing advanced TLS Fingerprinting.",
                },
                {
                    "category": "Vulnerability Research",
                    "description": "Identified and documented broken access control and DoS vulnerabilities (CVE-2002–20001).",
                },
                {
                    "category": "Identity Hardening",
                    "description": "Scaled ITDR (Identity Threat Detection and Response) across 30,000+ devices to secure Active Directory and Entra ID.",
                },
            ],
            "security_automation": [
                {
                    "category": "Governance as Code",
                    "description": "Built a configuration validation tool in Python and Azure DevOps to audit WAF/CDN drift against organizational standards.",
                },
                {
                    "category": "ML-Driven Defense",
                    "description": "Developed a DLP false-positive analysis tool using K-Means clustering to optimize rule accuracy and reduce alert fatigue.",
                },
                {
                    "category": "Pipeline Automation",
                    "description": "Architected a hybrid IaC pipeline using Terraform to automate Akamai CDN onboardings, reducing deployment time from hours to minutes.",
                },
            ],
            "tooling_and_platforms": [
                {
                    "category": "Core Stack",
                    "description": "Expert-level utilization of Python, Github Actions and Azure DevOps, Linux, Akamai WAF and CDN, and Trellix DLP.",
                },
                {
                    "category": "Frameworks",
                    "description": "Implementation of ZTNA, mTLS, and CIS Benchmarks across enterprise Linux and Windows environments.",
                },
                {
                    "category": "Continuous Learning",
                    "description": "Active labs on TryHackMe and HackTheBox; holder of GSEC, GCLD, and CCNA.",
                },
            ],
        },
        "email": "jobs@emilspace.com",
        "linkedin": "https://www.linkedin.com/in/emiliano-garcia000/",
        "github": "https://github.com/AeshEmi1",
    }
