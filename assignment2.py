users = {
    "admin":   {"password": "admin124", "role": "Admin"},
    "cashier": {"password": "pass124",  "role": "Cashier"},
    "buyer":   {"password": "buy123",   "role": "Customer"},
}

print("--- Welcome to the E-Commerce Platform ---")
username = input("Enter Username: ")
password = input("Enter Password: ")

access_level = ""

if username in users and users[username]["password"] == password:
    access_level = users[username]["role"]
    print(f"\nLogin Successful! Welcome, {access_level}.")
else:
    print("\nInvalid Username or Password. Access Denied.")

if access_level != "":


    if access_level == "Admin":
        print("[Admin Feature] System Status: Healthy. No errors reported.")
        print("[Admin Feature] Total Sales Today: $1,240.50")
        print("------------------------------------------")

    print(f"Proceeding to Checkout System as {access_level}...")

    subtotal = float(input("Enter the product subtotal amount: $"))
    coupon = input("Enter coupon code (Leave blank if none): ").upper()
    location = input("Enter your location (e.g., Kikoni, KK, Bwaise): ").upper()

    discount_rate = 0.0
    tax_rate = 0.0

    if coupon == "SAVE10":
        print("Coupon 'SAVE10' applied successfully!")
        if subtotal >= 100:
            discount_rate = 0.15
        else:
            discount_rate = 0.10

    elif coupon == "WELCOME5":
        print("Coupon 'WELCOME5' applied successfully!")
        discount_rate = 0.05

    elif coupon == "":
        print("No coupon entered.")
        if subtotal >= 200:
            print("Automatic loyalty discount applied!")
            discount_rate = 0.08
        else:
            discount_rate = 0.0
    else:
        print("Invalid coupon code entered. No discount applied.")
        if subtotal >= 200:
            print("However, you still qualify for our automatic spending discount!")
            discount_rate = 0.08
        else:
            discount_rate = 0.0

    if location == "KIKONI":
        tax_rate = 0.08
    elif location == "KK":
        tax_rate = 0.09
    elif location == "BWAISE":
        tax_rate = 0.06
    else:
        print(f"Location '{location}' matches standard base tax.")
        if subtotal > 500:
            tax_rate = 0.05
        else:
            tax_rate = 0.07

    discount_amount = subtotal * discount_rate
    price_after_discount = subtotal - discount_amount
    tax_amount = price_after_discount * tax_rate
    final_price = price_after_discount + tax_amount

    print("\n============ FINAL RECEIPT ============")
    print(f"User Access Role : {access_level}")
    print(f"Subtotal         : ${subtotal:.2f}")
    print(f"Discount Applied : -${discount_amount:.2f} ({discount_rate * 100}%)")
    print(f"Tax Applied      : +${tax_amount:.2f} ({tax_rate * 100}% via {location})")
    print("---------------------------------------")
    print(f"FINAL PRICE      : ${final_price:.2f}")
    print("=======================================")
