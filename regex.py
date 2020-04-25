import re

fhandle = open('regex_sum_448602.txt')
sum_total = 0

for line in fhandle:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        for i in x:
            sum_total  = sum_total + int(i)
print(sum_total)


    
    