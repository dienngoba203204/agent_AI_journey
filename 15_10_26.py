
base_product = [
    {"code": "IC", "quantity": 200},
    {"code": "Diode", "quantity": 50},
    {"code": "Transistor", "quantity": 30},
    {"code": "Fet", "quantity": 150},
    {"code": "Nikel", "quantity": 70},
]

def check_product(list_prd):
    found = False
    for prd in list_prd:
        print(f"{prd['code']}: {prd['quantity']}")

def print_code_under_threshold(list_prd, threshold):
    found = False
    for prd in list_prd:
        if prd["quantity"] < threshold:
            print(f"Product {prd['code']} has {prd['quantity']}")
            found = True
    if not found:
        print("No products are running low")

def append_product(list_prd, code, quantity):
    for prd in list_prd:
        if prd["code"] == code:
            prd["quantity"] += quantity
            print("The product already exists in list!")
            return
    list_prd.append({"code": code, "quantity": quantity})
    print("Appened product successfully!")

def remove_product(list_prd, code):
    found = False
    for prd in list_prd:
        if prd["code"] == code:
            list_prd.remove(prd)
            print("Removed product successfully!")
            found = True
            return
    if not found:
        print(f'{code} does not exist in list!')


if __name__ == "__main__":
    while True:
        menu = ("What order do you want to order? \n"
                      "A: Check list \n"
                      "B: Check which products are running low based on predefined thresholds \n"
                      "C: Append product \n"
                      "D: Remove product \n"
                      "Q: Quit \n"
                      "What is your choice?: ")
        order = input(menu).lower().strip().upper()
        if order == "A":
            check_product(base_product)
        elif order == "B":
            try:
                thrs_hld = int(input("Enter a threshold of quantity: "))
                print_code_under_threshold(base_product, thrs_hld)
            except ValueError:
                print("Quantity must be an integer greater than 0")
        elif order == "C":
            prd_code = str(input("Enter a product code: "))
            try:
                prd_quantity = int(input("Enter a quantity: "))
                if prd_quantity <= 0:
                    print("Please enter a number greater than 0")
                    continue
                append_product(base_product, prd_code, prd_quantity)
                check_product(base_product)
            except ValueError:
                print("Quantity must be an integer")
        elif order == "D":
            remove_prd = str(input("What product do you want to remove? "))
            remove_product(base_product, remove_prd)
            check_product(base_product)
        elif order == "Q":
            break
        else:
            print("Please enter a valid option A, B, C, D or Q")