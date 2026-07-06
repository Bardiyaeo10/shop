# فروشگاه ساده

# مشخصات محصولات
mouse_price = 150000
mouse_stock = 5

keyboard_price = 300000
keyboard_stock = 3

headset_price = 400000
headset_stock = 2

cart = 0   # تعداد کالاهای سبد
total = 0  # مجموع هزینه

while True:
    print("\n--- منوی فروشگاه ---")
    print("1) خرید ماوس")
    print("2) خرید کیبورد")
    print("3) خرید هدست")
    print("4) نمایش مجموع خرید")
    print("0) خروج")

    choice = input("انتخاب شما: ")

    if choice == "1":
        if mouse_stock > 0:
            mouse_stock -= 1
            total += mouse_price
            cart += 1
            print("یک ماوس به سبد اضافه شد.")
        else:
            print("ماوس تمام شده!")

    elif choice == "2":
        if keyboard_stock > 0:
            keyboard_stock -= 1
            total += keyboard_price
            cart += 1
            print("یک کیبورد به سبد اضافه شد.")
        else:
            print("کیبورد تمام شده!")

    elif choice == "3":
        if headset_stock > 0:
            headset_stock -= 1
            total += headset_price
            cart += 1
            print("یک هدست به سبد اضافه شد.")
        else:
            print("هدست تمام شده!")

    elif choice == "4":
        print("\n--- گزارش خرید ---")
        print("تعداد کالا:", cart)
        print("جمع کل:", total, "تومان")

    elif choice == "0":
        print("خروج از برنامه...")
        break

    else:
        print("گزینه نامعتبر!")
