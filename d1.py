import re
from datetime import datetime
import pandas as pd

with open('w.txt', "r", encoding='utf-8') as infile:
    regex_questions = r"[?]"
    regex_category = r'(#\w+|#+)'
    regex_links = r'(\Bhttps|\bhttps|\Ahttps)'
    regex_text = r'(\s[^:]*?)$'
    questions = []
    category = []
    links = []
    text = []
    for line in infile:
      if re.search(regex_questions, line):
        questions.append(re.findall(regex_questions, line) or "{undefined}")
      elif re.search(regex_category, line):
        category.append(re.findall(regex_category, line) or "{undefined}")
      elif re.search(regex_links, line):
        links.append(re.findall(regex_links, line) or "{undefined}")
      elif re.search(regex_text, line):
        text.append(re.findall(regex_text, line) or "{undefined}")
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

   # outputData = pd.DataFrame(questions,category,links,text)
    #outputData.to_json('output.json',indent=4)
    print(questions)
    print(category)
    print(links)
    print(text)

    #print(outputData['sender'])

