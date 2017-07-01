
import re


val="01012341234" #11



if re.match('^01[0-9][1-9]\d{7}$', val):
     print("matched") 
else:
     print("invalid")