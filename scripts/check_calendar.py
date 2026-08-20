import json

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN = '<script type="__bundler/template">'
start = content.find(OPEN) + len(OPEN)
end = content.find('</script>', start)
t = json.loads(content[start:end].strip())

# Find the 7-column calendar cells content
idx = t.find('Separadores verticales punteados')
print(t[idx-100:idx+4000])
