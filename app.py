from flask import Flask, request, jsonify
from utils.merged_logic import get_amazon_data

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    asin = data.get("asin")
    return jsonify(get_amazon_data(asin))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
