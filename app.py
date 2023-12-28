from flask import Flask, render_template 

import json
import requests


app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme/1"
    response = requests.request("GET", url)

    if response.status_code == 200:
      apiResponse = response.json()
      meme_title = apiResponse['memes'][0]['title']
      meme_img = apiResponse['memes'][0]['preview'][-1]
      return meme_img,meme_title
    else:
      return f'api is not available currently pls try again after some time..',503



@app.route("/")
def home():
  return render_template('home.html')

@app.route("/meme")
def getmeme():
  meme_pic, subreddit = get_meme()

  print(meme_pic, subreddit)

  return render_template("meme_index.html",meme_pic = meme_pic , subreddit = subreddit) 


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=1122, debug=True)

  