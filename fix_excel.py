with open('services/excel_handler.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 替换第138-144行 (0-indexed: 137-143)
new_lines = lines[:137] + [
    "                'has_group_level3': get_int(row.get('集团综维三级人数', 0)),\n",
    "                'has_group_level4': get_int(row.get('集团综维四级', 0)),\n",
    "                'has_group_level5': get_int(row.get('集团综维五级', 0)),\n",
    "                'has_special_double_cert': 0,\n",
    "                'group_cert_count': 0,\n",
    "                'specialist_cert_count': 0,\n",
] + lines[144:]

with open('services/excel_handler.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Fixed')
