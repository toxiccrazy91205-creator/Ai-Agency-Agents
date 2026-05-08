import os
import re
from django.conf import settings

def parse_agent_file(file_path):
    """
    Parses an agent markdown file to extract metadata and prompt content.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML-like metadata
        meta_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        metadata = {}
        if meta_match:
            meta_text = meta_match.group(1)
            for line in meta_text.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    metadata[key.strip()] = val.strip()
        
        # The prompt is the rest of the file
        prompt_content = content
        if meta_match:
            prompt_content = content[meta_match.end():].strip()
            
        return {
            'name': metadata.get('name', 'Unknown Agent'),
            'description': metadata.get('description', 'No description available.'),
            'color': metadata.get('color', 'blue'),
            'prompt': prompt_content,
            'id': os.path.basename(file_path).replace('.md', '')
        }
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

def get_all_agents():
    """
    Scans the repository for agent definitions organized by category.
    """
    categories = [
        'engineering', 'design', 'marketing', 'product', 
        'strategy', 'support', 'testing', 'specialized', 
        'spatial-computing', 'project-management'
    ]
    
    repo_root = settings.BASE_DIR / 'ai-agency-agents'
    agents_by_category = {}
    
    for category in categories:
        cat_path = repo_root / category
        if cat_path.exists() and cat_path.is_dir():
            agents_by_category[category] = []
            for file in os.listdir(cat_path):
                if file.endswith('.md') and '-' in file:
                    agent = parse_agent_file(cat_path / file)
                    if agent:
                        agent['category'] = category
                        agents_by_category[category].append(agent)
    
    return agents_by_category

def get_agent_by_id(category, agent_id):
    """
    Retrieves a specific agent by category and ID.
    """
    repo_root = settings.BASE_DIR / 'ai-agency-agents'
    file_path = repo_root / category / f"{agent_id}.md"
    if file_path.exists():
        agent = parse_agent_file(file_path)
        if agent:
            agent['category'] = category
            return agent
    return None
