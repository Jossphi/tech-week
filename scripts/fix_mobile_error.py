import json, re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

print("Before - animation-timeline count:", template.count('animation-timeline'))

# Remove all animation-timeline and animation-range properties from inline styles
# Pattern: "; animation-timeline: view(); animation-range: entry 0% entry 35%;"
template = re.sub(
    r';\s*animation-timeline:\s*view\(\);\s*animation-range:[^;"]+',
    '',
    template
)
# Also standalone (at start or end of style value)
template = re.sub(
    r'\s*animation-timeline:\s*view\(\);\s*animation-range:[^;"]+;?\s*',
    '',
    template
)
template = re.sub(
    r'\s*animation-timeline:\s*view\(\)\.?\s*',
    '',
    template
)

print("After - animation-timeline count:", template.count('animation-timeline'))

# Also add 'reveal' class to the elements that had animation-timeline
# The About grid had it - let's make sure it has the reveal class
# Check if already present
print("About grid has reveal:", 'class="about-grid"' in template)

# Save
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
print("animation-timeline remaining:", t2.count('animation-timeline'))
print("Done!")
