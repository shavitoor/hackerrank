if __name__ == '__main__':
    N = int(input())

    # initialise the list variable
    value_list = []

    # accept the inputs from the user
    for i in range(N):
        # get the command from the user. It will be in String
        input_string = input().split()

        # First element will always be a command to the list
        user_command = str(input_string[0])

        # Use map to convert the 1+ offsets of the list to Integers
        input_string_values = list(map(int, input_string[1:]))

        if user_command == 'insert':
            value_list.insert(input_string_values[0],input_string_values[1])
    
        if user_command == 'print':
            print(value_list, sep='\n')

        if user_command == 'remove':
            value_list.remove(input_string_values[0])

        if user_command == 'append':
            value_list.append(input_string_values[0])

        if user_command == 'sort':
            value_list.sort()
        
        if user_command == 'pop':
            value_list.pop()

        if user_command == 'reverse':
            value_list.reverse()