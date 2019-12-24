'''1. Create function `has_permission` that get `name` of page.
Inside has_permission function write `inner` function that check access
to this page by `username` of user. Print result to console.'''

def has_permission (page_name):
    def chek_access ():
        access_list = [("page1", "Neo"), ("page1", "Andy"), ("page2", "Leo"), ("page3", "Neo")]
        for a_l in  access_list:
            if a_l[0] == page_name:
                print(f"For page={page_name} have access={a_l[1]}")
    chek_access()
#Test
has_permission("page2")