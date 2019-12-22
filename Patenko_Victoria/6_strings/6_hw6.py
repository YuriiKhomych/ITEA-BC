emails = ["1@gmail.com", "2@ukr.net", "3@mail.ru"]


def email_domains(my_emails):
    import re
    my_email_string = ','.join(emails)
    print(my_email_string)
    my_domains = re.findall(r'@\w+\.\w+|@\w+\.\w+\.\w+', my_email_string)
    print(my_domains)


email_domains(emails)