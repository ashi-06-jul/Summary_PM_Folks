import re
from datetime import datetime
import pandas as pd

with open('w.txt', "r", encoding='utf-8') as infile:
    regex_questions = r"[\?+]"
    regex_category = r'(#\w+|#+)'
    regex_links = r'(\Bhttps.+)'
    regex_text = r'(.+)$'
    questions = []
    category = []
    links = []
    text = []
    for line1 in infile:
      if re.search(regex_questions, line1):
        questions.append(re.findall(regex_questions, line1) or "{undefined}") 
with open('w1.txt', "r", encoding='utf-8') as infile:
    for line2 in infile:
      if re.search(regex_category, line2):
        category.append(re.findall(regex_category, line2) or "{undefined}")
with open('w.txt', "r", encoding='utf-8') as infile:
    for line3 in infile:    
      if re.search(regex_links, line3):
        links.append(re.findall(regex_links, line3) or "{undefined}")
with open('w.txt', "r", encoding='utf-8') as infile:
    for line4 in infile:  
      if re.search(regex_text, line4):
        text.append(re.findall(regex_text, line4) or "{undefined}")
    print(questions)
    print(category)
    print(links)
    print(text)

    #print(outputData['sender'])

