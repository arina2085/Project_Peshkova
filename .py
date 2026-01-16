def isPolindrome():
    s1 = input("Введите строку: ")
    s2 = s1[::-1]
    s3 = s1.replace(s1, s2)
    s1.upper()
    s3.upper()
    if s1 == s3:
        print("true")
    else:
        print("false")
    
isPolindrome()