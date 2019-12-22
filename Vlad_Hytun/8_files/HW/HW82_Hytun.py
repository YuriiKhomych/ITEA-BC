# 2. Create program that get [Text](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
# from file, find 5 most popular words and write result to file.
import operator

def most_popular_word():
    with open('HW82_file') as file_obj:
        file_data = file_obj.read()
        words = file_data.split()
        set_words = set(words)
        dict_words = {}
        for word in set_words:
            count_word = 0
            for element in words:
                # count_word = 0
                if word == element:
                    count_word += 1
            dict_words[word] = count_word
    list_dict_words = list(dict_words.items())
    list_dict_words.sort(key=lambda i: i[1], reverse=True)
    print(words)
    print(set_words)
    print(list_dict_words[:5])

most_popular_word()