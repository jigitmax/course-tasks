import re
def check_password(str_pass):
    lowstr = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
    lowstrpattern = re.compile(lowstr)
    if lowstrpattern.fullmatch(str_pass) == None:
        return 'Password invalid'
    else:
        return 'Password valid'

str1 = input('Password: ')
print(check_password(str1))