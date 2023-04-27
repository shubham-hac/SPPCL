#exp 6
def pm():
    expk_reversed = expk[::-1]
    j = l - 1 - l
    exp1.extend(expk_reversed[:j][::-1])
    exp1.reverse()
    print(f"Three address code:\ntemp={exp1}\ntempl={expk_reversed[j+1]}{expk_reversed[j]}")
def div():
    exp1.extend(expk[:i+2])
    print(f"Three address code:\ntemp={exp1}\ntempl=temp{expk[i+2]}{expk[i+3]}")
def plus():
    exp1.extend(expk[:i+2])
    print(f"Three address code:\ntemp={exp1}\ntempl=temp{expk[i+2]}{expk[i+3]}")
exp1 = []
expk = []
ex = [0] * 10
id1 = [0] * 5
op = [0] * 5
id2 = [0] * 5
addr = 100
while True:
    print("\n1.assignment\n2.arithmetic\n3.relational\n4.Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        expk = input("\nEnter the expression with assignment operator: ")
        l = len(expk)
        expt = []
        i = 0
        while expk[i] != '=':
            i += 1
        expt.extend(expk[:i])
        expk_reversed = expk[::-1]
        exp1 = []
        exp1.extend(expk_reversed[i+1:l][::-1])
        exp1.reverse()
        print(f"Three address code:\ntemp={exp1}\n{expt}=temp")
    elif ch == 2:
        ex = input("\nEnter the expression with arithmetic operator: ")
        expk = list(ex)
        l = len(expk)
        exp1 = []
        for i in range(l):
            if expk[i] == '+' or expk[i] == '-':
                if expk[i+2] == '/' or expk[i+2] == '*':
                    pm()
                    break
                else:
                    plus()
                    break
            elif expk[i] == '/' or expk[i] == '*':
                div()
                break
    elif ch == 3:
        id1 = input("Enter the expression with relational operator: ")
        op = input()
        id2 = input()
        if op == '<' or op == '>' or op == '<=' or op == '>=' or op == '==' or op == '=':
            print(f"\n{addr}\tif {id1}{op}{id2} goto {addr + 3}")
            addr += 1
            print(f"{addr}\tT:=0")
            addr += 1
            print(f"{addr}\tgoto {addr + 2}")
            addr += 1
            print(f"{addr}\tT:=1")
        else:
            print("Expression is error")    
    elif ch == 4:
        break
