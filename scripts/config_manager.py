#!/usr/bin/env python3
"""
SMF SEO+GEO — Setup Configuration Helper
Reads and writes config for the SMF SEO+GEO skill.
"""

import sys
import json
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".smf" / "skills" / "smf-seo-gee"
CONFIG_FILE = CONFIG_DIR / "config.json"

def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        default_config = {
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
        CONFIG_FILE.write_text(json.dumps(default_config, indent=2))
    return CONFIG_FILE

def load_config():
    ensure_config_dir()
    return json.loads(CONFIG_FILE.read_text())

def save_config(config):
    ensure_config_dir()
    CONFIG_FILE.write_text(json.dumps(config, indent=2))

def is_setup_complete():
    config = load_config()
    return config.get("_setup_completed", False)

def mark_setup_complete():
    config = load_config()
    config["_setup_completed"] = True
    from datetime import datetime
    config["_created_at"] = datetime.now().isoformat()
    save_config(config)

def update_organization(**kwargs):
    config = load_config()
    for key, value in kwargs.items():
        if key in config["organization"]:
            config["organization"][key] = value
    save_config(config)

def update_brand(**kwargs):
    config = load_config()
    for key, value in kwargs.items():
        if key in config["brand"]:
            config["brand"][key] = value
    save_config(config)

def update_preferences(**kwargs):
    config = load_config()
    for key, value in kwargs.items():
        if key in config["preferences"]:
            config["preferences"][key] = value
    save_config(config)

def get_organization():
    return load_config().get("organization", {})

def get_brand():
    return load_config().get("brand", {})

def get_preferences():
    return load_config().get("preferences", {})

def show_config():
    config = load_config()
    print(json.dumps(config, indent=2))

def reset_config():
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
    ensure_config_dir()
    print("Config reset to defaults.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_config()
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == "show":
        show_config()
    elif cmd == "complete":
        mark_setup_complete()
        print("Setup marked as complete.")
    elif cmd == "reset":
        reset_config()
    elif cmd == "is-ready":
        print("yes" if is_setup_complete() else "no")
    elif cmd == "update-org":
        # update-org key value
        if len(sys.argv) >= 4:
            update_organization(**{sys.argv[2]: sys.argv[3]})
            print(f"Updated organization.{sys.argv[2]}")
        else:
            print("Usage: update-org <key> <value>")
    elif cmd == "update-brand":
        if len(sys.argv) >= 4:
            update_brand(**{sys.argv[2]: sys.argv[3]})
            print(f"Updated brand.{sys.argv[2]}")
        else:
            print("Usage: update-brand <key> <value>")
    elif cmd == "update-prefs":
        if len(sys.argv) >= 4:
            update_preferences(**{sys.argv[2]: sys.argv[3]})
            print(f"Updated preferences.{sys.argv[2]}")
        else:
            print("Usage: update-prefs <key> <value>")
    elif cmd == "get":
        if len(sys.argv) >= 3:
            section = sys.argv[2]
            config = load_config()
            if section == "org":
                print(json.dumps(config.get("organization", {}), indent=2))
            elif section == "brand":
                print(json.dumps(config.get("brand", {}), indent=2))
            elif section == "prefs":
                print(json.dumps(config.get("preferences", {}), indent=2))
            else:
                print(json.dumps(config.get(section, {}), indent=2))
        else:
            print("Usage: get <org|brand|prefs>")
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: show, complete, reset, is-ready, update-org, update-brand, update-prefs, get")
