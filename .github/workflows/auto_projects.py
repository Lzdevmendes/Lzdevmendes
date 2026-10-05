import os
import urllib.request
import json
import re

def get_recent_repos(token):
    url = "https://api.github.com/user/repos?sort=pushed&direction=desc&per_page=15"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    
    try:
        with urllib.request.urlopen(req) as response:
            repos = json.loads(response.read().decode())
    except Exception as e:
        print(f"Error calling GitHub API: {e}")
        return []
        
    recent = []
    for r in repos:
        # Ignore profile repo and forks
        if r['name'].lower() != 'lzdevmendes' and not r['fork']:
            recent.append(r)
        if len(recent) == 3:
            break
    return recent

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("No GITHUB_TOKEN found.")
        return

    repos = get_recent_repos(token)
    if len(repos) < 3:
        print("Not enough repos found.")
        return

    # Create the new projects yaml block
    projects_yaml = "projects:\n"
    for i, r in enumerate(repos):
        desc = r.get('description') or "Repositório atualizado recentemente."
        # escape quotes
        desc = desc.replace('"', "'")
        if len(desc) > 50:
            desc = desc[:47] + "..."
            
        projects_yaml += f"  - repo: \"{r['full_name']}\"\n"
        projects_yaml += f"    arm: {i % 3}\n"
        projects_yaml += f"    description: \"{desc}\"\n"

    # Read config.yml
    with open('config.yml', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the projects block
    # It starts with "projects:" and ends before "theme:" or end of file
    new_content = re.sub(r'projects:\n(?:[ \t]+-[^\n]+\n(?:[ \t]+[^\n]+\n)*)*', projects_yaml + '\n', content)

    # Write config.yml
    with open('config.yml', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated config.yml with: {[r['full_name'] for r in repos]}")

if __name__ == "__main__":
    main()
