while True:
    temp = input("Enter temp and unit: ")
    split_temp = temp.split()

    if len(split_temp) != 2:
        print("write number")
        continue

    t = split_temp[0]
    u = split_temp[1]

    try:
        t = float(t)
    except:
        print("this is not a number")
        continue

    if u == "C" or u == "c":
        f = (t * 9/5) + 32
        print("Fahrenheit:", f)
        break
    elif u == "F" or u == "f":
        c = (t - 32) * 5/9
        print("Celsius:", c)
        break
    else:
        print("try agine")