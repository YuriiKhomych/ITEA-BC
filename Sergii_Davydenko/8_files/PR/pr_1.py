
# Write a version of a palindrome recogniser that accepts a file name from
# the sys.argv, reads each line, and prints the line to the screen if it is a
# palindrome and write results to file like {source_name } /{result}.

# Update With


with open('palindrom.txt', 'r') as palindrom:
      print([word for word in (line.strip() for line in ((palindrom)
      .read().lower().split())) if word == word[::-1]])
