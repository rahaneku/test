import re
txt = "BlackRock\Reggie.Ahaneku.black"
tt =re.search(r"(\w+\\)(\w+\.\w+)",txt)
res = tt.group(2)
print(res)
