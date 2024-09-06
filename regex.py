#Metacharacters (.) DOT matches any character except new line

import re
pattern=r"hel.o"
if re.match(pattern,"helllo"):
    print("match1")
if re.match(pattern,"ello"):
    print("match2")    
