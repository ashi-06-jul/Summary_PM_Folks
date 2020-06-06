with open("simple.txt", "r") as f:       
    words = list(map(str.strip, f.readlines()))
    try: 
        text=words[words.index("#hire")+1]
        print(text)
        text=words[words.index("#new_technology")+1]
        print(text)
        text=words[words.index("#good_conversations")+1]
        print(text)
        text=words[words.index("#upcoming_events")+1]
        print(text)
        text=words[words.index("#doubts")+1]
        print(text)
    except:
        print("Sorry the word is not found.")
        print ("Hello World")