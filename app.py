from flask import Flask, json, jsonify


app = Flask(__name__)

with open('birthdays.json') as f:
    db = json.load(f)


@app.route('/birthday/<int:year>/<int:month>/<int:day>')
def famous_twins(year, month, day):
    return jsonify(body=db.get('%d%d%d' % (year, month, day), []))


if __name__ == '__main__':
    app.run(debug=True)
