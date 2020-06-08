print ("Hello World")
print("Please enter the term (with #):")
find = input()
with open("simple.txt", "r") as f:       
    words = list(map(str.strip, f.readlines()))
    try: 
        text=words[words.index(find) + 1]
        print(text)
    except:
        print("Sorry the word is not found.")
        print ("Hello World")
print("Please enter the term (with #):")
find = input()
with open("simple.txt", "r") as f:       
    words = list(map(str.strip, f.readlines()))
    try: 
        text=words[words.index(find) + 1]
        print(text)
    except:
        print("Sorry the word is not found.")