def isHappy(n: int) -> bool:
    s = set()
    while n > 0:
        n_str = str(n)
        temp = 0
        for i in n_str:
            temp += int(i) ** 2

        if temp == 1:
            return("True")
            break
        if temp in s:
            return("False")
            break
        else:
            s.add(temp)
        n = temp
#isHappy(1)
#isHappy(19)
isHappy(2)