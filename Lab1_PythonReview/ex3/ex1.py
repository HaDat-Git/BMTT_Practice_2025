def Sum_Even(numlist):
    total = 0
    for num in numlist:
        if num % 2 == 0:
            total += num
    return total

n = input("Nhập vào một chuỗi số nguyên, ngăn cách nhau bởi dấu phẩy: ")
numlist = [int(x) for x in n.split(",")]
result = Sum_Even(numlist)
print("Tổng các số chẵn trong chuỗi là:", result)
    