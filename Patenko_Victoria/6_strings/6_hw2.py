def find_longest_word(w_list):
    print(max([len(i) for i in w_list.split(', ')]))

ent_list = input("Enter your words: ")
find_longest_word(ent_list)


