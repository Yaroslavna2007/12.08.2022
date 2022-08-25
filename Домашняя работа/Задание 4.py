x = str(input())
p = x[0: x.find('h')+1]
f = x[x.rfind('h'):]
d = x[x.find('h')+1:x.rfind('h')]
print(p+d.replace('h','H')+f)