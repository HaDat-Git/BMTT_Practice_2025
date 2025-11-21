def Count(word):
    count_dict = {}
    for char in word:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

input_text = input("Nhập các từ (ngăn cách nhau bởi khoảng trống) : ")
words = input_text.split()

times = Count(words)
print("Số lần xuất hiện của mỗi từ trong danh sách là:", times)