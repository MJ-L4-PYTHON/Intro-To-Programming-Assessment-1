prompt = "\nEnter desired topping:"
prompt += "\nEnter 'quit' when you are finished"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f" I'll add {topping} to your pizza.")

    else:
        break