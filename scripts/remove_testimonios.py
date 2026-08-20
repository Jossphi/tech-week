import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

# Remove testimonials section: from its \n<section to the \n before <!-- 11. SPONSORS -->
t_start = 75937  # \n<section data-screen-label="Testimonios"
t_end   = 79466  # \n<!-- ============ 11. SPONSORS ============ -->

removed = template[t_start:t_end]
print("Removing block (first 200 chars):", removed[:200])
print("Removed block ends with:", removed[-100:])

template = template[:t_start] + template[t_end:]

print("\nTestimonios still present:", 'data-screen-label="Testimonios"' in template)

new_template_json = json.dumps(template, ensure_ascii=True).replace('</', r'<\/')
new_content = content[:content_start] + new_template_json + content[close_pos:]

with open('src/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# Validate
with open('src/index.html', 'r', encoding='utf-8') as f:
    c2 = f.read()
s2 = c2.find(OPEN) + len(OPEN)
e2 = c2.find(CLOSE, s2)
t2 = json.loads(c2[s2:e2].strip())
print("JSON valid:", len(t2) > 0)
print("Done!")
