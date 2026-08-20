import json, re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN  = '<script type="__bundler/template">'
CLOSE = '</script>'
start_tag     = content.find(OPEN)
content_start = start_tag + len(OPEN)
close_pos     = content.find(CLOSE, content_start)
template = json.loads(content[content_start:close_pos].strip())

# The column 4 block goes from <!-- Column 4 --> up to <script type="text/x-dc"
col4_start = template.find('<!-- Column 4 -->')
dc_script_start = template.find('<script type="text/x-dc"')

print("col4_start:", col4_start)
print("dc_script_start:", dc_script_start)
print("\nContent to replace:")
print(template[col4_start:dc_script_start])

# New column 4: just LinkedIn + Instagram with proper real links
new_col4 = '''<!-- Column 4 -->
      <div style="display: flex; flex-direction: column; gap: 16px; align-items: flex-start;">
        <h4 style="margin: 0 0 4px; font-family: 'Codec Pro', sans-serif; font-size: 23px; font-weight: 700; color: #fff;">Síguenos</h4>
        <!-- LinkedIn -->
        <a href="https://www.linkedin.com/company/peru-tech-week/" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 10px; color: #b9b9b9; text-decoration: none; font-family: 'Codec Pro', sans-serif; font-size: 19px; transition: color .2s;" style-hover="color: #fff;">
          <span style="width: 36px; height: 36px; background: #0A66C2; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
          </span>
          LinkedIn
        </a>
        <!-- Instagram -->
        <a href="https://www.instagram.com/perutechweek/" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 10px; color: #b9b9b9; text-decoration: none; font-family: 'Codec Pro', sans-serif; font-size: 19px; transition: color .2s;" style-hover="color: #fff;">
          <span style="width: 36px; height: 36px; background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          </span>
          Instagram
        </a>
      </div>
      '''

# Replace the block from col4_start to dc_script_start
template = template[:col4_start] + new_col4 + template[dc_script_start:]

print("\nAfter replacement:")
print("LinkedIn link present:", 'linkedin.com/company/peru-tech-week' in template)
print("Instagram link present:", 'instagram.com/perutechweek' in template)
print("Old X/Twitter gone:", 'M4 4l11.733 16h4.267' not in template)

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
