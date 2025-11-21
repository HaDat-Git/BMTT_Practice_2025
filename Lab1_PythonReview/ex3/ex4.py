def SearchElement(tuple):
    first_element = tuple[0]
    last_element = tuple[-1]
    return first_element, last_element

input_text = input("Nhập chuỗi các số nguyên (được ngăn cách bởi dấu ','): ")
numlist = [int(x) for x in input_text.split(",")]
num_tuple = tuple(numlist)
first, last = SearchElement(num_tuple)
print("Phần tử đầu tiên trong tuple là:", first)
print("Phần tử cuối cùng trong tuple là:", last)