import re
from datetime import datetime
import pandas as pd

with open('w.txt', "r", encoding='utf-8') as infile:
    outputData = { 'date': [], 'sender': [],'questions':[], 'category': [],'links':[], 'text': [] }
    for line in infile:
      if re.search ("[?]", line):
        outputData['questions'].append(re.findall ("[?]", line) or "{undefined}")
      elif re.search ("#\w+", line) or re.search("#+", line):
        outputData['category'].append(re.findall ("#\w+", line) or re.findall("#+", line) or "{undefined}")
      elif re.search("\Bhttps", line) or re.search("\bhttps", line) or re.search("\Ahttps", line):
        outputData['links'].append(re.findall("\Bhttps", line) or re.findall("\bhttps", line) or re.findall ("\Ahttps", line) or "{undefined}")

        #matches = re.match(r'^(\d{1,2})\/(\d{1,2})\/(\d\d), (24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]), ((\S[^:]*?): )?(.*), ("[?]"), (("#\w+")("#+")), (("\Bhttps")("\bhttps")("\Ahttps")), ((\S[^:]*?): )?(.*)$', line)
        #if matches:
         # outputData['date'].append(
          #  datetime(
           #   int(matches.group(3))+2000,
            #  int(matches.group(1)),
             # int(matches.group(2)),
              #hour=int(matches.group(4)[0:2]),
             # minute=int(matches.group(4)[3:])
            #))
          #outputData['sender'].append(matches.group(6) or "{undefined}")
          #outputData['questions'].append(matches.group(7) or "{undefined}")
          #outputData['category'].append(matches.group(8) or "{undefined}")
          #outputData['links'].append(matches.group(9) or "{undefined}")
          #outputData['text'].append(matches.group(10) or "{undefined}")

        #elif len(outputData['text']) > 0:
         # outputData['text'][-1] += "\n" + line[0:-1]

    outputData = pd.DataFrame(outputData)
    outputData.to_json('output.json',indent=6)
    #print(outputData['sender'])

