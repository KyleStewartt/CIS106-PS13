numItems = int(input("Enter the number of items in the list: "))
myList = []
for i in range(numItems):
    item = int(input(f"Enter integer {i+1}: "))
    myList.append(item)
print("List:", myList)
myList.insert(1, 99)
print("List after inserting 99 at position 1:", myList)
index99 = myList.index(99)
myList[index99] = 100
print("List after replacing 99 with 100:", myList)
secondList = [500, 600, 700, 800, 900]
print("Second list:", secondList)
myList.extend(secondList)
print("First list after extending:", myList)
myList.remove(800)
print("First list after removing 800:", myList)
del myList[2]
print("First list after removing the third item:", myList)
grades = ["A", "B", "C", "A", "A", "C"]
print("Number of A grades:", grades.count("A"))
print("Index of the first B grade:", grades.index("B"))
if "F" in grades:
    print("F grade found in the list.")
else:
    print("F grade not found in the list.")
secondList.clear()
print("Second list after clearing:", secondList)
del secondList
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
players.sort()
print("Sorted players:", players)
players2 = players.copy()
players2.reverse()
print("Players:", players)
print("Reversed players2:", players2)