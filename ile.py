from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup
from pyrogram.enums import ParseMode
import requests,uvloop
import os, random, string


#from flask import Flask,request
#server=Flask(__name__)
def download_file(url, save_path):
  try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
      # Open a file for binary write and save the content
      with open(save_path, 'wb') as file:
        file.write(response.content)
      print(f"File downloaded and saved as {save_path}")
    else:
      print(f"Failed to download file. Status code: {response.status_code}")
  except Exception as e:
    print(f"An error occurred: {str(e)}")


api_id = 12930802
api_hash = "e28ec8094a5779645abcacef029a785c"
bot_token = "6565017763:AAGHHrGGxoQEIiINjzwsJh16rOJRN0S6EjQ"
uvloop.install()
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
#app.set_parse_mode(ParseMode.MARKDOWN)
keyboar = [[InlineKeyboardButton("PROGRAMMER", url="https://t.me/dev_fury")]]
buttons = InlineKeyboardMarkup(keyboar)


async def custom_progress(
    current,
    total,
):
  progress_percentage = (current / total) * 100
  if not progress_percentage == 100:
    progress_message = f"**Uploading: {progress_percentage:.2f}%**"
    cat_i = open("ID.txt", "r").read()
    ind = str(cat_i).splitlines()[0]
    messi = str(cat_i).splitlines()[1]
    await app.edit_message_text(ind,
                                int(messi),
                                str(progress_message),
                                reply_markup=buttons)
  else:
    cat_id = open("ID.txt", "r").read()
    d = str(cat_id).splitlines()[0]
    essi = str(cat_id).splitlines()[1]
    await app.delete_messages(d, int(essi))


@app.on_message(filters.command("start"))
async def Start(client, mes):
  await app.send_message(
      mes.chat.id,
      "**Hi,Im Jafar!\nIm Here To Assist with porting your files from The Web to Telegram\nAll you have to do is send /download_file command with the url\n\nExample:/download_file https://My-File.com/file.zip**",
      reply_markup=buttons)


@app.on_message(filters.command("download_file"))
async def send_file(client, mess):
  await app.send_message(mess.chat.id, "**Wait For The File To Be Downloaded**")
  url = str(mess.text).split("download_file")[1]
  #name = mess.text[int(str(mess.text).rfind("/")) + 1:]
  characters = string.ascii_letters + string.digits
  name = ''.join(random.choice(characters) for _ in range(7))
  name = f"{name}{mess.text[str(mess.text).rfind('.'):]}"
  print(name)
  download_file(url, name)
  pro = await app.send_message(mess.chat.id, "**Uploading : 0%**")
  with open("ID.txt", "w") as IDo:
    IDo.write(f"{str(mess.chat.id)}\n{pro.id}")
  await app.send_document(mess.chat.id, name, progress=custom_progress)
  await app.send_message(mess.chat.id,
                         "**File Sent successfuly**",
                         reply_markup=buttons)


app.set_parse_mode(ParseMode.MARKDOWN)
app.run()
