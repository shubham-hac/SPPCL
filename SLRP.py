#exp 5
def check():
    global ac, c, stk, a, i
    ac = "REDUCE TO E->"
    # stk[15]
    z = 0
    while z < c:
        if stk[z] == '4':
            print(ac + "4")
            stk[z] = 'E'
            stk[z + 1] = '\0'
            stk[z + 2] = '\0'
            print("\n$" + stk + "\t" + a + "$\t")
        z += 1

    z = 0
    while z < c - 2:
        if stk[z] == '2' and stk[z + 1] == 'E' and stk[z + 2] == '2':
            print(ac + "2E2")
            stk[z] = 'E'
            stk[z + 1] = '\0'
            stk[z + 2] = '\0'
            print("\n$" + stk + "\t" + a + "$\t")
            i -= 2
        z += 1

    z = 0
    while z < c - 2:
        if stk[z] == '3' and stk[z + 1] == 'E' and stk[z + 2] == '3':
            print(ac + "3E3")
            stk[z] = 'E'
            stk[z + 1] = '\0'
            stk[z + 2] = '\0'
            print("\n$" + stk + "\t" + a + "$\t")
            i -= 2
        z += 1


def main():
    global a, c, stk, act, i, j
    print("GRAMMAR is -")
    print("E->2E2")
    print("E->3E3")
    print("E->4")
    a = "32423"
    c = len(a)
    act = "SHIFT"
    print("\nstack \t input \t action")
    print("$\t" + a + "$\t\t")
    for i in range(c):
        j = i
        print(act, end="")
        stk += a[j]
        stk += '\0'
        a = a[:j] + a[j+1:] + '\0'
        print("\n$" + stk + "\t" + a + "$\t")
        # check()

    # check()
    if stk == 'E' and stk[1] == '\0':
        print("Accept\n")
    else:
        print("Reject\n")


# Global variables initialization
a = ""
ac = ""
stk = ""
act = ""
i = 0
j = 0
c = 0

# Call the main function
main()
