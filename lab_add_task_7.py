array = [int(input()) for _ in range(4)] + list("_")

print(*array)

number, position = int(input()), int(input())
new_array = array[:position]
new_array.append(number)
new_array.extend(array[position:len(array) - 1])

print(*new_array)