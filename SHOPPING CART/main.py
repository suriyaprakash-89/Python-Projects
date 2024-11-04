shopping_cart = []
billing_counter = []
total_amount = 0


def push(item, price):
    shopping_cart.append((item, price))


def pop():
    if shopping_cart:
        removed_item = shopping_cart.pop()
        print(f"Removed {removed_item[0]} from the cart.")
    else:
        print("Your Shopping Cart is Empty")


def enqueue(item, price):
    billing_counter.append((item, price))


def dequeue_cart_display():
    temp_cart = []
    if shopping_cart:
        print("Displaying Shopping Cart:")
        while shopping_cart:
            item, price = shopping_cart.pop()
            temp_cart.append((item, price))
            print(f"{item}: ${price:.2f}")
        shopping_cart.extend(temp_cart)
    else:
        print("Your Shopping Cart is Empty")


while True:
    print(
        "\n1 - Add Items Into Shopping Cart\n2 - Remove Item From Shopping Cart\n3 - Checkout In Billing Counter\n4 - Display Cart\n5 - Exit\n")
    opt = int(input("Choose Options: "))

    if opt == 1:
        n = int(input("Enter Total Number Of Items: "))
        for i in range(n):
            item_i = input(f"Enter Item {i + 1}: ")
            price_i = float(input(f"Enter Price for {item_i}: "))
            push(item_i, price_i)
    elif opt == 2:
        pop()
    elif opt == 3:
        if shopping_cart:
            total_amount = 0
            while shopping_cart:
                item_i, price_i = shopping_cart.pop(0)
                enqueue(item_i, price_i)
                total_amount += price_i
            print("Checkout Summary:")
            for item, price in billing_counter:
                print(f"{item}: ${price:.2f}")
            print(f"Total Amount: ${total_amount:.2f}")
            break
        else:
            print("Your Shopping Cart is Empty")
    elif opt == 4:
        dequeue_cart_display()
    elif opt == 5:
        print("Thanks For Shopping!")
        break
    else:
        print("Enter Valid Command!")
