# Нэрсийн дарааллаас хамгийн урт нэрийг олж бүх үсгийг том болго.
names = ['baatar', 'bold', 'danzanravjaa', 'string']
index = names.index(max(names, key=len))
names[2] = names[2].upper()
print(names) # list dotroo tom bolgoh

print(max(names, key=len).upper())
