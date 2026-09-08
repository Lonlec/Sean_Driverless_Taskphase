class SelectionSort():
    def selection_sort(self, words):
        for i in range(len(words)-1):
            min_index = i
            for j in range(i + 1, len(words)):
                if words[j] < words[min_index]:
                    min_index = j         
            words[i], words[min_index] = words[min_index], words[i]
        print (words)

list_words=[]
n = int(input("Enter number of words you want to enter: "))

for i in range(n):
    s = input("Enter string:")
    list_words.append(s)

sorter = SelectionSort()
sorter.selection_sort(list_words)