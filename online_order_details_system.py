# Online Order Details System

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")

customer_age = int(input("Enter customer age: "))
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

is_paid = True
is_delivered = False

total_price = product_price * quantity

print("\n===.=.=== ORDER DETAILS ===.=.===")
print("Customer Name:", customer_name)
print("Product Name:", product_name)
print("Customer Age:", customer_age)
print("Product Price:", product_price)
print("Quantity:", quantity)
print("Total Price:", round(total_price, 2))
print("Payment Completed:", is_paid)
print("Order Delivered:", is_delivered)

print("\n===.=.=== DATA TYPES ===.=.===")
print("Name:", type(customer_name))
print("Age:", type(customer_age))
print("Price:", type(product_price))
print("Payment:", type(is_paid))
