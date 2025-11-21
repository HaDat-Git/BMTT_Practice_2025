from QuanlySinhvien import QuanlySinhvien

qlsv = QuanlySinhvien()
while True:
    print("----- Quản lý sinh viên -----")
    print("1. Thêm sinh viên")
    print("2. Cập nhập thông tin sinh viên")
    print("3. Xóa sinh viên = ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")   
    choice = input("Chọn một tùy chọn (0-7): ")
    if choice == '1':
        print("Thêm sinh viên")
        qlsv.NhapSinhvien()
        print("Sinh viên đã được thêm.")
    elif choice == '2':
        if(qlsv.Soluongsinhvien() > 0):
            print("Cập nhật thông tin sinh viên")
            print("Nhập ID: ")
            ID = int(input())
            qlsv.UpdateSinhvien(ID)
        else:
            print("Danh sách sinh viên trống.")
    elif choice == '3':
        if(qlsv.Soluongsinhvien() > 0):
            print("\n Xóa sinh viên")
            print("Nhập mã số sinh viên cần xóa: ")
            ID = int(input())
            if (qlsv.deleteByID(ID)):
                print("Xóa sinh viên thành công.")
            else:
                print("Xóa sinh viên thất bại. Không tìm thấy sinh viên với mã số đã cho.")
    elif choice == '4':
        if (qlsv.Soluongsinhvien() > 0):
            print("\n Tìm kiếm sinh viên theo tên")
            print("Nhập tên sinh viên: ")
            name = (input())
            nameRs = qlsv.FindByName(name)
            qlsv.ShowSinhvien(nameRs)
        else:
            print("Danh sách sinh viên trống.")
    elif choice == '5':
        if (qlsv.Soluongsinhvien() > 0):
            print("\n Sắp xếp sinh viên theo điểm trung bình")
            qlsv.sortByAvgScore()
            qlsv.ShowSinhvien(qlsv.listSinhvien)
        else:
            print("Danh sách sinh viên trống.")
    elif choice == '6':
        if (qlsv.Soluongsinhvien() > 0):
            print("\n Sắp xếp sinh viên theo tên chuyên ngành")
            qlsv.sortByName()
            qlsv.ShowSinhvien(qlsv.listSinhvien)
        else:
            print("Danh sách sinh viên trống.")
    elif choice == '7':
        if (qlsv.Soluongsinhvien() > 0):
            print("\n Danh sách sinh viên")
            qlsv.ShowSinhvien(qlsv.listSinhvien)
        else:
            print("Danh sách sinh viên trống.")
    elif choice == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")