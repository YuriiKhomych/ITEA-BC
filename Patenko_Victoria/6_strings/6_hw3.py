def filter_long_word(w_list, n):
    for word in w_list.split(', '):
        if len(word) > int(n):
            print(word)


my_w_list = input("Enter your words: ")
my_n = input("Enter your number: ")
filter_long_word(my_w_list, my_n)
