break_statment = '/end'
input_string = ''
input_text = ''
while input_string != break_statment:
    print("Input somthing: ")
    input_string = input()
    if input_string != break_statment:
        input_string = input_string.__add__('.').capitalize()
        input_text = input_text.__add__(input_string)
        print(input_text)
