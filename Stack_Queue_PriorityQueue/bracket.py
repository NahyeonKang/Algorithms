t = int(input())
dict = {"(":")", "[":"]", "{":"}"}
for i in range(0,t):
    stack = []
    lst = input()
    yesorno = 0
    for i in lst:
        if i in ["(", "[", "{"]:
            stack.append(i)
        else:
            if stack:
                j = stack.pop()
                if i == dict[j]:
                    yesorno = 0
                else:
                    yesorno = 1
                    break
            else:
                yesorno = 1
                break
    if stack:
        yesorno = 1

    if yesorno == 0:
        print('YES')
    else:
        print("NO")





