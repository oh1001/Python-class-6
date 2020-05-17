# Нэрсийн дарааллаас хамгийн богино нэрийг олж 'Сайн уу?' гэж соль.
names = input().split()
index = names.index(min(names, key=len))
names[index] = 'Sain uu'
print(names)