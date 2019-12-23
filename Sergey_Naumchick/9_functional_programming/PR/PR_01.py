'''1. Create function `has_permission` that get `name` of page.
Inside has_permission function write `inner` function that check access
to this page by `username` of user. Print result to console.'''
import csv

file_path = "check_permission.csv"


def has_permission():
    while True:
        u_name = input("Please input your login: ")
        u_password = input("Please input your password: ")

        with open(file_path) as file_with_permissions:
            reader = csv.DictReader(file_with_permissions)
            for row in reader:
                if u_name == row["user_name"] and u_password == row["password"]:
                    print("ok")
                    exit()

        print("ERROR check your login or password!, Try again!")


has_permission()
