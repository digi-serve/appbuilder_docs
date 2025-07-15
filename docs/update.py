import os
import re

# Recursively find all markdown files in the directory and subdirectories
def find_md_files(root):
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.endswith('.md'):
                md_files.append(os.path.join(dirpath, f))
    return md_files

# Find the closest parent directory with an index.md or similarly named file with a title
# Returns the title value if found, else None
def find_parent_title(md_file):
    dirpath = os.path.dirname(md_file)
    while True:
        # Look for index.md or a .md file matching the directory name
        candidates = [
            os.path.join(dirpath, 'index.md'),
            os.path.join(dirpath, os.path.basename(dirpath) + '.md')
        ]
        for candidate in candidates:
            if os.path.isfile(candidate):
                with open(candidate, 'r', encoding='utf-8') as f:
                    content = f.read()
                    m = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
                    if m:
                        return m.group(1).strip()
        # Go up one directory
        parent = os.path.dirname(dirpath)
        if parent == dirpath:
            break
        dirpath = parent
    return None

# Add parent field if missing
def add_parent_field(md_file, parent_title):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Find front matter
    if not lines or not lines[0].strip().startswith('---'):
        return
    # Check if parent already exists
    for line in lines:
        if line.strip().startswith('parent:'):
            return
    # Insert parent after ---
    for i in range(1, len(lines)):
        if lines[i].strip() and not lines[i].strip().startswith('#'):
            lines.insert(i, f'parent: {parent_title}\n')
            break
    else:
        lines.append(f'parent: {parent_title}\n')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def main():
    root = os.path.dirname(__file__)
    md_files = find_md_files(root)
    for md_file in md_files:
        parent_title = find_parent_title(md_file)
        if parent_title:
            add_parent_field(md_file, parent_title)

if __name__ == '__main__':
    main()
