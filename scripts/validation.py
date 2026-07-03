def get_valid_input(prompt, min_length, empty_error, length_error):

    while True:
        value = input(prompt).strip()
        if value == "":
            print(empty_error)
            continue
        
        if len(value) < min_length:
            print(length_error)
            continue
        
        return value
        
