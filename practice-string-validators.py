if __name__ == '__main__':
    s = input()

    # define the flag variables for all 5 conditions
    # assume all are False initially
    condition1, condition2, condition3, condition4, condition5 = False, False, False, False, False

    # begin the loop and iterate thru all the letters in the string
    for letter in s:
        # In the first line, print True if has any alphanumeric characters. Otherwise, print False. 
        if condition1 == False and letter.isalnum():
            condition1 = True
        
        # In the second line, print True if has any alphabetical characters. Otherwise, print False. 
        if condition2 == False and letter.isalpha():
            condition2 = True
        
        # In the third line, print True if has any digits. Otherwise, print False. 
        if condition3 == False and letter.isdigit():
            condition3 = True

        # In the fourth line, print True if has any lowercase characters. Otherwise, print False. 
        if condition4 == False and letter.islower():
            condition4 = True
        
        # In the fifth line, print True if has any uppercase characters. Otherwise, print False.
        if condition5 == False and letter.isupper():
            condition5 = True
        
    # output the flags
    print(condition1, condition2, condition3, condition4, condition5, sep='\n')
    