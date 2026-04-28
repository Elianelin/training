with open('static/js/app.js', 'r', encoding='utf-8') as f:
    content = f.read()

stack = []
line = 1
errors = []
for i, ch in enumerate(content):
    if ch == '\n':
        line += 1
    if ch in '{[(':
        stack.append((ch, line))
    elif ch in '}])':
        if not stack:
            errors.append(f'Unmatched closing {ch} at line {line}')
            break
        top, l = stack.pop()
        pairs = {'{':'}', '[':']', '(':')'}
        if pairs[top] != ch:
            errors.append(f'Mismatched brace: opened {top} at line {l}, closed {ch} at line {line}')
            break

if stack and not errors:
    for ch, l in stack:
        errors.append(f'Unclosed {ch} at line {l}')

if errors:
    print('ERRORS:')
    for e in errors:
        print(e)
else:
    print('OK: braces are balanced')
