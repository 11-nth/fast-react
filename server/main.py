import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/users", methods=['GET'])
def users():
    return jsonify(
        {
            'users': [
                'eze',
                'coi',
                'chukoy',
                'chooks',
                'ezekiel'
            ]
        }
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)