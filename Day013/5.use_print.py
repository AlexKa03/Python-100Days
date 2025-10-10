# Original Code:
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# New Code:
# Dellete the line word_per_page = 0, since it was giving warnings
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # Changed == to = to assign the input value to word_per_page, not compare it
total_words = pages * word_per_page

print(f"pages: {pages}") # Added print statements to help debug and see the values of pages and word_per_page
print(f"words per page: {word_per_page}") # Added print statements to help debug and see the values of pages and word_per_page
print(total_words)
