from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_num():
    num = request.form['num']
    return jsonify(num*2)


if __name__ == '__main__':
    app.run(debug=True)