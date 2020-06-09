import re
from datetime import datetime
import pandas as pd
import json
from iteration_utilities import duplicates

with open('w.txt', "r", encoding='utf-8') as infile:
    outputData = { 'date': [], 'sender': [],'category': [], 'text': [] }
    for line in infile:
        matches = re.match(r'^(\d{1,2})\/(\d{1,2})\/(\d\d), (24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]) - ((\S[^:]*?): )?(.*)$', line)
        if matches:
          outputData['date'].append(
            datetime(
              int(matches.group(3))+2000,
              int(matches.group(1)),
              int(matches.group(2)),
              hour=int(matches.group(4)[0:2]),
              minute=int(matches.group(4)[3:])
            ))
          outputData['sender'].append(matches.group(6) or "{undefined}")
          outputData['category'].append(matches.group(7).split(' ')[0] or "{undefined}")
          outputData['text'].append(matches.group(7).split(' ', 1)[1])

        elif len(outputData['text']) > 0:
          outputData['text'][-1] += "\n" + line[0:-1]
   
    outputData = pd.DataFrame(outputData)
    outputData.to_json('output.json',indent=4)
    
    #for key in outputData['category'].keys(): 
     #   print(key)
print('Scrolling through Whatsapp groups are a painful task. Let us give you a brief summary of what all happened on your PM Community group this week. ')
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
                print(x[i])
                for i in range(_size):
                  if x[i] == x[j]:
                    print(outputData['text'][i])
                  else:
                    continue
    return repeated 
p=Repeat(outputData['category'])
#print(p)
for (k,v) in outputData['category'].items():
    if v not in p:
      print(outputData['category'][k])
      print(outputData['text'][k])

  #  for (k, v) in outputData['category'].items():
  #   print("Key: " + str(k))
  #  print("Value: " + str(v))
           
     #outputData = pd.DataFrame(outputData)
    #outputData.to_json('output.json',indent=4)
    #file = open ("w.txt",'r')
    #f = file.readlines()
    #d=str(f)
    #dict_json=json.loads(d)
   # print(type(dict_json))    

#for i in outputData['category']:
 #   dict_json=json.loads(i)
  #  print(dict_json)
  


    #file = open ("w.txt",'r')
    #f = file.readlines()
    #d=str(f)
    #data=json.loads(d)
    #print(type(data))
    #for i in outputData['category']:
    #   print(outputData['text'])
      
 #file = open ("w.txt",'r')
  #  regex=r"#[a-b][A-B]"  
   # f = file.readlines()
    #for s in f:
     # category=s.split(' ')
      #print(category)
   # print('''Scrolling through Whatsapp groups are a painful task. 
#Let us give you a brief summary of what all happened on your PM Community group this week. 
#''')
 #   for i in outputData['sender']:
    #for i in category:
     # if i==i+1:
      #  for j in outputData['text']:
       #     print(i +':' +j)
      #else:
       # for j in outputData['text']:
        #  print(i+':'+j)