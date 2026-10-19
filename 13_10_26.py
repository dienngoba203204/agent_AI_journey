gia0 = 2800
gia1 = 3000
gia2 = 3500
gia3 = 4000
muc1 = 10
muc2 = 30
muc3 = 50
def input_data():
    while True:
        try:
            n = float(input("Số điện tháng này: "))
            if n < 0:
                print("Bạn đã nhập sai (số nhỏ hơn 0), vui lòng nhập lại...")
                continue
            print("Nhập thành công!")
            return n
        except ValueError:
            print("Bạn đã nhập sai định dạng, vui lòng nhập lại...")
def calculate(n):
    if n < muc1:
        tong_tien = n*gia0
    elif n < muc2:
        tong_tien = 10*gia0+(n-10)*gia1
    elif n < muc3:
        tong_tien = 10*gia0+20*gia1+(n-30)*gia2
    else:
        tong_tien = 10*gia0+20*gia1+20*gia2+(n-50)*gia3

    print("Số tiền bạn phải đóng trong tháng này: ", tong_tien, "VNĐ")

if __name__ == '__main__':
    so_dien = input_data()
    calculate(so_dien)
