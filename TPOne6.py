def dist(d, dx, dy):
    return (d[0] - dx) ** 2 + (d[1] - dy) ** 2

def selection_sort(big_list, dx, dy):
    n = len(big_list)

    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if dist(big_list[j], dx, dy) < dist(big_list[min_index], dx, dy):
                min_index = j

        big_list[i], big_list[min_index] = big_list[min_index], big_list[i]

    print(big_list)


x = int(input("Enter the x coordinate reference: "))
y = int(input("Enter the y coordinate reference: "))

n = int(input("How many coordinates do you want to enter? "))
big_list = []

for i in range(n):
    px = int(input("X Coordinate: "))
    py = int(input("Y Coordinate: "))
    big_list.append((px, py))

selection_sort(big_list, x, y)