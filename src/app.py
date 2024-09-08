import json
from os import environ
from flask import Flask, request, jsonify

app = Flask(__name__)

records = [{
    "name" : "iraitz",
    "email" : "iraitz@thebridge.com"
}]

@app.route('/')
def index():
    return jsonify({'message':"Hello buddies! Welcome to Flask + Docker. Lets Rock and Roll"})

# Búsqueda de todos los usuarios. http://localhost:5000/user/all
@app.route('/user/all', methods=['GET'])
def all_records():
    return jsonify(records)


# Búsqueda por nombre. http://localhost:5000/user?name="alejandru"
@app.route('/user', methods=['GET'])
def query_records():
    name = request.args.get('name')

    for record in records:
        if record['name'] == name:
            return jsonify(record)

    return jsonify({'error': 'data not found'})

# Editar usuario
@app.route('/user', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    records.append(record)
    return jsonify(record)

# Crear usuario
# POST http://localhost:5000/user
#
#{
#  "name": "muchelle",
#  "email": "muchelle@gmail.com"
#}

@app.route('/user', methods=['POST'])
def update_record():
    record = json.loads(request.data)

    index = -1
    for idx, record2 in enumerate(records):
        if record['name'] == record2['name']:
            index = idx

    if index < 0:
        return jsonify({"error" : "record not found"})

    records[idx] = record

    return jsonify(record)

# Borrar usuario
# POST http://localhost:5000/user
#
#{
#  "name": "miguel",
#  "email": "miguel@gmail.com"
#}

@app.route('/user', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)

    for idx, r in enumerate(records):  # noqa: F823
        if r['name'] == record['name']:
            del records[idx]

    return jsonify(record)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port=environ.get("PORT", 5000))
