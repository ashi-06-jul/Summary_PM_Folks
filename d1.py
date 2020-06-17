import re
from datetime import datetime
import pandas as pd

with open('dummy.txt', "r", encoding='utf-8') as infile:
    outputData = { 'date': [], 'sender': [],'questions':[], 'category': [],'links':[], 'text': [] }
    for line in infile:
        matches = re.findall(r'^(\d{1,2})\/(\d{1,2})\/(\d\d), (24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9]), ((\S[^:]*?): )?(.*), ("[?]"), (("#\w+")("#+")), (("\Bhttps")("\bhttps")("\Ahttps")), ((\S[^:]*?): )?(.*)$', line)
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
          outputData['questions'].append(matches.group(7) or "{undefined}")
          outputData['category'].append(matches.group(8) or "{undefined}")
          outputData['links'].append(matches.group(9) or "{undefined}")
          outputData['text'].append(matches.group(10))

        elif len(outputData['text']) > 0:
          outputData['text'][-1] += "\n" + line[0:-1]

    outputData = pd.DataFrame(outputData)
    outputData.to_json('output.json',indent=6)
    #print(outputData['sender'])

