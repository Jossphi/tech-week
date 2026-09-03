import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

# ─────────────────────────────────────────────────────────────
# 1. Update the events array in renderVals()
# ─────────────────────────────────────────────────────────────
old_events = """    const events = [
      { day: 'Lun 12', when: 'LUN 12 · 9:00 AM', cat: 'AI', title: 'Meetup de IA aplicada (ejemplo)', org: 'Organizador por confirmar' },
      { day: 'Mar 13', when: 'MAR 13 · 6:30 PM', cat: 'Fintech', title: 'Fintech Night (ejemplo)', org: 'Organizador por confirmar' },
      { day: 'Mié 14', when: 'MIÉ 14 · 8:30 AM', cat: 'VC', title: 'Desayuno con inversionistas (ejemplo)', org: 'Organizador por confirmar' },
      { day: 'Jue 15', when: 'JUE 15 · 7:00 PM', cat: 'Web3', title: 'Builders de Web3 (ejemplo)', org: 'Organizador por confirmar' },
      { day: 'Vie 16', when: 'VIE 16 · 10:00 AM', cat: 'Corporate', title: 'Innovación corporativa (ejemplo)', org: 'Organizador por confirmar' },
      { day: 'Sáb 17', when: 'SÁB 17 · 11:00 AM', cat: 'Social', title: 'Tech por el impacto social (ejemplo)', org: 'Organizador por confirmar' }
    ];"""

new_events = """    const events = [
      { day: 'Lun 12', when: 'LUN 12 · 18:00', cat: 'Social', title: 'Bienvenida Peru Tech Week 2026', org: 'PTW', time: '18:00 - 22:00' },
      { day: 'Mié 14', when: 'MIÉ 14 · 09:00', cat: 'Corporate', title: 'Experiencia Endeavor', org: 'ENDEAVOR', time: '09:00 - 17:00' },
      { day: 'Mié 14', when: 'MIÉ 14 · 10:00', cat: 'Corporate', title: 'Peru Business Fest', org: 'COFIDE', time: '10:00 - 19:30' },
      { day: 'Jue 15', when: 'JUE 15 · 09:00', cat: 'VC', title: 'Peru Venture Capital Conference 2026', org: 'PECAP', time: '09:00 - 19:00' },
      { day: 'Jue 15', when: 'JUE 15 · 10:00', cat: 'Corporate', title: 'Peru Business Fest', org: 'COFIDE', time: '10:00 - 19:30' },
      { day: 'Vie 16', when: 'VIE 16 · 09:00', cat: 'AI', title: 'Techsuyo', org: 'PERU SV', time: '09:00 - 18:00' },
      { day: 'Vie 16', when: 'VIE 16 · 10:00', cat: 'Corporate', title: 'Peru Business Fest', org: 'COFIDE', time: '10:00 - 19:30' },
      { day: 'Vie 16', when: 'VIE 16 · 18:00', cat: 'Social', title: 'Cóctel de cierre Peru Tech Week 2026', org: 'PTW', time: '18:00 - 22:00' },
      { day: 'Sáb 17', when: 'SÁB 17 · 10:00', cat: 'Corporate', title: 'Peru Business Fest', org: 'COFIDE', time: '10:00 - 19:30' }
    ];"""

if old_events in template:
    template = template.replace(old_events, new_events)
    print("Events array updated!")
else:
    print("Events array not found – manual search needed")

# ─────────────────────────────────────────────────────────────
# Helper: build an event card for the desktop grid
# ─────────────────────────────────────────────────────────────
def event_card(time, title, org, highlight=False, link=True, custom_url=None):
    bg = 'background: rgba(221,28,41,.07); border: 1px solid rgba(221,28,41,.3);' if highlight else 'background: #0f0d0d; border: 1px solid #2a2a2a;'
    org_color = '#DD1C29' if highlight else '#6a6a6a'
    url = custom_url if custom_url else 'https://lu.ma/perutechweek'
    reg = f'<div style="border-top: 1px solid #2a2a2a; padding-top: 10px; margin-top: 10px;"><a href="{url}" target="_blank" rel="noopener" style="color: #DD1C29; text-decoration: underline; text-underline-offset: 3px; font-size: 18px; font-weight: 600;" style-hover="color: #FF6C76;">Regístrate →</a></div>' if link else ''
    return f'''<div style="{bg} border-radius: 10px; padding: 14px 14px 12px; margin-bottom: 6px;">
                  <div style="font-family: 'Codec Pro', sans-serif; font-size: 16px; color: #7a7a7a; margin-bottom: 6px;">{time}</div>
                  <div style="font-family: 'Codec Pro', sans-serif; font-weight: 700; font-size: 19px; color: #fff; line-height: 1.25; margin-bottom: 4px;">{title}</div>
                  <div style="font-family: 'Codec Pro', sans-serif; font-size: 15px; color: {org_color}; font-weight: 600;">{org}</div>
                  {reg}
                </div>'''

def empty_cell():
    return '<div style="padding: 10px 8px; color: #3a3a3a; font-size: 15px; font-style: italic; font-family: \'Codec Pro\', sans-serif;">—</div>'

# ─────────────────────────────────────────────────────────────
# 2. Build new desktop calendar content (7 day columns)
# ─────────────────────────────────────────────────────────────
# Events by day: Lun=col1, Mar=col2, Mié=col3, Jue=col4, Vie=col5, Sáb=col6, Dom=col7
day_cells = {
    1: [event_card('18:00 - 22:00', 'Bienvenida Peru Tech Week 2026', 'PTW', highlight=True)],
    2: [event_card('16:00 - 21:00', 'Fintech & Proptech Mixer', 'ADN')],
    3: [event_card('09:00 - 17:00', 'Experiencia Endeavor', 'ENDEAVOR', custom_url='https://www.joinnus.com/landing/endeavor-2026'),
        event_card('10:00 - 19:30', 'Peru Business Fest', 'COFIDE')],
    4: [event_card('09:00 - 19:00', 'Peru Venture Capital Conference 2026', 'PECAP', highlight=True, custom_url='https://www.peruvcconference.com/'),
        event_card('10:00 - 19:30', 'Peru Business Fest', 'COFIDE')],
    5: [event_card('09:00 - 18:00', 'Techsuyo', 'PERU SV'),
        event_card('10:00 - 19:30', 'Peru Business Fest', 'COFIDE'),
        event_card('18:00 - 22:00', 'Cóctel de cierre PTW 2026', 'PTW', highlight=True)],
    6: [event_card('10:00 - 19:30', 'Peru Business Fest', 'COFIDE')],
    7: [empty_cell()],
}

new_event_columns = ''
for col, cards in day_cells.items():
    content_inner = '\n                '.join(cards)
    new_event_columns += f'''
          <!-- Col {col} -->
          <div style="grid-column: {col}; padding: 10px 8px 10px {('0' if col == 1 else '8px')};">
            {content_inner}
          </div>'''

# ─────────────────────────────────────────────────────────────
# 3. Replace the old event columns inside the desktop grid
#    Find the grid that has the separators + event rows
# ─────────────────────────────────────────────────────────────
# Find the opening of the events grid div
grid_open = 'display: grid; grid-template-columns: repeat(7, minmax(40px,1fr)); gap: 0; position: relative; overflow-x: auto;">'
grid_start = template.find(grid_open)

if grid_start == -1:
    print("Events grid not found!")
else:
    # Find end of this grid: look for the closing </div> that matches
    # The grid opens at grid_start + len(grid_open)
    content_start_pos = grid_start + len(grid_open)
    
    # Count nested divs to find the correct closing tag
    depth = 1
    pos = content_start_pos
    while pos < len(template) and depth > 0:
        next_open = template.find('<div', pos)
        next_close = template.find('</div>', pos)
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        elif next_close != -1:
            depth -= 1
            pos = next_close + 6
        else:
            break
    
    grid_end = pos  # pos is right after the closing </div>
    
    # Build separators
    separators = ''.join([
        f'\n          <div style="position: absolute; top: 0; bottom: 0; left: calc({i} * 100% / 7); border-left: 1px dashed #2a2a2a;"></div>'
        for i in range(1, 7)
    ])
    
    new_grid_content = f'''
{separators}
{new_event_columns}
        '''
    
    # Replace grid content (between grid opening tag and its closing </div>)
    template = template[:content_start_pos] + new_grid_content + '</div>' + template[grid_end:]
    print("Desktop grid replaced!")

# ─────────────────────────────────────────────────────────────
# 4. Update the mobile calendar cards
# ─────────────────────────────────────────────────────────────
# Find the cal-mobile div and replace its content
mobile_start = template.find('<div class="cal-mobile"')
mobile_end = template.find('</div>\n    </div>', mobile_start)  # close of inner flex column + cal-mobile

# Build new mobile cards
mobile_events = {
    'Lun': ('12', 'Lunes 12 oct', [('18:00 - 22:00', 'Bienvenida Peru Tech Week 2026', 'PTW')]),
    'Mar': ('13', 'Martes 13 oct', [
        ('16:00 - 21:00', 'Fintech & Proptech Mixer', 'ADN'),
    ]),
    'Mié': ('14', 'Miércoles 14 oct', [
        ('09:00 - 17:00', 'Experiencia Endeavor', 'ENDEAVOR', 'https://www.joinnus.com/landing/endeavor-2026'),
        ('10:00 - 19:30', 'Peru Business Fest', 'COFIDE'),
    ]),
    'Jue': ('15', 'Jueves 15 oct', [
        ('09:00 - 19:00', 'Peru Venture Capital Conference 2026', 'PECAP', 'https://www.peruvcconference.com/'),
        ('10:00 - 19:30', 'Peru Business Fest', 'COFIDE'),
    ]),
    'Vie': ('16', 'Viernes 16 oct', [
        ('09:00 - 18:00', 'Techsuyo', 'PERU SV'),
        ('10:00 - 19:30', 'Peru Business Fest', 'COFIDE'),
        ('18:00 - 22:00', 'Cóctel de cierre PTW 2026', 'PTW'),
    ]),
    'Sáb': ('17', 'Sábado 17 oct', [('10:00 - 19:30', 'Peru Business Fest', 'COFIDE')]),
    'Dom': ('18', 'Domingo 18 oct', []),
}

def mobile_card(abbr, num, full, events):
    has_events = len(events) > 0
    border_color = '#DD1C29' if abbr == 'Lun' else ('#2a2a2a' if not has_events else '#3a3a3a')
    bg = 'rgba(221,28,41,.06)' if abbr == 'Lun' else '#0f0d0d'
    num_color = '#DD1C29' if has_events else '#4a4a4a'
    abbr_color = '#DD1C29' if abbr == 'Lun' else ('#E4E4E4' if has_events else '#4a4a4a')
    
    events_html = ''
    for event in events:
        time = event[0]
        title = event[1]
        org = event[2]
        custom_url = event[3] if len(event) > 3 else None
        ptw_org = org == 'PTW'
        org_color = '#DD1C29' if ptw_org else '#7a7a7a'
        reg = f'<div style="margin-top: 8px;"><a href="{custom_url}" target="_blank" rel="noopener" style="color: #DD1C29; text-decoration: underline; text-underline-offset: 3px; font-size: 15px; font-weight: 600;">Regístrate →</a></div>' if custom_url else ''
        events_html += f'''
            <div style="border-top: 1px solid #2a2a2a; padding-top: 10px; margin-top: 10px;">
              <div style="font-size: 13px; color: #6a6a6a; font-family: 'Codec Pro', sans-serif;">{time}</div>
              <div style="font-size: 16px; font-weight: 700; color: #fff; font-family: 'Codec Pro', sans-serif; line-height: 1.3; margin-top: 3px;">{title}</div>
              <div style="font-size: 13px; color: {org_color}; font-weight: 600; font-family: 'Codec Pro', sans-serif; margin-top: 2px;">{org}</div>
              {reg}
            </div>'''
    
    no_event_msg = '' if has_events else '<div style="font-size: 13px; color: #4a4a4a; font-family: \'Codec Pro\', sans-serif; font-style: italic;">Sin eventos confirmados</div>'
    
    return f'''<div style="border: 1px solid {border_color}; background: {bg}; border-radius: 12px; padding: 16px 18px;">
          <div style="display: flex; align-items: flex-start; gap: 14px;">
            <div style="text-align: center; min-width: 44px; flex-shrink: 0;">
              <div style="font-family: 'Codec Pro', sans-serif; font-size: 12px; font-weight: 700; color: {abbr_color}; text-transform: uppercase; letter-spacing: 1px;">{abbr}</div>
              <div style="font-family: 'Codec Pro', sans-serif; font-size: 30px; font-weight: 700; color: {num_color}; line-height: 1;">{num}</div>
            </div>
            <div style="flex: 1; border-left: 1px solid #2a2a2a; padding-left: 14px; padding-top: 2px;">
              <div style="font-family: 'Codec Pro', sans-serif; font-size: 14px; font-weight: 600; color: #E4E4E4;">{full}</div>
              {no_event_msg}
              {events_html}
            </div>
          </div>
        </div>'''

mobile_cards_html = '\n        '.join([
    mobile_card(abbr, num, full, evts) 
    for abbr, (num, full, evts) in mobile_events.items()
])

new_mobile_section = f'''<div class="cal-mobile" style="display: none;">
      <div style="display: flex; flex-direction: column; gap: 12px;">
        {mobile_cards_html}
      </div>
    </div>'''

if mobile_start != -1:
    # find closing </div>\n    </div> after cal-mobile open
    close_inner = template.find('</div>\n    </div>', mobile_start)
    close_end = close_inner + len('</div>\n    </div>')
    template = template[:mobile_start] + new_mobile_section + template[close_end:]
    print("Mobile calendar updated!")
else:
    print("Mobile calendar not found!")

# ─────────────────────────────────────────────────────────────
# 5. Save & validate
# ─────────────────────────────────────────────────────────────
new_template_json = json.dumps(template, ensure_ascii=True).replace('</', r'<\/')
new_content = content[:content_start] + new_template_json + content[close_pos:]

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

with open('src/index.html', 'r', encoding='utf-8') as f:
    c2 = f.read()
s2 = c2.find(OPEN) + len(OPEN)
e2 = c2.find(CLOSE, s2)
t2 = json.loads(c2[s2:e2].strip())
print("JSON valid:", len(t2) > 0)
print("Bienvenida in template:", 'Bienvenida Peru Tech Week 2026' in t2)
print("Techsuyo in template:", 'Techsuyo' in t2)
print("PVCC in template:", 'Peru Venture Capital Conference' in t2)
print("Done!")
