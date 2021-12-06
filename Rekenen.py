listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


def addAndDisplayLists():
    print("List 1 : " + str(listOne))
    print("List 2 : " + str(listTwo))

    res_list = []
    for i in range(0, len(listOne)):
        res_list.append(listOne[i] + listTwo[i])

    print("Resultaat : " + str(res_list))


print(addAndDisplayLists())


def subtractAndDisplayLists():
    print("List 1 : " + str(listOne))
    print("List 2 : " + str(listTwo))

    res_list = []
    for i in range(0, len(listOne)):
        res_list.append(listOne[i] - listTwo[i])

    print("Resultaat : " + str(res_list))


print(subtractAndDisplayLists())


def multiplyAndDisplayLists():
    print("List 1 : " + str(listOne))
    print("List 2 : " + str(listTwo))

    res_list = []
    for i in range(0, len(listOne)):
        res_list.append(listOne[i] * listTwo[i])

    print("Resultaat : " + str(res_list))


print(multiplyAndDisplayLists())


def divideAndDisplayLists():
    print("List 1 : " + str(listOne))
    print("List 2 : " + str(listTwo))

    res_list = []
    for i in range(0, len(listOne)):
        res_list.append(listOne[i] / listTwo[i])

    print("Resultaat : " + str(res_list))


print(divideAndDisplayLists())
