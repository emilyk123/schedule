from flask import Flask, render_template
import requests

app = Flask(__name__)
url = 'http://api.myanimelist.net/v2/anime?q=Jinrui wa Suitai Shimashita&limit=1'
CLIENT_ID = 'e5d250c0329096077f8e575b3323833b'

@app.route('/')
def index():
    response = requests.get(url, headers = {
        'X-MAL-CLIENT-ID': CLIENT_ID
        })
    response.raise_for_status()
    anime = response.json()
    response.close()

    return render_template('index.html', anime=anime['data'][0]['node']['title'])

if __name__ == '__main__':
    app.run()