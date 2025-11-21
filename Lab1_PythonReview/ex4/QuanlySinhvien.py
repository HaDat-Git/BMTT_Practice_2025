from Sinhvien import Sinhvien

class QuanlySinhvien:
    listSinhvien = []
    
    def generateID(self):
        maxID = 1
        if (self.Soluongsinhvien() > 0):
            maxID = self.listSinhvien[0]._id
            for sv in self.listSinhvien:
                if (maxID > sv._id):
                    maxID = sv._id
            maxID += 1
        return maxID
    
    def Soluongsinhvien(self):
        return self.listSinhvien.__len__()
    
    def NhapSinhvien(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        sv = Sinhvien(svID, name, sex, major, avgScore = 0)
        self.xepLoaiHocLuc(sv)
        self.listSinhvien.append(sv)
        
    def UpdateSinhvien(self, ID):
        sv:Sinhvien = self.FindByID(ID)
        if (sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành sinh viên: ")
            avgScore = float(input("Nhập điểm trung bình sinh viên: "))
            sv._name = name
            sv.sex = sex
            sv._major = major
            sv._avgScore = avgScore
            self.xepLoaiHocLuc(sv)
        else:
            print("Không tìm thấy sinh viên với ID: " + str(ID))
            
    def sortByID(self):
        self.listSinhvien.sort(key=lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhvien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByAvgScore(self):
        self.listSinhvien.sort(key=lambda x: x._avgScore, reverse=True)
        
    def FindByID(self, ID):
        searchResult = None
        if (self.Soluongsinhvien() > 0):
            for sv in self.listSinhvien:
                if (sv._id == ID):
                    searchResult = sv
                return searchResult
            
    def FindByName(self, keyword):
        ListSV = []
        if (self.Soluongsinhvien() > 0):
            for sv in self.listSinhvien:
                if (keyword.lower() in sv._name.lower()):
                    ListSV.append(sv)
        return ListSV
        
    def deleteByID(self, ID):
        isDeleted = False
        sv = self.FindByID(ID)
        if (sv != None):
            self.listSinhvien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:Sinhvien):
        if (sv._avgScore >= 9):
            sv._rank = "Xuất sắc"
        elif (sv._avgScore >= 8):
            sv._rank = "Giỏi"
        elif (sv._avgScore >= 6.5):
            sv._rank = "Khá"
        elif (sv._avgScore >= 5):
            sv._rank = "Trung bình"
        else:
            sv._rank = "Yếu"
            
    def ShowSinhvien(self, listSv):
        print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}".format("ID", "Name", "Sex", "Major", "Average Score", "Rank"))
        if (listSv.__len__() > 0):
            for sv in listSv:
                print("{:<8}{:<18}{:<8}{:<8}{:<8}{:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._avgScore, sv._rank))
        print("\n")
        
    def ShowAllSinhvien(self):
        return self.listSinhvien
        
