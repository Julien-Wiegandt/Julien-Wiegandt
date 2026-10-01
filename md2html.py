import re, sys

src = open(sys.argv[1], encoding='utf-8').read()

# 1. pull the <style> block out verbatim
m = re.search(r'<style>.*?</style>', src, re.S)
style = m.group(0) if m else ''
body_src = src[m.end():] if m else src

def inline(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    return t

lines = body_src.split('\n')
out = []
i = 0
raw_block = False

while i < len(lines):
    line = lines[i]
    s = line.strip()

    # raw HTML blocks (tables, header paragraphs) pass through until they close
    if s.startswith('<table') or s.startswith('<p align') or s.startswith('<h1'):
        raw_block = True
    if raw_block:
        out.append(line)
        if s.startswith('</table>') or (s.startswith('<p align') and s.endswith('</p>')) or s.endswith('</p>') or s.startswith('</h1>') or s.endswith('</h1>'):
            raw_block = False
        i += 1
        continue

    if s.startswith('### '):
        out.append('<h3>' + inline(s[4:]) + '</h3>')
        i += 1
        continue

    if re.match(r'^- ', line):
        block = ['<li>' + inline(line[2:])]
        j = i + 1
        subs = []
        while j < len(lines):
            nxt = lines[j]
            if re.match(r'^  - ', nxt):
                subs.append('<li>' + inline(nxt[4:]) + '</li>')
            elif re.match(r'^  \S', nxt):
                if subs:
                    break
                block.append('<br/>' + inline(nxt.strip()))
            else:
                break
            j += 1
        if subs:
            block.append('<ul>' + ''.join(subs) + '</ul>')
        block.append('</li>')
        out.append(''.join(block))
        # merge consecutive top-level bullets into one <ul>
        i = j
        continue

    if not s:
        out.append('')
        i += 1
        continue

    if s.startswith('<'):
        out.append(line)
    else:
        out.append('<p>' + inline(s) + '</p>')
    i += 1

# wrap runs of <li> in <ul>
html_lines = []
open_ul = False
for l in out:
    if l.startswith('<li>'):
        if not open_ul:
            html_lines.append('<ul>')
            open_ul = True
        html_lines.append(l)
    else:
        if open_ul and l.strip():
            html_lines.append('</ul>')
            open_ul = False
        html_lines.append(l)
if open_ul:
    html_lines.append('</ul>')

html = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<title>Julien Wiegandt</title>' + style + '</head><body>\n'
        + '\n'.join(html_lines) + '\n</body></html>')
open(sys.argv[2], 'w', encoding='utf-8').write(html)
print('ok')
