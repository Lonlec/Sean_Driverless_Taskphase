class Selection_Sort_Binary_Search():
    def Selection_Sort(self, mylist):
        n = len(mylist)
        for i in range(n):
            min_ind = i
            for j in range (i+1, n):
                if mylist[min_ind] > mylist[j]:
                    min_ind = j
            mylist[i], mylist[min_ind] = mylist[min_ind], mylist[i]
        print (mylist)
        return(mylist)

    def Binary_Search(self, search, search_list):
        lower = 0
        upper = len(search_list) - 1
        flag = 0
        while lower <= upper:
            mid = lower + (upper - lower)//2

            if search_list[mid]==search:
                print("Found: ", search_list[mid], "at", mid)
                flag+=1
                break
            elif search_list[mid]<search:
                lower = mid + 1
            elif search_list[mid]>search:
                upper = mid  -1

        if flag == 0:
            print("Not in list")

n = int(input("Enter integer n: "))
string_list = []

for i in range(n):
    s = input("Enter string:")
    string_list.append(s)

obj = Selection_Sort_Binary_Search()
obj.Selection_Sort(string_list)

search_input = input("Enter the String : ")
obj.Binary_Search(search_input, string_list)print("Main branch edit")
