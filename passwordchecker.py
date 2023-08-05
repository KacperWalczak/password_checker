import requests
import sys
import hashlib


def request_api_for_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching:{res.status_code}, check api.')
    return res


def count_leaks(passwords, password_to_check):
    passwords = (line.split(':') for line in passwords.text.splitlines())
    for h, count in passwords:
        if h == password_to_check:
            return count
    return 0


def is_password_pwned(password):
    password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5, tail = password_sha1[:5], password_sha1[5:]
    pwned_passwords = request_api_for_data(first_5)
    return count_leaks(pwned_passwords, tail)


def main(args):
    for password in args:
        count = is_password_pwned(password)
        if int(count) > 1:
            print(f'{password} has been pawned {count} times. CHANGE YOUR PASSWORD!!!')
        elif int(count) == 1:
            print(f'{password} has been pawned {count} time. CHANGE YOUR PASSWORD!!!')
        else:
            print(f'{password} has been NOT been found!')


def flatten(lst):
    return [elem for sublist in lst for elem in sublist]


def read_password_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]
        return flatten(lines)


if __name__ == '__main__':
    try:
        main(read_password_from_file(sys.argv[1]))
    except FileNotFoundError:
        print(f"No such file or directory: {sys.argv[1]} !!!")



