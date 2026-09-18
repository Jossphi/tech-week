import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

# The content is a JSON encoded string containing the HTML
template_str = json.loads(content[content_start:close_pos].strip())

with open('dump.html', 'w', encoding='utf-8') as f:
    f.write(template_str)
