#!/usr/bin/env python3
"""
SMF SEO+GEO — Content Optimization Engine
Main entry point for smfw CLI integration.

Usage:
    python3 main.py                    # Check status / guide user
    python3 main.py configure          # Run setup wizard
    python3 main.py reconfigure        # Reset and run setup wizard
    python3 main.py status             # Check configuration status
    python3 main.py get <key>         # Get config value
    python3 main.py quick-test <kw>    # Quick SEO keyword test

Requires: SMF Works Pro subscription (smf login)
"""

import sys
import os
import json
from pathlib import Path

# Add bundled auth as fallback (for standalone install)
SCRIPT_DIR = Path(__file__).parent
bundled_auth = SCRIPT_DIR / "shared_auth.py"
if bundled_auth.exists():
    sys.path.insert(0, str(SCRIPT_DIR))
    try:
        from shared_auth import require_subscription, show_subscription_error
        HAS_AUTH = True
    except ImportError:
        HAS_AUTH = False
elif shared_path.exists():
    # Use shared auth from full repo install
    sys.path.insert(0, str(shared_path))
    try:
        from smf_auth import require_subscription, show_subscription_error
        HAS_AUTH = True
    except ImportError:
        HAS_AUTH = False
else:
    HAS_AUTH = False

# Add scripts directory to path for imports
scripts_path = SCRIPT_DIR / "scripts"
if scripts_path.exists():
    sys.path.insert(0, str(scripts_path))

try:
    from config_manager import (
        load_config, save_config, is_setup_complete,
        mark_setup_complete, reset_config, get_organization, get_brand, get_preferences
    )
except ImportError:
    # Fallback if config_manager not available
    CONFIG_DIR = Path.home() / ".smf" / "skills" / "smf-seo-gee"
    CONFIG_FILE = CONFIG_DIR / "config.json"
    
    def load_config():
        if CONFIG_FILE.exists():
            return json.loads(CONFIG_FILE.read_text())
        return {}
    
    def is_setup_complete():
        return load_config().get("_setup_completed", False)
    
    def reset_config():
        if CONFIG_FILE.exists():
            CONFIG_FILE.unlink()

# Skill configuration
SKILL_NAME = "smf-seo-gee"
MIN_TIER = "pro"

# Commands that require subscription
PRO_COMMANDS = {"configure", "reconfigure", "status", "get", "update", "quick-test"}


def check_pro_subscription():
    """Verify user has Pro subscription before allowing skill use."""
    if not HAS_AUTH:
        # Auth not available — allow in development/dev mode
        print("⚠️  Warning: Auth system not available, skipping subscription check")
        return True
    
    result = require_subscription(SKILL_NAME, MIN_TIER)
    
    if not result.get("valid"):
        print("❌ SMF SEO+GEO — Pro Skill")
        print("=" * 40)
        show_subscription_error(result)
        return False
    
    return True


def run_wizard():
    """Run the setup wizard."""
    wizard_path = SCRIPT_DIR / "scripts" / "setup_wizard.py"
    if wizard_path.exists():
        os.system(f"python3 {wizard_path}")
    else:
        print("Error: setup_wizard.py not found")
        sys.exit(1)

def show_status():
    """Show configuration status."""
    config = load_config()
    
    if config.get("_setup_completed"):
        print("✅ SEO+GEO is configured and ready!")
        print()
        org = config.get("organization", {})
        print(f"Domain: {org.get('domain', 'Not set')}")
        print(f"Organization: {org.get('name', 'Not set')}")
        print(f"Content pillars: {org.get('content_pillars', 'Not set')}")
        print()
        brand = config.get("brand", {})
        print(f"Brand voice: {brand.get('voice', 'Not set')}")
        print(f"Author: {brand.get('author_name', 'Not set')}")
    else:
        print("⚠️ SEO+GEO is not configured.")
        print()
        print("Run 'smfw run smf-seo-gee configure' to set up.")

def quick_test(keyword):
    """Quick SEO keyword analysis."""
    print(f"\n🔍 Quick SEO Keyword Analysis: {keyword}")
    print("=" * 50)
    print()
    print("This feature requires OpenClaw's web_search tool.")
    print()
    print("In OpenClaw, say:")
    print(f'"Analyze the keyword "{keyword}" for SEO and GEO"')
    print()
    print("Or create a full article:")
    print(f'"Create an SEO article targeting: {keyword}"')

def main():
    if len(sys.argv) < 2:
        # No arguments — check if configured and guide user
        if is_setup_complete():
            print("SMF SEO+GEO — Pro Skill ✅")
            print()
            print("Usage:")
            print("  smfw run smf-seo-gee status        Check configuration")
            print("  smfw run smf-seo-gee configure     Reconfigure settings")
            print("  smfw run smf-seo-gee quick-test <keyword>  Quick keyword test")
        else:
            print("Welcome to SMF SEO+GEO!")
            print()
            print("Run 'smfw run smf-seo-gee configure' to set up for your organization.")
        sys.exit(0)
    
    cmd = sys.argv[1].lower()
    
    # Check subscription for Pro commands
    if cmd in PRO_COMMANDS:
        if not check_pro_subscription():
            sys.exit(1)
    
    if cmd == "configure":
        run_wizard()
    elif cmd == "reconfigure":
        print("Resetting configuration...")
        reset_config()
        run_wizard()
    elif cmd == "status":
        show_status()
    elif cmd == "get":
        if len(sys.argv) >= 3:
            key = sys.argv[2]
            config = load_config()
            # Navigate nested keys
            parts = key.split(".")
            val = config
            for part in parts:
                val = val.get(part, {})
            if isinstance(val, dict):
                print(json.dumps(val, indent=2))
            else:
                print(val)
        else:
            print("Usage: get <key> (e.g., organization.domain)")
    elif cmd == "update":
        if len(sys.argv) >= 4:
            key = sys.argv[2]
            value = sys.argv[3]
            print(f"Updating {key} = {value}")
            print("(Use the configure wizard for full setup)")
        else:
            print("Usage: update <key> <value>")
    elif cmd == "quick-test":
        keyword = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "your keyword"
        quick_test(keyword)
    elif cmd in ["help", "--help", "-h"]:
        print(__doc__)
    else:
        print(f"Unknown command: {cmd}")
        print("Usage: smf-seo-gee [configure|status|quick-test]")
        sys.exit(1)

if __name__ == "__main__":
    main()
