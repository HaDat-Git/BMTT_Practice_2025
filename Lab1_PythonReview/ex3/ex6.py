def del_elment_index(dict, index):
    if index in dict:
        del dict[index]
        return True
    else:
        return False
    
my_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
index_to_delete = int(input("Nhập chỉ mục của phần tử bạn muốn xóa: "))
result = del_elment_index(my_dict, index_to_delete)
if result:
    print(f"Phần tử tại chỉ mục {index_to_delete} đã được xóa.")
else:
    print(f"Chỉ mục {index_to_delete} không tồn tại trong từ điển.")
print("Từ điển sau khi xóa:", my_dict)