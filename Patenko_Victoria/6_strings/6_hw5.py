cell_phone = ["+38066", "+38095", "+38050"]


def check_number(li):
    for num in li:
        if num[:6] in cell_phone:
            print(f"This is really phone number: {num}")
        else:
            print(f"This is not a phone number {num}")

check_number(li)