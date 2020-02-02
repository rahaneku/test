import re
txt = "BadTouch\Abloggs.Joe"
tt =re.search(r"(\w+\\)(\w+\.\w+)",txt)
res = tt.group(2)
print(res)
