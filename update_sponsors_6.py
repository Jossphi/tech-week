import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

target1 = """<img src="https://i.postimg.cc/pVgQ2wBy/INTIPALKA-2022-12-12-Logo-Pisco-jpg.jpg" alt="Sponsor 5" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));">"""
replacement1 = """<img src="https://i.postimg.cc/pVgQ2wBy/INTIPALKA-2022-12-12-Logo-Pisco-jpg.jpg" alt="Sponsor 5" style="max-width: 110%; max-height: 135px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1)); transform: scale(1.15);">"""

target2 = """<img src="https://i.postimg.cc/R0VKs4M4/Logo-Prestamype.png" alt="Sponsor 6" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));">"""
replacement2 = """<img src="https://i.postimg.cc/4y5XSk4d/Logo-Prestamype-1.png" alt="Sponsor 6" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));">"""

updated = False

if target1 in template_str:
    template_str = template_str.replace(target1, replacement1)
    updated = True

if target2 in template_str:
    template_str = template_str.replace(target2, replacement2)
    updated = True

if updated:
    new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
    new_final_content = content[:content_start] + new_template_json + content[close_pos:]
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(new_final_content)
    print("Sponsors updated in index.html successfully!")
else:
    print("Could not find targets in index.html.")
