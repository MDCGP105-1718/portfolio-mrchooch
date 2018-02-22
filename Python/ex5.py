for i in range(99,0,-1):
    if i > 2:
        print("%i bottles of beer on the wall, %i bottles of beer.\nTake one down, pass it around, %i bottles of beer on the wall…" %(i,i,i-1))
    elif i == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall…")
    else:
        print("1 bottle of beer on the wall, 1 bottle of beer!\nSo take it down, pass it around, no more bottles of beer on the wall!")
