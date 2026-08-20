import json, re

with open('src/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

OPEN = '<script type="__bundler/template">'
start = content.find(OPEN) + len(OPEN)
end = content.find('</script>', start)
t = json.loads(content[start:end].strip())

# Find the componentDidMount to check for IO errors
idx = t.find('componentDidMount()')
print("=== componentDidMount ===")
print(t[idx:idx+1200])

# Also check for animation-timeline (not well supported on mobile Chrome)
count_at = t.count('animation-timeline')
print(f"\nanimation-timeline occurrences: {count_at}")

# Check for CSS.registerProperty or other unsupported APIs  
print("\nCSS.registerProperty:", 'CSS.registerProperty' in t)
print("animation-timeline: view()", 'animation-timeline: view()' in t)
