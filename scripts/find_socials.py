import json, re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

col4_start = template.find('<!-- Column 4 -->')
# Print a larger chunk to see what's around col4
print(template[col4_start:col4_start+3000])
