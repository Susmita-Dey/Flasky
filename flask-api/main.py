# Simple Flask server to test API calls
from flask import Flask, request, jsonify

app = Flask(__name__)

# setup routes for Flask server


@app.route('/')
def home():
    return 'Hello Home!'


@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get('extra')
    if (extra):
        user_data["extra"] = extra

    return jsonify(user_data), 200  # 200 is the status code for OK


@app.route('/get-user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify(data), 201  # 201 is the status code for CREATED


# setup Flask server
if __name__ == '__main__':
    app.run(debug=True)
