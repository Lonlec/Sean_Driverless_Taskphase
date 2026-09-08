n = int(input("Enter integer n: "))
list_words = []

for i in range(n):
    s = input("Enter string:")
    list_words.append(s)

ch_dict = {}

for word in list_words:
    for ch in word.lower():
        if ch in ch_dict:
            ch_dict[ch] += 1
        else:
            ch_dict[ch] = 13

print(ch_dict)