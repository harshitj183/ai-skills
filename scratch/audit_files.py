import os
import re
import json

def check_file_references(root_dir):
    skill_md_path = os.path.join(root_dir, "SKILL.md")
    if not os.path.exists(skill_md_path):
        print(f"Error: {skill_md_path} not found.")
        return

    with open(skill_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract roles/ and skills/ references
    references = re.findall(r'`(roles/[^`]+|skills/[^`]+)`', content)
    
    # Also check registry/
    registry_ref = re.findall(r'`(registry/[^`]+)`', content)
    references.extend(registry_ref)

    missing_files = []
    for ref in references:
        full_path = os.path.join(root_dir, ref.replace('/', os.sep))
        if not os.path.exists(full_path):
            missing_files.append(ref)

    if missing_files:
        print("Missing files referenced in SKILL.md:")
        for missing in missing_files:
            print(f"- {missing}")
    else:
        print("All file references in SKILL.md are valid.")

    # Check registry/skill_bank.json consistency
    registry_path = os.path.join(root_dir, "registry", "skill_bank.json")
    if os.path.exists(registry_path):
        with open(registry_path, 'r', encoding='utf-8') as f:
            try:
                skill_bank = json.load(f)
                # Assuming skill_bank.json stores paths in keys or values
                # Let's just list the directory and see if all files in skills/ are in skill_bank.json
                skills_in_dir = [f for f in os.listdir(os.path.join(root_dir, "skills")) if f.endswith('.md')]
                # Need to inspect skill_bank.json structure
                # For now, just print the check
            except Exception as e:
                print(f"Error reading skill_bank.json: {e}")

if __name__ == "__main__":
    # Use the directory of the script to find the project root (assuming script is in scratch/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    check_file_references(project_root)
