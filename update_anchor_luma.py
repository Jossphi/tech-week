import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

old_link = 'https://lu.ma/perutechweek'
new_link = 'https://luma.com/Perutechweek2026'

if old_link in template_str:
    template_str = template_str.replace(old_link, new_link)
    new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
    new_final_content = content[:content_start] + new_template_json + content[close_pos:]
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(new_final_content)
    print("Links updated in index.html successfully!")
else:
    print("Old link not found in index.html.")
