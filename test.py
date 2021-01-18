# # b = "🔴⚪💚|⭐"
# # print(b)

def empty():
    return ' +'
bbb = [[empty()] * 5 for y in range(5)]
bbb[0][2] = '🔴'
bbb[2][2] = '⚪'
resb = '  1 2 3 4 5 '
for y in range(5):
    resb += "\n" + f"{y + 1}" + ''.join(map(str, bbb[y])) + f"{y + 1}"
resb += "\n" + '  1 2 3 4 5 '
print(resb)

def testik():
    a3, b3 = input("Enter 2 koordinats:").split()
    a = int(a3)
    b = int(b3)
    c = a + b
    print(c)
testik()