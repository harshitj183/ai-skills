import os
import re
import json
import sys

def get_target_version(root_dir):
    """Fetches the source-of-truth version from the registry."""
    registry_path = os.path.join(root_dir, "registry", "skill_bank.json")
    try:
        with open(registry_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("version", "unknown")
    except Exception:
        return "unknown"

def _audit_file_metadata(file_path, root_dir, version):
    """Performs metadata and signature checks on a single file."""
    rel_path = os.path.relpath(file_path, root_dir)
    errors = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 1. YAML Frontmatter check
            if not content.startswith("---"):
                errors.append(f"Missing YAML frontmatter in {rel_path}")
            
            # 2. Dynamic Signature check
            expected_sig = f"⚡ Smart AI Skills Library | v{version} | Active"
            if expected_sig not in content:
                errors.append(f"Signature mismatch in {rel_path}. Component must have v{version} signature.")

            # 3. Mermaid check for complex folders
            if any(folder in rel_path for folder in ["orchestration", "lifecycle"]):
                if "```mermaid" not in content:
                    errors.append(f"Missing mandatory Mermaid diagram in complex skill: {rel_path}")
    except Exception as e:
        errors.append(f"Could not read {rel_path}: {e}")
        
    return errors

def validate_project():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    version = get_target_version(root_dir)
    errors = []
    
    print(f"[INFO] Validating Smart AI Skills Library v{version}...")

    # 1. Check Root SKILL.md
    skill_md_path = os.path.join(root_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        errors.append("Missing root SKILL.md")
    else:
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if f"v{version}" not in content:
                errors.append(f"SKILL.md version mismatch. Expected v{version}")
            
            # Broken reference check
            refs = re.findall(r'`(roles/[^`]+|skills/[^`]+)`', content)
            for ref in refs:
                if not os.path.exists(os.path.join(root_dir, ref)):
                    errors.append(f"Broken reference in SKILL.md: {ref}")

    # 2. Audit Skills and Roles
    for sub in ["skills", "roles"]:
        dir_path = os.path.join(root_dir, sub)
        if not os.path.exists(dir_path):
            errors.append(f"Missing mandatory directory: {sub}/")
            continue
            
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".md"):
                    errors.extend(_audit_file_metadata(os.path.join(root, file), root_dir, version))

    # 3. Check History (Flexible: CONTEXT.md or ai_activity_log.md)
    history_dir = os.path.join(root_dir, "history")
    history_files = ["CONTEXT.md", "ai_activity_log.md"]
    if not os.path.exists(history_dir) or not any(os.path.exists(os.path.join(history_dir, f)) for f in history_files):
        errors.append("Missing mandatory history log (CONTEXT.md or ai_activity_log.md)")

    if errors:
        print(f"\n[!] Found {len(errors)} validation errors:")
        for e in errors:
            print(f"    - {e}")
        return False
    
    print(f"[PASS] Smart AI Skills Library v{version} validation successful!")
    return True

if __name__ == "__main__":
    if not validate_project():
        sys.exit(1)
