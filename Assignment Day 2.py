String = input('Enter a String')
# Using Count Method
list1 = []
for ch in String:
    if ch not in list1:
        list1.append(ch)
        print(ch, String.count(ch))


