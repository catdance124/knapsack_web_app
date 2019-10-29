# coding: utf-8
from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
df = pd.read_csv('items.csv', encoding="shift-jis")
print(df)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/human")
def index():
    items = []
    for index, row in df.iterrows():
        items.append({'id':row['id'], 'name':row['name'], 'weight':row['weight'], 'capacity':row['capacity'], 'value':row['value']})
    return render_template('index.html', items=items)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')