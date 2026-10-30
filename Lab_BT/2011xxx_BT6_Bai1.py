def calculate_emi(principal, annual_rate, months):

    #Buoc 1 chuyển lãi suất năm sang lãi suất tháng
    monthly_rate = annual_rate / 12

    #Bước 2 tình EMI hằng tháng theo công thức
    emi = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

    #Bước 3 tính tổng tiền phải trả trong toàn bộ kỳ hạn
    total_payment = emi * months

    #Bước 4 tính tổng tiền lãi
    total_interest = total_payment - principal

    #Bước 5 trả về 2 giá trị bằng tuple
    return emi, total_interest

#Phần chạy chương trình
principal = 1_000_000_000
annual_rate = 0.12
months = 12

#SỬ dụng  unpacking để nhận 2 giá trị
monthly_emi, total_interest = calculate_emi(principal, annual_rate, months)

#In kết quả 
print(f"Trả mỗi tháng: {monthly_emi:,.0f} VND")
print(f"Tổng lãi phải trả: {total_interest:,.0f} VND")

