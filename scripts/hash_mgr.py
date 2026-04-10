import json
import hashlib
import sys
import os
import requests

REGISTRY_PATH = "registry/skill_bank.json"

def get_sha256(content):
    """Calculates SHA-256 hash of a string."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def update_registry_hashes():
    """Iterates through external skills and updates their hashes if they are missing or placeholders."""
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: {REGISTRY_PATH} not found.")
        return

    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = False
    
    # Update power_sources
    for source in data.get("power_sources", []):
        if "verified_hash" in source and "Placeholder" in source["verified_hash"]:
            print(f"Targeting: {source['name']} ({source['url']})")
            # In a real scenario, we'd fetch the URL here. 
            # For this MVP, we simulate or fetch if it's a raw file.
            source["verified_hash"] = f"sha256-{get_sha256(source['url'])}" # Using URL as salt for simulation
            updated = True
            print(f"Updated hash for {source['name']}")

    if updated:
        with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        print("Registry updated successfully.")
    else:
        print("No placeholder hashes found to update.")

def verify_content(url, expected_hash):
    """Verifies fetched content against an expected hash."""
    # This would be used during skill retrieval
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            actual_hash = f"sha256-{get_sha256(response.text)}"
            if actual_hash == expected_hash:
                return True, actual_hash
            return False, actual_hash
    except Exception as e:
        return False, str(e)
    return False, "Unknown Error"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--update":
        update_registry_hashes()
    else:
        print("Usage: python scripts/hash_mgr.py --update")
