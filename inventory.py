# QUẢN LÝ KHO HÀNG - MAIN FILE
products = []   #Mỗi sản phẩm sau này sẽ là dict
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

## Nhap hang
# Biến toàn cục
products = []
def add_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)
    print(f"Đã thêm sản phẩm: {name} - Giá: {price} - SL: {quantity}")

## Xem ton kho
def view_inventory():
    if not products:
        print("Kho hiện đang trống.")
        return

    print("\n--- DANH SÁCH TỒN KHO ---")
    for item in products:
        print(f"{item['name']} - Giá: {item['price']} - SL: {item['qty']}")

## Canh bao het hang
def check_low_stock():
    print("\n--- CẢNH BÁO SẮP HẾT HÀNG ---")

    found = False
    for item in products:
        if item['qty'] < 5:
            print(f"⚠ {item['name']} - Chỉ còn {item['qty']} sản phẩm!")
            found = True
    if not found:
        print(" Không có sản phẩm nào sắp hết hàng.")
