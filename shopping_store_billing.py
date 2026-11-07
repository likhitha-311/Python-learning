customer_name = input("Enter the customer name: ")
product_name = input("Enter the product name: ")
product_price = float(input("Enter the product price: "))
quantity = int(input("Enter quantity: "))

subtotal = product_price * quantity
discount = subtotal * 0.10
final_amount = subtotal - discount

print("\n===.===.=== CUSTOMER BILL ===.===.===")
print("Customer Name :", customer_name)
print("Product       :", product_name)
print("Price         :", product_price)
print("Quantity      :", quantity)
print("-----------------------------------")
print("Subtotal      :", round(subtotal, 2))
print("Discount      :", round(discount, 2))
print("Final Amount  :", round(final_amount, 2))
print("===.====.===.====.===.===.====.===.===")
