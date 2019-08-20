# import の実行
from flask import Flask, jsonify, request,render_template
import json
import input_data
import matplotlib.pyplot as plt

# インスタンスの作成
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

lunches = json.loads(input_data.past_lunches)

# URL, Methodと関数の紐づけ
@app.route('/lunches')
def get_dataall():

    # 配列作成
    dates = []
    costs = []

    plt.cla()
    
    # 配列格納
    for data in lunches['results']:
        dates.append(data['date'])
        costs.append(int(data['cost']))
    x= range(len(costs))
    
    print(dates) 
    print(costs) 

    # ラベル
    plt.title("lunches")
    plt.xlabel("date")
    plt.ylabel("cost")

    # グリッド線を表示するならTrue
    plt.grid(True)

    # グラフ作成
    plt.plot(x,costs, marker="o", color = "red", linestyle = "--")
    plt.xticks(x,dates)
    plt.savefig('static/images/sample.png')
    
    return render_template('image.html', filename='/static/images/sample.png') 
    
@app.route('/lunches', methods=['POST'])
def make_list():
    newdata = request.get_json()
    lunches['results'].append(newdata)
    return jsonify(lunches)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# サーバの起動
if __name__ == '__main__':
    app.run()
