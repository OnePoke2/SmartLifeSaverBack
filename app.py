# coding: utf-8
from flask import Flask, request, json, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

markers = {
    '1': 'flask start test1',
    '2': 'watching doiken test1'
}

@app.route('/markers', methods=['GET'])
def list_all_markers():
    json = {
        'message': markers
    }
    return jsonify(markers)

@app.route('/markers/<int:markerid>', methods=['GET'])
def marker(markerid):
    markerid = str(markerid)
    json = {
        'message': markers[markerid]
    }
    return jsonify(json)

@app.route('/markers/<int:markerid>', methods=['DELETE'])
def delete_marker(markerid):
    markerid = str(markerid)
    if markerid in markers:
        del markers[markerid]
        msg = 'Marker {} deleted'.format(markerid)
    else:
        msg = '{0} is not in markers.'.format(markerid)
    json = {
        'message': msg
    }
    return jsonify(json)

@app.route('/markers', methods=['POST'])
def create_marker():
    markerid = str(int(max(markers.keys())) + 1)
    posted = request.get_json()
    if 'marker' in posted:
        markers[markerid] = posted['marker']
        msg = 'New marker created'
    else:
        msg = 'No marker created'
    json = {
        'message': msg
    }
    return jsonify(json)

@app.route('/markers/<int:markerid>', methods=['PUT'])
def update_marker(markerid):
    markerid = str(markerid)
    posted = request.get_json()
    if 'marker' in posted and markerid in markers:
        markers[markerid] = posted['marker']
        msg = 'Marker {} updated'.format(markerid)
    else:
        msg = 'No marker updated'
    json = {
        'message': msg
    }
    return jsonify(json)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
