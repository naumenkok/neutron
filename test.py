from random import choice
# # b = "🔴⚪💚|⭐"
# # print(b)

# def empty():
#     return ' +'
# bbb = [[empty()] * 5 for y in range(5)]
# bbb[0][2] = '🔴'
# bbb[2][2] = '⚪'
# resb = '  1 2 3 4 5 '
# for y in range(5):
#     resb += "\n" + f"{y + 1}" + ''.join(map(str, bbb[y])) + f"{y + 1}"
# resb += "\n" + '  1 2 3 4 5 '
# print(resb)

# def testik():
#     a3, b3 = input("Enter 2 koordinats:").split()
#     c = [int(a3) - 1, int(b3) - 1]
#     # b = int(b3) - 1
#     # c = [a, b]
#     print(c)
# testik()


# for i in range(5):
#     inp = input("Enter:").split()
#     if len(inp) == 2:
#         if all(map(lambda c:c.isdigit(), inp)):
#             print(f"правильно")
#         else:
#             print(f'223')    
#     else:
#         print(f'222')

# a = 2%3
# print(a)

# def testiczek(n_o_m):
#     flag = True
#     n_o_m = 0
#     while flag:
        
#         print(n_o_m)
#         modul = n_o_m % 4
#         print(modul)
#         n_o_m += 1 
#         if n_o_m == 5:
#             flag = False


# testiczek(0)

# a = "alo mam"
# b = a.split()
# print(b)

lis_t = [[1, 2], [4, 2], [6, 3], [9, 33]]
[a, b] = choice(lis_t)
print(a, b)