from pyrogram import Client, filters
import requests
import os
#from flask import Flask,request
#server=Flask(__name__)
def download_file(url, save_path):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("now")
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

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
@app.on_message(filters.command("start"))
async def Start(client,mes):
	await app.send_message(mes.chat.id,"Hello")
@app.on_message()
async def send_file(client,mess):
	await app.send_message(mess.chat.id,"Wait please")
	name=mess.text[int(str(mess.text).rfind("/"))+1:]
	download_file(mess.text,name)
	await app.send_message(mess.chat.id,"Wait please \n progress:0")
	await app.send_document(mess.chat.id,name,
	progress=app.send_message(mess.chat.id,))
app.run()