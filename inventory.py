# QUẢN LÝ KHO HÀNG - MAIN FILE
products = []   
def add_product():
    print(">> Chức năng nhập hàng (sẽ phát triển ở Feature Branch).")

def view_inventory():
    print(">> Chức năng xem tồn kho (sẽ phát triển ở Feature Branch).")

def check_low_stock():
    print(">> Chức năng cảnh báo sắp hết hàng (sẽ phát triển ở Feature Branch).")


def main():
    while True:
        print("\n=== QUẢN LÝ KHO HÀNG ===")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            check_low_stock()
        elif choice == "4":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


if __name__ == "__main__":
    main()
