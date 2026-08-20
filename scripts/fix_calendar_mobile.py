import json, re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

# ────────────────────────────────────────────────────────────
# 1. Find the scroll container that wraps the 7-column grid
#    and give it a class so CSS can hide it on mobile
# ────────────────────────────────────────────────────────────
old_scroll_wrap = '<div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">\n      <div style="min-width: 900px;">'
new_scroll_wrap = '<div class="cal-desktop" style="overflow-x: auto; -webkit-overflow-scrolling: touch;">\n      <div style="min-width: 900px;">'

if old_scroll_wrap in template:
    template = template.replace(old_scroll_wrap, new_scroll_wrap)
    print("Scroll wrap class added!")
else:
    # Try alternate spacing
    idx = template.find('overflow-x: auto; -webkit-overflow-scrolling: touch;')
    print("Found overflow at:", idx)
    print(repr(template[idx-5:idx+120]))

# ────────────────────────────────────────────────────────────
# 2. Find where the desktop calendar ends (closing </div></div>
#    after the 7-col grid) and inject mobile calendar right after
# ────────────────────────────────────────────────────────────
# The desktop block ends with two closing </div> tags for the scroll wrap
# Find where to insert mobile view — right after closing </div></div> of cal-desktop
# Look for the pattern after the last day column events
closing_pattern = '</div>\n      </div>\n    </div>'  # closes min-width, overflow, then outer
# Actually let's find it via the section end
idx_close = template.find('</div>\n      </div>\n    </div>', template.find('cal-desktop'))
print("Desktop close pattern at:", idx_close)
if idx_close != -1:
    close_end = idx_close + len('</div>\n      </div>\n    </div>')
else:
    # fallback: find next section after calendar
    idx_next_section = template.find('<!-- ============ 8.', template.find('cal-desktop'))
    if idx_next_section == -1:
        idx_next_section = template.find('<!-- ============ 9.', template.find('cal-desktop'))
    close_end = idx_next_section
    print("Using next section at:", close_end)

# ────────────────────────────────────────────────────────────
# 3. Build the mobile calendar — a simple vertical card list
#    for each of the 7 days
# ────────────────────────────────────────────────────────────
days_mobile = [
    ('Lun', '12', 'Lunes 12 oct'),
    ('Mar', '13', 'Martes 13 oct'),
    ('Mié', '14', 'Miércoles 14 oct'),
    ('Jue', '15', 'Jueves 15 oct'),
    ('Vie', '16', 'Viernes 16 oct'),
    ('Sáb', '17', 'Sábado 17 oct'),
    ('Dom', '18', 'Domingo 18 oct'),
]

day_cards = []
for i, (abbr, num, full) in enumerate(days_mobile):
    active = 'border-color: #DD1C29; background: rgba(221,28,41,.06);' if i == 0 else 'border-color: #2a2a2a; background: #0f0d0d;'
    label_color = '#DD1C29' if i == 0 else '#6a6a6a'
    card = f'''<div style="border: 1px solid; {active} border-radius: 12px; padding: 16px 18px; display: flex; align-items: center; gap: 16px;">
          <div style="text-align: center; min-width: 48px;">
            <div style="font-family: 'Codec Pro', sans-serif; font-size: 13px; font-weight: 600; color: {label_color}; text-transform: uppercase; letter-spacing: 1px;">{abbr}</div>
            <div style="font-family: 'Codec Pro', sans-serif; font-size: 32px; font-weight: 700; color: #fff; line-height: 1;">{num}</div>
          </div>
          <div style="flex: 1; border-left: 1px solid #2a2a2a; padding-left: 16px;">
            <div style="font-family: 'Codec Pro', sans-serif; font-size: 15px; font-weight: 600; color: #E4E4E4;">{full}</div>
            <div style="font-family: 'Codec Pro', sans-serif; font-size: 13px; color: #6a6a6a; margin-top: 4px;">Agenda por confirmar · 27 ago 2026</div>
          </div>
        </div>'''
    day_cards.append(card)

mobile_cal = '\n\n    <!-- Mobile Calendar (solo visible en mobile) -->\n    <div class="cal-mobile" style="display: none;">\n      <div style="display: flex; flex-direction: column; gap: 10px;">\n        ' + '\n        '.join(day_cards) + '\n      </div>\n    </div>'

# Insert the mobile calendar after the closing of the desktop one
if idx_close != -1:
    template = template[:close_end] + mobile_cal + template[close_end:]
    print("Mobile calendar inserted!")

# ────────────────────────────────────────────────────────────
# 4. Add CSS to show/hide cal-desktop vs cal-mobile
# ────────────────────────────────────────────────────────────
calendar_css = """
/* Calendar responsive */
.cal-mobile { display: none; }
.cal-desktop { display: block; }
@media (max-width: 700px) {
  .cal-desktop { display: none !important; }
  .cal-mobile { display: block !important; }
}
"""
template = template.replace('  </style>', calendar_css + '  </style>')

print("CSS added:", '.cal-mobile' in template)

new_template_json = json.dumps(template, ensure_ascii=True).replace('</', r'<\/')
new_content = content[:content_start] + new_template_json + content[close_pos:]

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Validate JSON
with open('src/index.html', 'r', encoding='utf-8') as f:
    c2 = f.read()
s2 = c2.find(OPEN) + len(OPEN)
e2 = c2.find(CLOSE, s2)
t2 = json.loads(c2[s2:e2].strip())
print("JSON valid:", len(t2) > 0)
print("cal-desktop in template:", 'cal-desktop' in t2)
print("cal-mobile in template:", 'cal-mobile' in t2)
print("Done!")
