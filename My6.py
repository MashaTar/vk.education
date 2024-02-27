import sys
n = int(input())
ans = []
k=0
while True:
    s=sys.stdin.readline()
    if s == '' or s == '\n':
        break

    if k>=n:
        continue

    nums = [int(x) for x in s.split()]
    ans.append(max(nums))
    k+=1

ans.sort()
ans.reverse()
print(';'.join(str(gg) for gg in ans))