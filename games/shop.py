items = {
    "apple": 10,
    "banana": 5,
    "milk": 20,
    "bread": 15,
    "eggs": 30
}

balance = 100

while True:
    print("\n" + "="*40)
    print("WELCOME TO THE SHOP")
    print("="*40)
    print("Items available:")
    for idx, (i, price) in enumerate(items.items(), start=1):
        print(f"{idx}. {i.capitalize():10} - ${price}")
    print("-"*40)
    print(f"Your balance: ${balance}")
    print("="*40)

    print("\nOptions:")
    print("1. Buy single item (with quantity)")
    print("2. Add multiple items to cart")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item to buy: ").lower()
        if item in items:
            try:
                qty = int(input("Enter quantity: "))
            except:
                print("Invalid quantity! Defaulting to 1.")
                qty = 1
            total_price = items[item] * qty
            print(f"You want to buy {qty} x {item} for ${total_price}.")
            confirm = input("Confirm purchase? (yes/no): ").lower()
            if confirm == "yes":
                if balance >= total_price:
                    balance -= total_price
                    print(f"Purchase successful! Remaining balance: ${balance}")
                else:
                    print(f"Not enough balance! Your balance: ${balance}")
            else:
                print("Purchase canceled.")
        else:
            print("Item not found!")

    elif choice == "2":
        cart = {}
        total = 0
        while True:
            item = input("Add item to cart (or type 'done' to finish adding): ").lower()
            if item == "done":
                break
            if item in items:
                try:
                    qty = int(input(f"Enter quantity of {item}: "))
                except:
                    print("Invalid quantity! Defaulting to 1.")
                    qty = 1
                if item in cart:
                    cart[item] += qty
                else:
                    cart[item] = qty
                total += items[item] * qty
                print(f"{qty} x {item} added to cart. Cart total so far: ${total}")
            else:
                print("Item not found!")

        if cart:
            print("\nYour cart summary:")
            for k, v in cart.items():
                print(f"{v} x {k} - ${items[k]*v}")
            print(f"Total amount: ${total}")
            confirm = input("Confirm purchase? (yes/no): ").lower()
            if confirm == "yes":
                if total <= balance:
                    balance -= total
                    print(f"Cart purchased successfully! Remaining balance: ${balance}")
                else:
                    print(f"Not enough balance! Your balance: ${balance}")
            else:
                print("Purchase canceled.")

    elif choice == "3":
        print("Thank you for shopping! Goodbye!")
        break

    else:
        print("Invalid choice!")
