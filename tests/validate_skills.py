import os
import re

def validate_skill(file_path):
    print(f"Validating {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for metadata header
    if not content.startswith('---'):
        return False, "Missing metadata header start (---)"
    
    # Check for name and description
    name_match = re.search(r'name:\s*"(.*?)"', content)
    desc_match = re.search(r'description:\s*"(.*?)"', content)
    
    if not name_match:
        return False, "Missing or malformed 'name' in metadata"
    if not desc_match:
        return False, "Missing or malformed 'description' in metadata"
    
    # Check for signature
    if "⚡ Smart AI Skills Library" not in content:
        return False, "Missing system signature line"
        
    return True, "Valid"

def validate_skill_md_paths():
    print("Validating SKILL.md path references...")
    if not os.path.exists("SKILL.md"):
        return False, "SKILL.md not found"
        
    with open("SKILL.md", 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all path references like 'skills/something.md' or 'roles/something.md'
    # and verify they exist in the repo.
    # The wording "mapped to the smart-instructions/ directory" refers to the fact
    # that locally they exist in skills/ etc, and cli.js maps them later.
    paths = re.findall(r'(skills/[a-zA-Z0-9_/-]+\.md|roles/[a-zA-Z0-9_/-]+\.md)', content)
    
    missing_paths = []
    for path in paths:
        if not os.path.exists(path):
            missing_paths.append(path)
            
    if missing_paths:
        return False, f"Missing referenced files: {', '.join(missing_paths)}"
    return True, "All referenced paths exist"

def main():
    skill_dir = "skills"
    role_dir = "roles"
    errors = []
    
    for root, _, files in os.walk(skill_dir):
        for filename in files:
            if filename.endswith(".md"):
                path = os.path.join(root, filename)
                valid, msg = validate_skill(path)
                if not valid:
                    errors.append(f"{path}: {msg}")
    
    for filename in os.listdir(role_dir) if os.path.exists(role_dir) else []:
        if filename.endswith(".md"):
            path = os.path.join(role_dir, filename)
            valid, msg = validate_skill(path)
            if not valid:
                errors.append(f"{path}: {msg}")
                
    valid_paths, msg_paths = validate_skill_md_paths()
    if not valid_paths:
        errors.append(f"SKILL.md: {msg_paths}")
                    
    if errors:
        print("\n--- Validation Errors ---")
        for err in errors:
            print(err)
        exit(1)
    else:
        print("\n--- All skills, roles, and SKILL.md paths are valid! ---")

if __name__ == "__main__":
    main()
