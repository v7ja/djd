try:
 import tambotapi
except:
 import os
 os.system('pip install tambotapi')
 os.system('clear')
 import tambotapi
token = input("- Enter Token : ")
text = input("- Enter Text : ")
bot = tambotapi.TamBot(token)
def main():  
    bot.send_message(text, bot.get_chat_id())
main()
