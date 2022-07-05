#codeing:utf-8

import itertools

key = []
cipher = "ilnllliiikkninlekile" # 密文

for i in itertools.permutations('ilnke', 5): # 字典表
    key.append(''.join(i))

for now_key in key:
    solve_c = ""
    res = ""
    for now_c in cipher:
        solve_c += str(now_key.index(now_c))
    for i in range(0, len(solve_c), 2):
        now_ascii = int(solve_c[i]) * 5 + int(solve_c[i + 1]) + 97
        if now_ascii > ord('i'):
            now_ascii += 1
        res += chr(now_ascii)
        
    if "flag" in res: # 判断是否有关键词flag
        print(now_key, res)
