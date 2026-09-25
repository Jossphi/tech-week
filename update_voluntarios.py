import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

old_content = '<a href="https://airtable.com/appnnVuEijSgpZFHR/shrqouASmqggq7oEr" style="flex: 1; min-width: 176px; max-width: 231px; justify-content: center; text-align: center; white-space: normal; line-height: 1.1; background: rgba(0,0,0,0.4); border: 1px solid #fff; color: #fff; text-decoration: none; font-family: \'Codec Pro\', sans-serif; font-weight: 600; font-size: 18px; padding: 13px 18px; border-radius: 999px; transition: background .2s; display: inline-flex; align-items: center; gap: 6px;" style-hover="background: rgba(255,255,255,0.1);">Ser voluntario <span>&#8594;</span></a>'
new_content = '<a href="https://luma.com/Perutechweek2026" target="_blank" rel="noopener" style="flex: 1; min-width: 176px; max-width: 231px; justify-content: center; text-align: center; white-space: normal; line-height: 1.1; background: rgba(0,0,0,0.4); border: 1px solid #fff; color: #fff; text-decoration: none; font-family: \'Codec Pro\', sans-serif; font-weight: 600; font-size: 18px; padding: 13px 18px; border-radius: 999px; transition: background .2s; display: inline-flex; align-items: center; gap: 6px;" style-hover="background: rgba(255,255,255,0.1);">Ver Eventos <span>&#8594;</span></a>'

if old_content in template_str:
    template_str = template_str.replace(old_content, new_content)
    new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
    new_final_content = content[:content_start] + new_template_json + content[close_pos:]
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(new_final_content)
    print("Button updated in index.html successfully!")
else:
    print("Old button not found in index.html.")
