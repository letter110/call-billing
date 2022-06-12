import sqlite3
from flask import Flask
from flask_restful import Api,  Resource, abort, reqparse
from math import ceil


app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('database.db', check_same_thread=False)

data_put_args = reqparse.RequestParser()
data_put_args.add_argument(
    'call_duration', type=int, required=True)


def getUser_names():
    c = conn.cursor()

    c.execute(f"SELECT * FROM mobie")
    user_names = set(c.fetchall())

    conn.commit()
    c.close()
    return user_names


def abort_if_name_not_exist(user_name):
    user_names = getUser_names()
    if user_name not in user_names:
        abort(404, message="not find")
    return


class Call(Resource):
    def put(self, user_name):
        args = data_put_args.parse_args()
        call_duration = args["call_duration"]

        c = conn.cursor()
        c.execute(f"INSERT INTO mobie values('{user_name}',{call_duration})")

        conn.commit()
        c.close()

        return 'PUTED', 201


class Billing(Resource):
    def get(self, user_name):
        abort_if_name_not_exist(user_name)
        c = conn.cursor()

        c.execute(f"SELECT * FROM mobie WHERE use_name='{user_name}'")
        data = c.fetchall()
        call_durations = [i[1] for i in data]
        call_count = sum(call_durations)
        block_count = sum([ceil(i / 30000)for i in call_durations])

        conn.commit()
        c.close()

        return {'call_count': call_count, 'block_count': block_count}


api.add_resource(Call, "/mobie/<string:user_name>/call")
api.add_resource(Billing, "/mobie/<string:user_name>/billing")


if __name__ == '__main__':
    app.run(debug=True)
