s=raw_input("please enter a word")
upper_s = s.upper()
print(upper_s)
lower_s = s.lower()
print(lower_s)

combined = upper_s + lower_s

print(combined)

num_s = len(s)
print(num_s)
num_combined = len(combined)
print(num_combined)


halfway = len(s)/2
print(s[halfway])
print("at s[0]")
print(s[0])
last = len(s) - 1
print(s[last])
print(s[-1])

firsthalf = s[0:halfway]
lasthalf = s[halfway:last+1]
print(firsthalf)
print(lasthalf)

copy = s[:]

skip =  s[1::2]
print(skip)

value = s[:len(s)/2:-1]
print(value)

print(s.find("e"))
print(s[:s.find("e")])

replaced = s.replace("great","awesome")
print(replaced)

skip = s[1::2]
print(skip)

#value = a[len(s):halfway:-1]
#print(value)
words = s.split()
numerofwords = len(words)
print(words[0:2])
print(words[0:2:-1])
print(words[0:2:-1])
print(words[::-1])

sentence = "\n ".join(words)
print(sentence)


newsentence = sentence.replace("\n",":-)")
print(newsentence)







#s.replace("o","o")

#slice
#start,stop,increment

#concat
