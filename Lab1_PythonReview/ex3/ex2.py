def ConvertPositionNumList(numlist):
    return numlist[::-1]
    
input_text = input("Nhập chuỗi các số nguyên (được ngăn cách bởi dấu ','): ")
numlist = [int(x) for x in input_text.split(",")]
converted_list = ConvertPositionNumList(numlist)
print("Danh sách sau khi chuyển đổi vị trí:", converted_list)