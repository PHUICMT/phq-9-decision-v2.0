from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

from decision import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

print("[INFO] Decision Server is started...")

@app.route('/get-decision', methods=['POST'])
def get_result():
    data = request.get_json()
    # data to dataframe with features
    df = pd.DataFrame(data, index=[0])
    df = initialize_data(df)
    # predict
    result = predict(df)
    # return result
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)