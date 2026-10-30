
#bài tập: Mô phỏng kế hoạch tích luỹ hưu trí

tuoi = 25
so_du = 0.0
tien_gui = 60000000.0
lai_suat = 0.10
tang_tien_gui = 0.08
muc_tieu = 10000000000.0

nam = 1

print("BAO CÁO TÍCH LUỸ QUỸ HƯU TRÍ")


print("-" * 100)
print(f"{'Năm':<6}| {'Tuổi':<6}| {'Số tiền gửi mới':>20}|"
          f"{'Tiền lãi trong năm':>20} | {'Tổng tài sản cuối năm':>25}")
print("-" * 100)

while so_du < muc_tieu:
    #Luu so du dau nam
    so_du_dau_nam = so_du   

    #tinh tien lai trong nam
    tien_lai = so_du_dau_nam * lai_suat

    #tinh tong tai san cuoi nam
    so_du = so_du_dau_nam + tien_lai + tien_gui

    #In bao cao cua nam hien tai
    print(f"{nam:<6}| {tuoi:<6}| {tien_gui:>20,.0f}|"
          f"{tien_lai:>20,.0f} | {so_du:>25,.0f}")
          

    #tang tien gui cho nam tiep thep
    tien_gui = tien_gui * (1 + tang_tien_gui)

    #Chuyen sang nam va tuoi tiep theo
    nam = nam + 1
    tuoi = tuoi + 1

print("-" * 90)
print(f"Dat muc tieu {muc_tieu:,.0f} VNĐ")
print(f"So nam tích luỹ: {nam - 1 } năm")
print(f"Tuổi khi đạt mục tiêu: {tuoi - 1} tuổi")
print(f"Tổng tài sản: {so_du:,.0f} VNĐ")
