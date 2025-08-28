def sinh_so_nhi_phan(n):
    """
    Sinh tất cả các số nhị phân có độ dài n (chỉ gồm chữ số 0,1).
    """
    if n <= 0:
        print("Độ dài phải là số dương.")
        return

    print(f"Các số nhị phân có độ dài {n}:")
    so_luong_so = 2**n   # Tổng số tổ hợp nhị phân

    for i in range(so_luong_so):
        # format i thành dạng nhị phân, độ dài n ký tự
        dang_nhi_phan = f"{i:0{n}b}"
        print(dang_nhi_phan)


def sinh_so_tam_phan(n):
    """
    Sinh tất cả các số tam phân có độ dài n (chỉ gồm chữ số 0,1,2).
    """
    if n <= 0:
        print("Độ dài phải là số dương.")
        return

    print(f"Các số tam phân có độ dài {n}:")
    so_luong_so = 3**n   # Tổng số tổ hợp tam phân

    for i in range(so_luong_so):
        # chuyển i sang dạng tam phân
        so_tam_phan = ""
        x = i
        while x > 0:
            so_tam_phan = str(x % 3) + so_tam_phan
            x //= 3
        # Bổ sung số 0 vào đầu cho đủ n ký tự
        so_tam_phan = so_tam_phan.zfill(n)
        print(so_tam_phan)


# ===============================
# Ví dụ chạy thử
# ===============================

print("=== Số nhị phân độ dài 4 ===")
sinh_so_nhi_phan(4)

print("\n=== Số tam phân độ dài 2 ===")
sinh_so_tam_phan(2)

print("\n=== Số tam phân độ dài 3 ===")
sinh_so_tam_phan(3)

# Danh sách các vật phẩm: (trọng lượng, giá trị)
VAT_PHAM = [(3, 5), (4, 7), (2, 4), (5, 8)]
SUC_CHUA_TOI_DA = 8  # sức chứa tối đa của túi

# Biến toàn cục để lưu trữ giá trị tối ưu và lựa chọn tương ứng
GIA_TRI_TOI_DA_HIEN_TAI = 0
LUA_CHON_TOT_NHAT_HIEN_TAI = []

# Biến đếm số lần hàm được gọi
so_lan_goi = 0


def giai_knapsack_bnb_don_gian(idx, current_weight, current_value, current_selection):
    """
    Giải bài toán cái túi 0/1 bằng quay lui + cắt tỉa đơn giản
    """
    global GIA_TRI_TOI_DA_HIEN_TAI, LUA_CHON_TOT_NHAT_HIEN_TAI, so_lan_goi
    so_lan_goi += 1  # mỗi lần gọi hàm thì tăng biến đếm

    # Nếu quá sức chứa thì dừng (pruning)
    if current_weight > SUC_CHUA_TOI_DA:
        return

    # Nếu đây là nghiệm hợp lệ tốt hơn trước đó thì cập nhật
    if current_value > GIA_TRI_TOI_DA_HIEN_TAI:
        GIA_TRI_TOI_DA_HIEN_TAI = current_value
        LUA_CHON_TOT_NHAT_HIEN_TAI = list(current_selection)

    # Nếu đã xét hết các vật phẩm thì dừng
    if idx == len(VAT_PHAM):
        return

    # --- Nhánh 1: chọn vật phẩm hiện tại ---
    item_weight, item_value = VAT_PHAM[idx]
    giai_knapsack_bnb_don_gian(
        idx + 1,
        current_weight + item_weight,
        current_value + item_value,
        current_selection + [VAT_PHAM[idx]]
    )

    # --- Nhánh 2: bỏ qua vật phẩm hiện tại ---
    giai_knapsack_bnb_don_gian(
        idx + 1,
        current_weight,
        current_value,
        current_selection
    )


# --- Chạy chương trình ---
print("--- Giải bài toán cái túi bằng Nhánh Cận (đơn giản) ---")
print(f"Sức chứa tối đa: {SUC_CHUA_TOI_DA}")
print(f"Danh sách vật phẩm: {VAT_PHAM}")

giai_knapsack_bnb_don_gian(0, 0, 0, [])

print(f"Tổng giá trị lớn nhất có thể đạt được: {GIA_TRI_TOI_DA_HIEN_TAI}")
print(f"Các vật phẩm được chọn: {LUA_CHON_TOT_NHAT_HIEN_TAI}")
print(f"Số lần hàm được gọi: {so_lan_goi}")
