# 1. Danh sách ban đầu chứa 5 linh kiện
kho_linh_kien = [
    {"ma": "RES_10K", "so_luong": 250},
    {"ma": "CAP_100UF", "so_luong": 45},
    {"ma": "IC_NE555", "so_luong": 80},
    {"ma": "LED_RED", "so_luong": 500},
    {"ma": "DIO_4007", "so_luong": 15},
]


def tim_linh_kien_sap_het(danh_sach, nguong=100):
    """Tìm và in các mã linh kiện có số lượng < nguong"""
    print(f"\n--- CÁC MÃ LINH KIỆN SẮP HẾT (< {nguong}) ---")
    tim_thay = False
    for item in danh_sach:
        if item["so_luong"] < nguong:
            print(f"- Mã: {item['ma']} (Số lượng còn: {item['so_luong']})")
            tim_thay = True

    if not tim_thay:
        print("Không có linh kiện nào sắp hết.")


def them_linh_kien(danh_sach, ma, so_luong):
    """Thêm linh kiện mới hoặc cộng dồn nếu đã tồn tại"""
    for item in danh_sach:
        if item["ma"] == ma:
            item["so_luong"] += so_luong
            print(f"-> Đã cập nhật số lượng cho {ma}: {item['so_luong']}")
            return

    danh_sach.append({"ma": ma, "so_luong": so_luong})
    print(f"-> Đã thêm mới linh kiện: {ma}")


def xoa_linh_kien(danh_sach, ma):
    """Xóa linh kiện khỏi danh sách theo mã"""
    for item in danh_sach:
        if item["ma"] == ma:
            danh_sach.remove(item)
            print(f"-> Đã xoá linh kiện: {ma}")
            return
    print(f"-> Không tìm thấy mã {ma} để xoá.")


# ================== CHẠY THỬ CHƯƠNG TRÌNH ==================
if __name__ == "__main__":
    # In danh sách các mã < 100 ban đầu
    tim_linh_kien_sap_het(kho_linh_kien)

    # Thêm linh kiện mới
    print("\n--- THỰC HIỆN THÊM MỚI ---")
    them_linh_kien(kho_linh_kien, "TRANS_2N2222", 60)

    # Xoá một linh kiện
    print("\n--- THỰC HIỆN XOÁ ---")
    xoa_linh_kien(kho_linh_kien, "CAP_100UF")

    # Kiểm tra lại các mã < 100 sau khi thêm/xoá
    tim_linh_kien_sap_het(kho_linh_kien)