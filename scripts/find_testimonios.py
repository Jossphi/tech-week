import json, re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

# Find start of testimonials section
t_start = template.find('\n<section', template.find('data-screen-label="Testimonios"') - 50)
if t_start == -1:
    t_start = template.rfind('<section', 0, template.find('data-screen-label="Testimonios"'))

# Find start of NEXT section after testimonials
next_section = template.find('\n<!-- ============', template.find('data-screen-label="Testimonios"'))
if next_section == -1:
    next_section = template.find('\n<section', template.find('data-screen-label="Testimonios"') + 100)

print("Section start:", t_start)
print("Next section start:", next_section)
print("\n--- TESTIMONIOS START ---")
print(template[t_start:t_start+120])
print("\n--- NEXT SECTION ---")
print(template[next_section:next_section+120])
