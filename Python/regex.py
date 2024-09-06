#Metacharacters (.) DOT matches any character except new line

import re
pattern=r"hel.o"
if re.match(pattern,"hello"):
    print("match1")
if re.match(pattern,"ello"):
    print("match2")    

#Metacharacters (^ and $) 
# the below code find the pattern in a string which starts with "piyush." and then any character(s)
pattern2=r"^piyush\..*$"
if re.match(pattern2,"piyush. kumar gupta"):
    print("match1")
if re.match(pattern2,"ello piyush kumar gupta"):
    print("match2")

# to find the pattern for total 3 characters where last 3rd character will be !
pattern3=r"^.{2}\!$"    
if re.match(pattern3,"hell!"):
    print("found")

#Search and replace
    
def replace_str(input_str,to_replace_with,pattern):
    
        a=re.sub(pattern,to_replace_with,input_str)
        return a
    
pattern=r"Piyush"    
input_str=input()
to_replace_with=input()
print(replace_str(input_str,to_replace_with,pattern))    

