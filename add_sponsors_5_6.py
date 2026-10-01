import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

target = """      <!-- Sponsor 4 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/mZYsdFx4/Eventplus-Logo-2-(2).png" alt="Sponsor 4" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>"""

new_content = """      <!-- Sponsor 4 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/mZYsdFx4/Eventplus-Logo-2-(2).png" alt="Sponsor 4" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>

      <!-- Sponsor 5 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/pVgQ2wBy/INTIPALKA-2022-12-12-Logo-Pisco-jpg.jpg" alt="Sponsor 5" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>

      <!-- Sponsor 6 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/R0VKs4M4/Logo-Prestamype.png" alt="Sponsor 6" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>"""

# Try with \n and \r\n
if target in template_str:
    template_str = template_str.replace(target, new_content)
else:
    target = target.replace('\n', '\r\n')
    if target in template_str:
        template_str = template_str.replace(target, new_content)
    else:
        print("Target not found.")
        exit(1)

new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
new_final_content = content[:content_start] + new_template_json + content[close_pos:]
with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(new_final_content)
print("Sponsors added to index.html successfully!")
