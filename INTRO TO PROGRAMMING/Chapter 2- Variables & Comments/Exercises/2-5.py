# usb price and girl's budget
usb_price = 6
budget = 50

# calculate how many USB sticks she can purchase
usb_purchased = budget/usb_price

# calculate how many pounds will she have left
change = budget%usb_price

# display results
print(f"She can buy {usb_purchased} USB sticks")
print(f"She will have £{change} left.")

