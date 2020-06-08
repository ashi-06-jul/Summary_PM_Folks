import re
from datetime import datetime
import pandas as pd

with open('w.txt', "r", encoding='utf-8') as infile:
    outputData = { 'date': [], 'sender': [],'category': [], 'text': [] }
    for line in infile:
        matches = re.match(r'^(\d{1,2})\/(\d{1,2})\/(\d\d), (24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]) - ((\S[^:]*?): )?(.*)$', line)
        categ=re.search("^(#)\w$",line)
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
          outputData['category'].append(categ or "{undefined}")
          outputData['text'].append(matches.group(7))

        elif len(outputData['text']) > 0:
          outputData['text'][-1] += "\n" + line[0:-1]

    outputData = pd.DataFrame(outputData)
    outputData.to_csv('output.csv', index=False, line_terminator='\n', encoding='utf-8')
    print(outputData['sender'])

file = open ("w.txt",'r')
regex=r"#[a-b][A-B]"
f = file.readlines()
for s in f:
    sender=s.split(' ')
    print(sender[4])
