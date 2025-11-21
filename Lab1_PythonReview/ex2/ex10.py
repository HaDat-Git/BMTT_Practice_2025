def ConvertText(text):
    return text[::-1]

input_text = input("Nhập văn bản cần chuyển đổi: ")
converted_text = ConvertText(input_text)
print("Văn bản sau khi chuyển đổi: " + converted_text)