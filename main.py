import pyinputplus


def check_password(password: str):
    with open('passwords.text', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_passwords in enumerate(common_passwords, start=1):
        if password == common_passwords:
            print(f'{password}: Match Found (#{i})')
        return

    print(f'{password}: Match Not Found')


def main():
    user_password: str = pyinputplus.inputStr('Enter Password: ')
    check_password(user_password)


if __name__ == '__main__':
    main()
