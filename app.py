# coding: utf-8
from flask import Flask, render_template
import pandas as pd
from settings import weight_limit, capacity_limit

app = Flask(__name__)
df = pd.read_csv('items.csv', encoding="shift-jis")

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/human")
def index():
    items = []
    for index, row in df.iterrows():
        items.append({'id':row['id'], 'name':row['name'], 'weight':row['weight'], 'capacity':row['capacity'], 'value':row['value']})
    return render_template('index.html', items=items, weight_limit=weight_limit, capacity_limit=capacity_limit)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')