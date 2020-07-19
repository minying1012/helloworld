from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, reqparse, Api
import os

class getSurveyData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', required=False)
    parser.add_argument('zip', required=False)
    parser.add_argument('yc', required=False)
    parser.add_argument('nc', required=False)

    def get(self):
        try:
            args = postSurveyData.parser.parse_args()
            print(args)
            return {'result': "Success"}, 200
        except Exception as e:
            return {'error': str(e)}

class postSurveyData(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True)
    parser.add_argument('surveyResult', type=list, location='json', required=True)
    parser.add_argument('location', type=str, required=True)

    def post(self):
        try:
            args = postSurveyData.parser.parse_args()
            surveryList = args['surveyResult']
            surveyYesSum = 0
            for item in surveryList:
                if item == 1:
                    surveyYesSum += 1
                elif isinstance(item, int) == False:
                    return {'error': 'surveyResult only allowed integer type'}, 400
                elif item != 0 & item != 1:
                    return {'error': 'surveyResult allowed only 1 and 0 value'}, 400
            percent = surveyYesSum/len(surveryList)*100
            
            return {'precent': str(int(percent))}, 200
        except Exception as e:
            return {'error': str(e)}

app = Flask(__name__)
api = Api(app)
api.add_resource(postSurveyData, '/api/postSurveyData')
api.add_resource(getSurveyData, '/api/getSurveyData')

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True, host='0.0.0.0', port=port)