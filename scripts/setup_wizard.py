#!/usr/bin/env python3
"""
SMF SEO+GEO — Interactive Onboarding Wizard

This script runs interactively to configure the skill for a new organization.
It asks 8 questions and saves the answers to config.json.

Usage:
    python3 setup_wizard.py              # Interactive mode
    python3 setup_wizard.py --non-interactive  # Auto-config for testing
"""

import sys
import json
import os
from pathlib import Path
from datetime import datetime

CONFIG_DIR = Path.home() / ".smf" / "skills" / "smf-seo-gee"
CONFIG_FILE = CONFIG_DIR / "config.json"

def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

def load_config():
    ensure_config_dir()
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return get_default_config()

def save_config(config):
    ensure_config_dir()
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
    print(f"\n✅ Config saved to: {CONFIG_FILE}")

def get_default_config():
    return {
        "_schema_version": 1,
        "_setup_completed": False,
        "_setup_version": "1.0",
        "_created_at": None,
        "organization": {
            "domain": None,
            "name": None,
            "primary_services": None,
            "content_pillars": None,
            "target_audience": None,
            "audience_pain_points": None,
            "key_competitors": None,
            "existing_high_performing_content": None
        },
        "brand": {
            "voice": None,
            "cta_style": None,
            "author_name": None,
            "author_credentials": None
        },
        "preferences": {
            "default_word_count": 2000,
            "default_tone": "professional but approachable",
            "primary_platform": "google"
        }
    }

def ask_question(question, default=None, multiline=False):
    """Ask a question and return the answer."""
    if default:
        prompt = f"{question}\n[Default: {default}] > "
    else:
        prompt = f"{question} > "
    
    print(prompt, end="")
    sys.stdout.flush()
    
    if multiline:
        lines = []
        while True:
            line = sys.stdin.readline()
            if not line or line.strip() == "":
                break
            lines.append(line.rstrip())
        answer = "\n".join(lines)
    else:
        answer = sys.stdin.readline().strip()
    
    if not answer and default:
        return default
    return answer

def ask_yes_no(question, default="n"):
    """Ask a yes/no question."""
    default_val = "y" if default == "y" else "n"
    suffix = " [Y/n]" if default == "y" else " [y/N]"
    answer = ask_question(f"{question}{suffix}", default=default_val)
    return answer.lower() in ["y", "yes"]

def run_wizard():
    """Run the interactive setup wizard."""
    print("=" * 60)
    print("  SMF SEO+GEO — Onboarding Wizard")
    print("=" * 60)
    print()
    print("This wizard will configure the SEO+GEO skill for your organization.")
    print("Your answers are saved locally — never sent to any server.")
    print()
    print("Press Enter to accept defaults shown in [brackets].")
    print("Type multi-line answers (like a list), then press Enter on empty line to continue.")
    print()
    
    config = get_default_config()
    
    print("\n" + "=" * 60)
    print("  ORGANIZATION DETAILS")
    print("=" * 60)
    
    # Question 1: Domain
    config["organization"]["domain"] = ask_question(
        "1. What is your website domain?",
        default="example.com",
        multiline=False
    )
    
    # Question 2: Organization name
    config["organization"]["name"] = ask_question(
        "2. What is your organization/company name?",
        default="Acme Inc"
    )
    
    # Question 3: Primary services/products
    print("\n3. What are your primary services or products?")
    print("(Enter one per line, empty line when done)")
    services_lines = []
    while True:
        line = input("(service, press Enter when done) > ").strip()
        if not line:
            break
        services_lines.append(line)
    config["organization"]["primary_services"] = "\n".join(services_lines) if services_lines else None
    
    # Question 4: Content pillars
    print("\n4. What are your main content topic areas?")
    print("(These are your blog categories or areas of expertise)")
    pillars_lines = []
    while True:
        line = input("(content pillar, press Enter when done) > ").strip()
        if not line:
            break
        pillars_lines.append(line)
    config["organization"]["content_pillars"] = "\n".join(pillars_lines) if pillars_lines else None
    
    # Question 5: Target audience
    config["organization"]["target_audience"] = ask_question(
        "5. Who is your target audience?",
        default="Small business owners who need AI automation",
        multiline=True
    )
    
    # Question 6: Audience pain points
    print("\n6. What are your audience's main pain points?")
    pain_lines = []
    while True:
        line = input("(pain point, press Enter when done) > ").strip()
        if not line:
            break
        pain_lines.append(line)
    config["organization"]["audience_pain_points"] = "\n".join(pain_lines) if pain_lines else None
    
    # Question 7: Key competitors
    print("\n7. Who are your main competitors?")
    print("(For content gap analysis — websites you'd like to outrank)")
    competitors_lines = []
    while True:
        line = input("(competitor name or URL, press Enter when done) > ").strip()
        if not line:
            break
        competitors_lines.append(line)
    config["organization"]["key_competitors"] = "\n".join(competitors_lines) if competitors_lines else None
    
    # Question 8: Existing high-performing content
    print("\n8. Do you have existing high-performing content?")
    print("(Pages that already rank well — good for internal linking)")
    print("(Enter URLs or page titles, one per line, empty line when done)")
    content_lines = []
    while True:
        line = input("(URL or title, press Enter when done) > ").strip()
        if not line:
            break
        content_lines.append(line)
    config["organization"]["existing_high_performing_content"] = "\n".join(content_lines) if content_lines else None
    
    print("\n" + "=" * 60)
    print("  BRAND DETAILS")
    print("=" * 60)
    
    # Question 9: Brand voice
    print("\n9. How would you describe your brand voice?")
    print("(e.g., 'Direct and practical, no jargon' or 'Friendly and conversational')")
    config["brand"]["voice"] = ask_question(
        "Brand voice",
        default="Direct, practical, skip the jargon, no corporate fluff"
    )
    
    # Question 10: CTA style
    config["brand"]["cta_style"] = ask_question(
        "10. What is your preferred CTA style?",
        default="Clear and action-oriented"
    )
    
    # Question 11: Author name
    print("\n11. What name should appear on articles as the author?")
    config["brand"]["author_name"] = ask_question(
        "Author name",
        default="The Team"
    )
    
    # Question 12: Author credentials
    config["brand"]["author_credentials"] = ask_question(
        "12. What credentials/bio should appear with articles?",
        default="AI automation experts helping small businesses work smarter",
        multiline=True
    )
    
    print("\n" + "=" * 60)
    print("  PREFERENCES")
    print("=" * 60)
    
    # Question 13: Default word count
    word_count = ask_question(
        "13. Default target word count for articles",
        default="2000"
    )
    try:
        config["preferences"]["default_word_count"] = int(word_count)
    except ValueError:
        config["preferences"]["default_word_count"] = 2000
    
    # Question 14: Default tone
    config["preferences"]["default_tone"] = ask_question(
        "14. Default content tone",
        default="Professional but approachable"
    )
    
    # Question 15: Primary platform
    print("\n15. Which search/AI platform is your primary target?")
    print("(This determines which platforms we optimize GEO for)")
    platform = ask_question(
        "Primary platform",
        default="google"
    ).lower()
    if "chatgpt" in platform or "perplexity" in platform:
        config["preferences"]["primary_platform"] = "ai"
    else:
        config["preferences"]["primary_platform"] = "google"
    
    # Mark as complete
    config["_setup_completed"] = True
    config["_created_at"] = datetime.now().isoformat()
    
    # Save
    save_config(config)
    
    print("\n" + "=" * 60)
    print("  SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("Your SEO+GEO skill is configured and ready to use.")
    print(f"Config location: {CONFIG_FILE}")
    print()
    print("To reconfigure, run:")
    print(f"  python3 {__file__}")
    print()
    print("Now you can start creating SEO content. Try:")
    print('"Create an SEO article targeting [keyword]"')

def main():
    # Check for --non-interactive flag (for testing)
    if len(sys.argv) > 1 and sys.argv[1] == "--non-interactive":
        # Auto-configure with test values
        config = get_default_config()
        config["organization"]["domain"] = "example.com"
        config["organization"]["name"] = "Test Company"
        config["organization"]["primary_services"] = "AI automation\nLead generation\nChatbots"
        config["organization"]["content_pillars"] = "AI Tools\nAutomation\nSmall Business"
        config["organization"]["target_audience"] = "Small business owners"
        config["organization"]["audience_pain_points"] = "Time constraints\nLimited budget\nTech confusion"
        config["organization"]["key_competitors"] = "zapier.com\nmake.com"
        config["organization"]["existing_high_performing_content"] = "/blog/getting-started"
        config["brand"]["voice"] = "Direct and practical"
        config["brand"]["cta_style"] = "Get started free"
        config["brand"]["author_name"] = "Test Author"
        config["brand"]["author_credentials"] = "Tech writer"
        config["preferences"]["default_word_count"] = 2000
        config["preferences"]["default_tone"] = "Professional"
        config["preferences"]["primary_platform"] = "google"
        config["_setup_completed"] = True
        config["_created_at"] = datetime.now().isoformat()
        save_config(config)
        return
    
    run_wizard()

if __name__ == "__main__":
    main()
