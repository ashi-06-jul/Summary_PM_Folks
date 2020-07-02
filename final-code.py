import re
from datetime import datetime
import pandas as pd
import json
from iteration_utilities import duplicates
with open('pm1.txt', "r", encoding='utf-8') as infile:
    outputData = { 'date': [], 'sender': [], 'text': [] }
    for line in infile:
        matches = re.match(r'^(\d{1,2})\/(\d{1,2})\/(\d?\d?\d\d), (24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]) - ((\S[^:]*?): )?(.*)$', line)
        if matches:
          try:
            outputData['date'].append(
              datetime(
                int(matches.group(3))+2000,
                int(matches.group(1)),
                int(matches.group(2)),
                hour=int(matches.group(4)[0:2]),
                minute=int(matches.group(4)[3:])
              ))
          except:
            outputData['date'].append(' ')
          try:
            outputData['sender'].append(matches.group(6) or "{undefined}")
          except:
            outputData['sender'].append(' ')
          try:
            outputData['text'].append(matches.group(7) or "{undefined}")
          except IndexError: 
            outputData['text'].append(" ")
        elif len(outputData['text']) > 0:
          outputData['text'][-1] += "\n" + line[0:-1]
    outputData = pd.DataFrame(outputData)
    outputData.to_json('output.json',indent=3)
regex_category = r'(#\w+|#+)'
regex_links = r'^https?.+|\bhttps?.+'
category=[]
links=[]
Repeat=[]
summary=[['links']]
NoRepeat=[]
def filter_data(x):
    size_x=len(x)
    for (k,v) in x.items():
        if re.search(regex_category, v):
            category.append(re.findall(regex_category, v))
        if re.search(regex_links, v):
            links.append(re.findall(regex_links, v))
            summary.append(re.findall(regex_links, v))

    return category
def Repeat_noRepeat(x):
  size=len(x)
  for i in range(size):
    k=i+1
    for j in range(k, size): 
      if x[i] == x[j] and x[i] not in Repeat: 
            Repeat.append(x[i]) 
            summary.append(x[i])
            summary.append(outputData['sender'][i])
            summary.append(outputData['text'][i])
      elif x[i] not in summary:
            summary.append(x[i])
          #  summary.append(outputData['sender'][i])
           # summary.append(outputData['text'][i])
      else:
            continue
p=filter_data(outputData['text'])
Repeat_noRepeat(category)
#print(category)
#print(links)
#print(summary)
print('\n'.join(map(str, summary)))
print(Repeat)