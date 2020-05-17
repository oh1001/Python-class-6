# hamgiin urt neriig avah
names = ['baatar', 'bold', 'danzanravjaa', 'string']
max_len = 2
max_len_name = ''
for name in names:
    if len(name)>max_len:
        max_len = len(name)
        max_len_name = name
print(max_len_name)
print(max(names,key=len)) # amarhan arga