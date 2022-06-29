def takestr(a,b):
    if len(a)==len(b):
        print(a,b)
    elif len(a)<len(b):
        print(b)
    elif len(a)>len(b):
        print(a)
takestr("Abhi","Bhim")