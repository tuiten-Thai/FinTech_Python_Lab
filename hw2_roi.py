# hw2_roi.py

# Nhập tổng vốn ban đầu và tổng giá trị bán ra
initial_investment = float(input("Nhập tổng vốn ban đầu: "))
final_value = float(input("Nhập tổng giá trị bán ra: "))

# Tính lợi nhuận ròng
net_profit = final_value - initial_investment

# Tính ROI
roi = (net_profit / initial_investment) * 100

# Hiển thị kết quả
print("Lợi nhuận ròng (Net Profit):", net_profit)
print("Tỷ suất sinh lời (ROI):", roi, "%")
