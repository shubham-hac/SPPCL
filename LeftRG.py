#exp 3
#Shubham Raut
SIZE = 10
def eliminate_left_recursion(production, num):
    for i in range(num):
        print("\nGRAMMAR:", production[i])
        nterminal = production[i][0]
        if nterminal == production[i][3]:
            alpha = production[i][4:]
            print(" is left recursive.")
            index = 3
            while production[i][index] != 0 and production[i][index] != '|':
                index += 1
            if production[i][index] != 0:
                beta = production[i][index + 1:]
                print("Grammar without left recursion:")
                print(nterminal, "->", beta, nterminal)
                print(nterminal, "\'->", alpha, nterminal, "\'|E")
            else:
                print(" can't be reduced")
        else:
            print(" is not left recursive.")

num = int(input("Enter Number of Production: "))
production = [0] * 10
print("Enter the grammar:")
for i in range(num):
    production[i] = input()
eliminate_left_recursion(production, num)