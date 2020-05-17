# Тоон дарааллын хамгийн их болон багын байрыг соль.
numbers =[int(x) for x in input().split()]
min_element = min(numbers)
min_element_index = numbers.index(min_element)
max_element = max(numbers)
max_element_index = numbers.index(max_element)
numbers[min_element_index] = max_element
numbers[max_element_index] = min_element
print(numbers)

