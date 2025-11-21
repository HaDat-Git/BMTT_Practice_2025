def CreateTuple(list):
    return tuple(list)

input_text = input("Nhập chuỗi các số nguyên (được ngăn cách bởi dấu ','): ")
numlist = [int(x) for x in input_text.split(",")]
result_tuple = CreateTuple(numlist)
print("Danh sách ban đầu là:", numlist)
print("Bộ tuple được tạo ra là:", result_tuple)