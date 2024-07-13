from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


df = pd.read_csv('data.csv')

@app.route('/get-data', methods=['POST'])
def get_data():
    data = request.get_json()
    user_id = data['id']
    result = df[df['id'] == int(user_id)].to_dict(orient='records')
    if result:
        return jsonify(result=result[0])
    else:
        return jsonify(result='ID not found')

if __name__ == '__main__':
    app.run(port=8000)