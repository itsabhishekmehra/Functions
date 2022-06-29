def testspeed(speed):
    if speed<=70:
        print("Normal speed")
    elif speed >70:
        a = speed-70
        lst=[]
        for i in range(0,a):
            if i%5==0:
                lst.append(i)
        if len(lst)>11:
            print("“License suspended”")
        else:
            print(len(lst))
testspeed(85)          
testspeed(135)