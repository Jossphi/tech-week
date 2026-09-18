import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

target = "<!-- ============ 7. AGENDA COMPLETA / SIDE EVENTS ============ -->\n\n\n<!-- ============ 8. CÓMO FUNCIONA ============ -->"
target_alt = "<!-- ============ 7. AGENDA COMPLETA / SIDE EVENTS ============ -->\r\n\r\n\r\n<!-- ============ 8. CÓMO FUNCIONA ============ -->"

new_content = """<!-- ============ 7. AGENDA COMPLETA / SIDE EVENTS ============ -->
<section id="agenda-luma" style="background: #080808; padding: clamp(60px, 8vw, 100px) clamp(16px, 4vw, 48px); border-top: 1px solid #1c1c1c; position: relative;">
  <div style="max-width: 1200px; margin: 0 auto;">
    
    <!-- Header -->
    <div style="text-align: center; margin-bottom: 40px;">
      <div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid #2a2a2a; border-radius: 999px; padding: 7px 16px; background: rgba(22,20,20,0.8); margin-bottom: 24px;">
        <span style="width: 8px; height: 8px; background: #DD1C29; border-radius: 50%; flex-shrink: 0; box-shadow: 0 0 10px #DD1C29;"></span>
        <span style="font-family: 'Codec Pro', sans-serif; font-size: 18px; color: #E4E4E4; text-transform: uppercase; letter-spacing: 2px;">Agenda Oficial</span>
      </div>
      <h2 style="margin: 0; font-family: 'Codec Pro', sans-serif; font-weight: 700; font-size: clamp(32px, 4vw, 48px); color: #fff; line-height: 1.1;">Todos los eventos de la <span style="background: linear-gradient(90deg, #FF3344, #FF6C76); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">PTW</span></h2>
    </div>

    <!-- Embed Container -->
    <div style="background: #111; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5);">
      <iframe
        src="https://luma.com/embed/calendar/cal-wK0lkbFo07BExHZ/events"
        width="100%"
        height="700"
        frameborder="0"
        style="border: none; border-radius: 8px; display: block;"
        allowfullscreen=""
        aria-hidden="false"
        tabindex="0"
      ></iframe>
    </div>

  </div>
</section>

<!-- ============ 8. CÓMO FUNCIONA ============ -->"""

if target in template_str:
    template_str = template_str.replace(target, new_content)
elif target_alt in template_str:
    template_str = template_str.replace(target_alt, new_content)
else:
    # Try a regex or just find the prefix
    idx = template_str.find("<!-- ============ 7. AGENDA COMPLETA / SIDE EVENTS ============ -->")
    idx2 = template_str.find("<!-- ============ 8. CÓMO FUNCIONA ============ -->", idx)
    if idx != -1 and idx2 != -1:
        template_str = template_str[:idx] + new_content + template_str[idx2 + len("<!-- ============ 8. CÓMO FUNCIONA ============ -->"):]
    else:
        print("Could not find targets to replace.")
        exit(1)

new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
new_final_content = content[:content_start] + new_template_json + content[close_pos:]
with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(new_final_content)
print("Luma added to index.html successfully!")
