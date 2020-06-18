from telegram.ext import Updater, CommandHandler

def callback_alarm(bot, job):
    bot.send_message(chat_id=job.context, text='Alarm')
    #bot.send_message(chat_id='1076770159', text='Wait for some min')

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
