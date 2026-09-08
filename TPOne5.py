big_list = [[] for i in range(10)]
#big_list=[[],[],[],[],[],[],[],[],[],[]]

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
        num = int(input("Enter number: "))
        index = num%10
        big_list[index].append(num)

for i in range(10):
    print(f"Sublist {i}: ", big_list[i])