# Тоон дарааллын элементүүдын хамгийн их элементийг ол.
numbers = [1,3,1,2,3,9]
max_element = -9999999999999 # baij boloh hamgiin baga too gej uzev
for num in numbers:
    if num > max_element:
        max_element = num
print("max:", max_element)
print("max1:", max(numbers)) # hamgiin amarhan arga