import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

target = """    </div>

    <!-- 2 Sponsors Container -->"""

new_content_to_insert = """    </div>

    <!-- Main Sponsor -->
    <div style="max-width: 900px; margin: 0 auto 32px;">
      <div style="background: rgba(221,28,41,0.05); border: 1px solid rgba(221,28,41,0.3); border-radius: 24px; padding: 70px 40px; display: flex; flex-direction: column; align-items: center; justify-content: center; backdrop-filter: blur(20px); transition: all 0.3s ease; box-shadow: 0 15px 50px rgba(221,28,41,0.15); min-height: 280px; position: relative;" style-hover="transform: translateY(-5px); border-color: rgba(221,28,41,0.8); box-shadow: 0 25px 60px rgba(221,28,41,0.3);">
        <div style="position: absolute; top: -15px; background: linear-gradient(90deg, #FF3344, #FF6C76); color: #fff; font-family: 'Codec Pro', sans-serif; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; padding: 8px 20px; border-radius: 999px; box-shadow: 0 4px 15px rgba(221,28,41,0.4);">Main Partner</div>
        <div style="font-family: 'Codec Pro', sans-serif; font-size: 28px; font-weight: 700; color: #b9b9b9; text-transform: uppercase; letter-spacing: 2px;">
          <img src="https://i.postimg.cc/rwkC1s6c/logo-texto-blanco.png" alt="Main Sponsor" style="max-width: 100%; max-height: 160px; object-fit: contain; filter: drop-shadow(0 0 15px rgba(255,255,255,0.15));">
        </div>
      </div>
    </div>

    <!-- Sponsors Grid Container -->"""

if target in template_str:
    template_str = template_str.replace(target, new_content_to_insert)
    new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
    new_final_content = content[:content_start] + new_template_json + content[close_pos:]
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(new_final_content)
    print("Main sponsor added to index.html successfully!")
else:
    print("Target not found in template. Cannot replace.")
