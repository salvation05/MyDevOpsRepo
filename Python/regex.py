#Metacharacters (.) DOT matches any character except new line

import re
pattern=r"hel.o"
if re.match(pattern,"helllo"):
    print("match1")
if re.match(pattern,"ello"):
    print("match2")    

#Metacharacters (^ and $)  
pattern2=r"^piyush$"
if re.match(pattern2,"helllo"):
    print("match1")
if re.match(pattern2,"ello"):
    print("match2")
