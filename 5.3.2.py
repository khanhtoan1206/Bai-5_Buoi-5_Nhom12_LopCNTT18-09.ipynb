import math

# --- Thay đổi đồ thị ở đây (3 thành phố để quan sát rõ) ---
GRAPH_TSP = [
    [math.inf, 20, 15],   # từ thành phố 0
    [20, math.inf, 35],   # từ thành phố 1
    [15, 35, math.inf]    # từ thành phố 2
]
SO_THANH_PHO = len(GRAPH_TSP)

# Biến toàn cục để lưu nghiệm tốt nhất
CHI_PHI_TOI_THIEU_HIEN_TAI = math.inf
DUONG_DI_TOT_NHAT_HIEN_TAI = []


def giai_tsp_bnbl_in(current_city, current_path, current_cost):
    """
    Hàm giải TSP bằng nhánh cận (branch and bound) với in chi tiết
    """
    global CHI_PHI_TOI_THIEU_HIEN_TAI, DUONG_DI_TOT_NHAT_HIEN_TAI

    # --- Cắt tỉa (pruning) ---
    if current_cost >= CHI_PHI_TOI_THIEU_HIEN_TAI:
        print(f"❌ Cắt nhánh {current_path} vì cost={current_cost} >= best={CHI_PHI_TOI_THIEU_HIEN_TAI}")
        return

    # --- Điều kiện dừng (đi hết các thành phố) ---
    if len(current_path) == SO_THANH_PHO:
        cost_to_return = GRAPH_TSP[current_city][current_path[0]]
        if cost_to_return != math.inf:
            tong_chi_phi = current_cost + cost_to_return
            print(f"✔️ Hoàn thành lộ trình {current_path+[current_path[0]]}, cost={tong_chi_phi}")
            if tong_chi_phi < CHI_PHI_TOI_THIEU_HIEN_TAI:
                CHI_PHI_TOI_THIEU_HIEN_TAI = tong_chi_phi
                DUONG_DI_TOT_NHAT_HIEN_TAI = current_path + [current_path[0]]
        return

    # --- Nhánh (branching) ---
    for next_city in range(SO_THANH_PHO):
        if next_city != current_city and \
           next_city not in current_path and \
           GRAPH_TSP[current_city][next_city] != math.inf:

            new_cost = current_cost + GRAPH_TSP[current_city][next_city]
            print(f"Đi {current_city} → {next_city}, path={current_path+[next_city]}, cost={new_cost}")
            giai_tsp_bnbl_in(next_city, current_path+[next_city], new_cost)


print("\n--- Giải Bài toán Người du lịch (3 thành phố) bằng Nhánh cận ---")
giai_tsp_bnbl_in(0, [0], 0)

print("\nKẾT QUẢ:")
print(f"Ma trận chi phí: {GRAPH_TSP}")
print(f"Tổng chi phí đường đi ngắn nhất: {CHI_PHI_TOI_THIEU_HIEN_TAI}")
print(f"Đường đi tối ưu: {DUONG_DI_TOT_NHAT_HIEN_TAI}")
