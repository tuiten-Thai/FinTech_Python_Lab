def credit_score(income, credit_history_years, has_bad_debt=False):

    # Dieu_kien 1 neu khach hang co no xau
    if has_bad_debt == True:
        return "Reject"

    # Dieu_kien 2: neu thu nhap thap hoặc lịch sử tín dụng ngắn
    elif income < 10000000 or credit_history_years < 1:
        return "High Risk"

    # Điều kiện 3: THu nhập cao và lịch sử tín dụng tốt
    elif income >= 20000000 or credit_history_years >= 3:
        return "VIP"

    #Điều kiện 4: Các trường hợp còn lại
    else:
        return "Standard"


#Nhập thông tin khách hàng
income = float(input("Nhập thu nhập hàng tháng (VND): "))
credit_history_years = int(input("Nhập số năm lịch sử tín dụng: "))

has_bad_debt = input("Khách hàng có nợ xấu không? (yes/no): ").strip().lower()

if has_bad_debt == "yes":
    has_bad_debt == True

elif has_bad_debt == "no":
    has_bad_debt == False

else:
    print("Dữ liệu nợ xấu không hợp lệ!")
    exit()    


# GÓi hàng chấm điểm tín dụng
result = credit_score(income, credit_history_years, has_bad_debt)

#Hiển thị kết quả
print("-------------------------------------------")
print("KẾT QUẢ CHẤM ĐIỂM TÍN DỤNG")
print("Thu nhập:", format(income, ",.0f"), "VND")
print("Lịch sử tín dụng:", credit_history_years, "năm")
print("Nợ xấu:", has_bad_debt)
print("Xếp loại khách hàng:", result)
print("-------------------------------------------")



