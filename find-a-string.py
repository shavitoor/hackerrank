def count_substring(string, sub_string):
    # count variable to hold the sub string matches
    count = 0

    length_string = len(string)
    length_sub_string = len(sub_string)

    if length_string>=length_sub_string:
        # Sample string's from hackerrank
        # string 1: ABCDCDC
        # sub-string 1: CDC
        #
        # string 2: WoW!ItSCoOWoWW
        # sub-string 2: oW
        for i in range(0,length_string):
            # Define a flag variable to find sub string 
            sub_string_found = True

            if (length_string-i)>=length_sub_string and string[i]==sub_string[0]:
                for j in range(0,length_sub_string):
                    # break the loop and move on the to next character in the main string
                    # if the matching pattern fails
                    if string[i+j]!=sub_string[j]:
                        sub_string_found = False
                        break

                # if the matching pattern if still true, this means we have a match!
                if sub_string_found == True:                
                    count+=1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)