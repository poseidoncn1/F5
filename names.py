from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        continue
    last = input("please give me last name:")
    if last =='q':
        break

    formatted_name = get_formatted_name(first,last)
    print("\nNeatly formatted name:" + formatted_name + '.')
