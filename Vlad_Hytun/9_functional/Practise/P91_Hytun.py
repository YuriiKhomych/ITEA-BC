# 1. Create function `has_permission` that get `name` of page.
# # Inside has_permission function write `inner` function that check access
# # to this page by `username` of user. Print result to console.

def has_permition():
    name_page = 'Main page'
    print(name_page)

    def inner_func():
        try:
            name_page = 'Change name'
        except Exception as error:
            print(f'You cannot change page name')

    inner_func()
    print(name_page)

has_permition()