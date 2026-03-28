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

def main():
    skill_dir = "skills"
    role_dir = "roles"
    errors = []
    
    for d in [skill_dir, role_dir]:
        if not os.path.exists(d): continue
        for filename in os.listdir(d):
            if filename.endswith(".md"):
                path = os.path.join(d, filename)
                valid, msg = validate_skill(path)
                if not valid:
                    errors.append(f"{path}: {msg}")
                    
    if errors:
        print("\n--- Validation Errors ---")
        for err in errors:
            print(err)
        exit(1)
    else:
        print("\n--- All skills and roles are valid! ---")

if __name__ == "__main__":
    main()
