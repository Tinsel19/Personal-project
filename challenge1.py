
Array = []
Output = []
count = 0
list_num = int(input("Enter number of list elements : "))
target = int(input(f"Enter target integer: "))


for i in range(list_num):
	list_item = int(input(f"Enter list item { str(i+1)}: "))
	Array.append(list_item)


Len = len(Array)

for i in Array:
	for j in range(Len):
		if (i + Array[j]) == target:
			Output.append(Array.index(i))
			Output.append(Array.index(Array[j]))

print(Output)