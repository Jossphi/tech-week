import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

# 1
old1 = '<a href="#organiza" onClick="{{ toggleMenu }}"'
new1 = '<a href="https://airtable.com/appnnVuEijSgpZFHR/shrRXl6s1L2GJaFLd" target="_blank" onClick="{{ toggleMenu }}"'
template_str = template_str.replace(old1, new1)

# 2
old2 = '<a href="#organiza" style="flex: 1; min-width: 176px; max-width: 231px;'
new2 = '<a href="https://airtable.com/appnnVuEijSgpZFHR/shrRXl6s1L2GJaFLd" target="_blank" style="flex: 1; min-width: 176px; max-width: 231px;'
template_str = template_str.replace(old2, new2)

# 3
old3 = '<a href="https://techweek.pe/#organiza:~:text=importante%20del%20sector.-,Postula%20tu%20evento%20%E2%86%92,-PARTNERS%20ESTRAT%C3%89GICOS"'
new3 = '<a href="https://airtable.com/appnnVuEijSgpZFHR/shrRXl6s1L2GJaFLd"'
template_str = template_str.replace(old3, new3)

# 4
old4 = '<a href="#organiza" style="color: #b9b9b9; text-decoration: none;'
new4 = '<a href="https://airtable.com/appnnVuEijSgpZFHR/shrRXl6s1L2GJaFLd" target="_blank" style="color: #b9b9b9; text-decoration: none;'
template_str = template_str.replace(old4, new4)

new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
new_content = content[:content_start] + new_template_json + content[close_pos:]

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Links replaced!")
