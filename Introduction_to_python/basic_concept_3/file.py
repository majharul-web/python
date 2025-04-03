# csv: comma separated values
# json: javascript object notation

# with open('message.txt', 'w') as file:
#    file.write('Hello World!')


# with open('message.txt', 'a') as file:
#    file.write('Hello World!')


with open('message.txt', 'r') as file:
    content = file.read()
    print(content)