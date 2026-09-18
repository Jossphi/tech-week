import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)

template_str = json.loads(content[content_start:close_pos].strip())

target = """<section id="agenda-luma" style="background: #080808; padding: clamp(60px, 8vw, 100px) clamp(16px, 4vw, 48px); border-top: 1px solid #1c1c1c; position: relative;">
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
</section>"""

new_content = """<section id="agenda-luma" style="background: #080808; padding: clamp(60px, 8vw, 100px) clamp(16px, 4vw, 48px); border-top: 1px solid #1c1c1c; position: relative; overflow: hidden;">
  <!-- background glow -->
  <div style="position: absolute; top: 50%; left: 0; transform: translateY(-50%); width: 40%; height: 500px; background: radial-gradient(circle, rgba(221,28,41,0.15) 0%, rgba(8,8,8,0) 70%); filter: blur(60px); pointer-events: none;"></div>

  <div style="max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 450px), 1fr)); gap: clamp(40px, 6vw, 80px); align-items: center; position: relative; z-index: 2;">
    
    <!-- Left Column: Info -->
    <div style="display: flex; flex-direction: column; align-items: flex-start; text-align: left;">
      <div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid #2a2a2a; border-radius: 999px; padding: 7px 16px; background: rgba(22,20,20,0.8); margin-bottom: 24px;">
        <span style="width: 8px; height: 8px; background: #DD1C29; border-radius: 50%; flex-shrink: 0; box-shadow: 0 0 10px #DD1C29;"></span>
        <span style="font-family: 'Codec Pro', sans-serif; font-size: 16px; font-weight: 600; color: #E4E4E4; text-transform: uppercase; letter-spacing: 2px;">Agenda Oficial</span>
      </div>
      <h2 style="margin: 0 0 24px; font-family: 'Codec Pro', sans-serif; font-weight: 700; font-size: clamp(40px, 5vw, 64px); color: #fff; line-height: 1.05;">
        Conoce todos los eventos de <br><span style="background: linear-gradient(90deg, #FF3344, #FF6C76); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">PTW 2026</span>
      </h2>
      <p style="margin: 0 0 32px; font-size: clamp(20px, 2vw, 22px); line-height: 1.6; color: #b9b9b9; max-width: 500px;">
        Descubre conferencias, hackathons, meetups y experiencias inmersivas organizadas por la comunidad. Regístrate en los eventos que más te interesen y asegura tu lugar.
      </p>
      
      <div style="display: flex; gap: 16px; flex-wrap: wrap;">
        <a href="#organiza" style="display: inline-block; background: #DD1C29; color: #fff; text-decoration: none; font-weight: 700; font-size: 18px; padding: 14px 28px; border-radius: 12px; transition: background .2s;" style-hover="background: #FF6C76;">Organiza tu evento</a>
      </div>
    </div>

    <!-- Right Column: Luma Embed -->
    <div style="background: #111; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.5); width: 100%;">
      <iframe
        src="https://luma.com/embed/calendar/cal-wK0lkbFo07BExHZ/events"
        width="100%"
        height="650"
        frameborder="0"
        style="border: none; border-radius: 8px; display: block;"
        allowfullscreen=""
        aria-hidden="false"
        tabindex="0"
      ></iframe>
    </div>

  </div>
</section>"""

if target in template_str:
    template_str = template_str.replace(target, new_content)
    new_template_json = json.dumps(template_str, ensure_ascii=True).replace('</', r'<\/')
    new_final_content = content[:content_start] + new_template_json + content[close_pos:]
    with open('src/index.html', 'w', encoding='utf-8') as f:
        f.write(new_final_content)
    print("Luma 2-column added to index.html successfully!")
else:
    print("Target not found in template. Cannot replace.")
