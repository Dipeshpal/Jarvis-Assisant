import re

txt = "delete my shopping list"

print(re.search(r"^delete *.+ list$", txt))