var1 = int(input())
var2 = float(input())
var3 = int(input())
print(f"{var1:0=+10}")
print(f"{var2:#>10.2f}")
res_current = (f"{(var3):0>16b}")
res_current = str(res_current)
result = str(res_current)
result = (result[::-1])
print('_'.join(result[i:i+4] for i in range(0, len(result), 4))[::-1])