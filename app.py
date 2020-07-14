from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def postSurveyData():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host='0.0.0.0', port=port)