# declare result as a list globally
result = []


# Function to process the string and split it into substrings
def process_string(S):
    global result
    count = 0
    str = ""


    for c in S:
        str += c
        if c == 'L':
            count += 1
        elif c == 'R':
            count -= 1


        if count == 0:
            result.append(str)
            str = ""


    return result


# Function to output the result
def output_result(result):
    print(len(result))
    for substr in result:
        print(substr)


# Input and function calls
S = input()  
result = process_string(S)
output_result(result)