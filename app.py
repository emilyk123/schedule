from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class add_anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Anime %r>' % self.id

url = 'http://api.myanimelist.net/v2/anime?q=Jinrui wa Suitai Shimashita&limit=1'
CLIENT_ID = 'e5d250c0329096077f8e575b3323833b'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add/anime', methods=['POST', 'GET'])
def anime():
    if request.method == 'POST':
        anime_name = request.form['content']
        new_anime = add_anime(content=anime_name)

        db.session.add(new_anime)
        db.session.commit()
        return redirect('/add/anime')

    else:
        anime_list = add_anime.query.order_by(add_anime.date_created).all()
        return render_template('anime.html', anime_list=anime_list)

    # response = requests.get(url, headers = {
    #     'X-MAL-CLIENT-ID': CLIENT_ID
    #     })
    # response.raise_for_status()
    # anime = response.json()
    # response.close()

    # return render_template('anime.html', anime=anime['data'][0]['node']['title'])

if __name__ == '__main__':
    app.run()