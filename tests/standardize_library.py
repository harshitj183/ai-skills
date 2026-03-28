import os
import re

signature = "\n---\n⚡ Smart AI Skills Library | v2.2.6 | Active\n"

def standardize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    content = "".join(lines)
    
    # 1. Ensure signature exists (at the end)
    if "⚡ Smart AI Skills Library" not in content:
        content = content.rstrip() + signature
    
    # 2. Ensure YAML header exists
    if not content.startswith('---'):
        # Extract title from # header or filename
        title = ""
        for line in lines:
            if line.startswith('# '):
                title = line.replace('# ', '').strip()
                break
        
        if not title:
            title = os.path.basename(file_path).replace('.md', '').replace('_', ' ').title()
        
        # Try to extract a description from the first paragraph
        desc = f"Modular skill/role for {title}."
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith('#'):
                desc = line.strip()[:100] # Use first 100 chars
                break
        
        # Add header
        header = f"---\nname: \"{title}\"\ndescription: \"{desc}\"\n---\n\n"
        content = header + content
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Standardized {file_path}")

def main():
    for d in ["skills", "roles"]:
        if os.path.exists(d):
            for filename in os.listdir(d):
                if filename.endswith(".md"):
                    standardize_file(os.path.join(d, filename))

if __name__ == "__main__":
    main()
