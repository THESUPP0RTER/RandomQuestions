test = [1, 2, 3, 5, 6, 3, 3, 5, 6, 1, 4, 3, 6 , 4]
def deleteDuplicates(a, n):
    j = 0
    for i in a:
        if i not in a:
            a[++j] = a[i]
    a[++j] = a[n-1]
    return j
length = len(test)
length = deleteDuplicates(test,length)


print("The original list is: " + str(test))
for i in range(length):
    print("The new list is: " + str(test[i]) + " ")

