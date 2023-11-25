class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


# VALID_DOMAIN = ['.com', '.bg', '.net', '.org'] -> We can use a constant variable.
while True:
    email = input()
    if email == 'End':
        break

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split('@')[0]) <= 4:
        raise NameTooShortError(
            "Name must be more than 4 characters")  # -> We raise it when the name in the email is less than or equal to 4.

    # domain = '.' + email.split('.')[-1] -> If we use a constant variable the code should look like this.
    # if domain not in VALID_DOMAIN:
    #     raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if email.split('.')[-1] != 'com' and email.split('.')[-1] != 'bg' \
            and email.split('.')[-1] != 'org' and email.split('.')[-1] != 'net':
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')

# SECOND OPTION
# class NameTooShortError(Exception):
#     pass
# class MustContainAtSymbolError(Exception):
#     pass
#
# class InvalidDomainError(Exception):
#     pass
#
# email = input()
# VALID_DOMAIN = ['.com', '.bg', '.net', '.org']
#
# while email != 'End':
#     if '@' not in email:
#         raise MustContainAtSymbolError("Email must contain @")
#
#     if len(email.split('@')[0]) <= 4:
#         raise NameTooShortError("Name must be more than 4 characters")
#
#     domain = '.' + email.split('.')[-1]
#     if domain not in VALID_DOMAIN:
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     email = input()
#
#     print('Email is valid')
