from collections import Counter


def sortString(s: str) -> str:
    cnt = Counter(s)
    ans=[]
    asc=True
         
    while cnt:
        for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):
            ans.append(c)
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]
        asc = not asc
    return ''.join(ans)


print(sortString('aabbccaa'))
