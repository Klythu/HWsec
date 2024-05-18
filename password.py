import hashlib
hexdigit=""
while hexdigit=="":
    password=input("Введите пароль")
    important=["0","1","2","3","4","5","6","7","8","9"]
    flagnum=0
    flagdif=0
    if len(password)<8:
        print("Минимальная длинна пароля должна составлять 8 символов")
    else:
        sudo=""
        for char in password:
            for num in important:
                if char==num:
                    flagnum=1
            if flagnum==0:
                sudo=sudo+char
            flagnum=0
        if len(sudo)==len(password):
            print("Пароль должен содержать хотябы 1 цифру")
        elif len(sudo)==0:
            print("Пароль должен содержать хотябы 1 букву")
        else:

            if sudo.isupper() or sudo.islower():
                print("пароль должен содержать как заглавные так и строчные буквы")
            else:
                hashpass=hashlib.sha256(password.encode())
                hexdigit=hashpass.hexdigest()
                print(hexdigit)