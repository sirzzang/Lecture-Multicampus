# 이렇게 하면? 런타임에러!!!
# 아... 약간근데 뭔가 문제가 있을거같은데 ( -> append 좋다 근데 



# 이것도 3개 맞음.
T = int(input())

for t in range(T):

    checkList = []
    
    myStr = input()  

    for i in range(len(myStr)):
        if myStr[i] == '(':
            checkList.append(myStr[i])
            
        elif myStr[i] == ')':
            checkList.pop()
        
    if len(checkList) != 0:
        print(f"#{t+1} 0")
        break
    else:
        pass

    for i in range(len(myStr)):
        if myStr[i] == '{':
            checkList.append(myStr[i])
            
        elif myStr[i] == '}':
            checkList.pop()
    
    if len(checkList) != 0:
        print(f"#{t+1} 0")
        break
    else:
        print(f"#{t+1} 1")


# 소괄호 없으면?

# T = int(input())


# for t in range(T):

#     checkList = []
    
#     myStr = input()  

#     for i in range(len(myStr)):
#         if myStr[i] == '(':
#             checkList.append(myStr[i])
#         if myStr[i] == ')':
#             checkList.pop()
        
#     if len(checkList) != 0:
#         print(f"#{t+1} 0")
#         break
        
#     else:
#         if myStr[i] == '}':
#             checkList.pop()

#         if myStr[i] == '{':
#             checkList.append(myStr[i])
            
#     if len(checkList) != 0:
#         print(f"#{t+1} 0")
#     else:
#         print(f"#{t+1} 1")