# Тоон дарааллын элементүүдын хамгийн бага элементийг ол.
numbers = [1,3,1,2,3,9]
min_element = 1 # baij boloh hamgiin baga too gej uzev
for num in numbers:
    if num < min_element:
        min_element = num
print("min:", min_element)
print("min1:", min(numbers)) # hamgiin amarhan arga