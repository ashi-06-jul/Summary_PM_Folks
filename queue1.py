import re
from datetime import datetime
import pandas as pd
import json
from iteration_utilities import duplicates
from telegram.ext import Updater, CommandHandler
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
def callback_alarm(bot, job):
  listt = []
  def noRepeat():
      for (k,v) in outputData['category'].items():
        if v not in p:
            listt.append(outputData['category'][k])
            listt.append(outputData['text'][k])
  def Repeat(x): 
        _size = len(x) 
        repeated = [] 
        for i in range(_size): 
            k = i + 1
            for j in range(k, _size): 
                if x[i] == x[j] and x[i] not in repeated: 
                    repeated.append(x[i]) 
                    listt.append(x[i])
                    for i in range(_size):
                      if x[i] == x[j]:
                        listt.append(outputData['text'][i])
                      else:
                        continue
  return repeated 
  p=Repeat(outputData['category'])
  bot.send_message(chat_id=job.context, text=listt)

def callback_timer(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id,
                      text='Starting!')
    job_queue.run_repeating(callback_alarm, 21600, context=update.message.chat_id)

def stop_timer(bot, update, job_queue):
    bot.send_message(chat_id=update.message.chat_id,
                      text='Stoped!')
    job_queue.stop()

updater = Updater("1184324197:AAFChlWE5tU5X4lzHq-mQHvhxNIYisCqq1U")
updater.dispatcher.add_handler(CommandHandler('start', callback_timer, pass_job_queue=True))
updater.dispatcher.add_handler(CommandHandler('stop', stop_timer, pass_job_queue=True))

updater.start_polling()
