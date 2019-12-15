def list_of_words(w_list):
    len_list = []
    enter_list = w_list.split(', ')
    for word in enter_list:
        len_list.append(len(word))
    print(f"Your list looks like: {len_list}")


w_list = input("Enter your words: ")
list_of_words(w_list)