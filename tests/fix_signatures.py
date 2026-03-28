import os

signature = "\n---\n⚡ Smart AI Skills Library | v2.2.6 | Active\n"

def add_signature(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "⚡ Smart AI Skills Library" not in content:
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(signature)
        print(f"Updated {file_path}")

def main():
    for d in ["skills", "roles"]:
        if os.path.exists(d):
            for filename in os.listdir(d):
                if filename.endswith(".md"):
                    add_signature(os.path.join(d, filename))

if __name__ == "__main__":
    main()
