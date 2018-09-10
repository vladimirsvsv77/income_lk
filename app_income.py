from flask import Flask, request, render_template
from flask_cors import CORS
from flask_restful import abort, Api, Resource
from vacancies import Vacancy
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

vac = Vacancy()
vacancies = vac.vacancies


def make_backup(data):
    with open('backup.json', 'w') as outfile:
        json.dump(data, outfile)


def abort_if_vac_doesnt_exist(vac_id):
    if vac_id not in vacancies:
        abort(404, message="Vacancy {} doesn't exist".format(vac_id))


class Vacancy(Resource):
    def get(self, vac_id):
        abort_if_vac_doesnt_exist(vac_id)
        return vacancies[vac_id]

    def put(self, vac_id):
        vacancies[vac_id]['is_active'] = request.form['is_active']
        make_backup(vacancies)
        return 201


class VacList(Resource):
    def get(self):
        return vacancies


class CityList(Resource):
    def post(self):
        return [{'value': i} for i in vac.cities_list]


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


api.add_resource(CityList, '/cities')
api.add_resource(VacList, '/vacancies')
api.add_resource(Vacancy, '/vac/<vac_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2122, debug=True)
