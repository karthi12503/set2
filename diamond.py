rows = int(input("enter the size of diamond :"))
for i in range(1,rows+1):
    s = "  " * (rows - i) + "* " * (2 * i -1)
    print(s)
for i in range(rows-1,0,-1):
    s = "  " * (rows - i) + "* " * (2 * i -1)
    print(s)
