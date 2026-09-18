import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

target = """      <!-- Sponsor 2 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/9MbkYhLB/GROWYARD-LOGOTIPO-BLANCO-1.png" alt="Sponsor Growyard" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>"""

new_sponsors = """      <!-- Sponsor 2 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/9MbkYhLB/GROWYARD-LOGOTIPO-BLANCO-1.png" alt="Sponsor Growyard" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>

      <!-- Sponsor 3 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/L4tpyZdM/Blanco.png" alt="Sponsor 3" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>

      <!-- Sponsor 4 -->
      <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 60px 40px; display: flex; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 10px 40px rgba(0,0,0,0.2); min-height: 220px;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.5); box-shadow: 0 20px 50px rgba(221,28,41,0.15);">
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;"><img src="https://i.postimg.cc/mZYsdFx4/Eventplus-Logo-2-(2).png" alt="Sponsor 4" style="max-width: 100%; max-height: 120px; object-fit: contain; filter: drop-shadow(0 0 10px rgba(255,255,255,0.1));"></div>
      </div>"""

if target in template_str:
    template_str = template_str.replace(target, new_sponsors)
    new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
    new_content = content[:content_start] + new_template_json + content[close_pos:]
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Sponsors added to index.html successfully!")
else:
    print("Target not found in template. Cannot replace.")
