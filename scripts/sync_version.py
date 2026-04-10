import os
import re
import sys
import json

def sync_version(new_version):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # 1. Update package.json
    pkg_path = os.path.join(root_dir, "package.json")
    with open(pkg_path, 'r', encoding='utf-8') as f:
        pkg_data = json.load(f)
    old_version = pkg_data['version']
    pkg_data['version'] = new_version
    with open(pkg_path, 'w', encoding='utf-8') as f:
        json.dump(pkg_data, f, indent=2)
    print(f"[FIX] Updated package.json: {old_version} -> {new_version}")

    # 2. Update registry/skill_bank.json
    registry_path = os.path.join(root_dir, "registry", "skill_bank.json")
    with open(registry_path, 'r', encoding='utf-8') as f:
        registry_data = json.load(f)
    registry_data['version'] = new_version
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry_data, f, indent=2)
    print(f"[FIX] Updated skill_bank.json to v{new_version}")

    # 3. Bulk Update Markdown files and Python scripts
    # We look for "vOLD_VERSION" and replace with "vNEW_VERSION"
    # We also look for specific signature strings
    
    files_to_check = []
    for root, _, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root or "dashboard/dist" in root:
            continue
        for file in files:
            if file.endswith((".md", ".py", ".js", ".tsx", ".ts")):
                files_to_check.append(os.path.join(root, file))

    updated_count = 0
    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace(f"v{old_version}", f"v{new_version}")
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_count += 1
        except Exception as e:
            print(f"[WARN] Could not update {file_path}: {e}")

    print(f"[SUCCESS] Synced version v{new_version} across {updated_count} files.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_version.py <new_version>")
        sys.exit(1)
    sync_version(sys.argv[1])
