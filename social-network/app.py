from flask import request, Flask, render_template, jsonify
from db_layer import DbLayer

app = Flask(__name__)


db = DbLayer()
@app.route('/', methods=['GET'])
def hello():
    return {}


@app.route('/users', methods=['GET'])
def get_all_users():
    result = db.get_all_users()

    return jsonify(result)

@app.route('/users', methods=['POST'])
def register_user():
    name = request.form['name']
    age = request.form['age']
    location = request.form['location']
    interests = request.form['interests']

    result = db.register_user(name, age, location, interests)

    return jsonify(result)


@app.route('/update/<username>', methods=['POST'])
def update_user(username):
    age = request.form['age']
    location = request.form['location']
    interests = request.form['interests']

    result = db.update_user(username, age, location, interests)

    return jsonify(result)


@app.route('/posts', methods=['POST'])
def create_post():
    title = request.form['title']
    detail = request.form['detail']

    result = db.create_post(title, detail)

    return jsonify(result)


@app.route('/posts/<post_title>/like', methods=['POST'])
def like_post(post_title):
    user_name = request.form['user_name']

    result = db.like_post(user_name, post_title)

    return jsonify(result)


@app.route('/users/<sender_name>/request_friend/<receiver_name>', methods=['POST'])
def send_friend_reqeust(sender_name, receiver_name):

    result = db.send_friend_request(sender_name, receiver_name)

    return jsonify(result)

@app.route('/users/<user_name>/get_all_friend_requests', methods=['GET'])
def get_all_friend_requests(user_name):
    result = db.see_incoming_requests(user_name)

    return jsonify(result)

@app.route('/users/<user_name>/accept_friend_request', methods=['POST'])
def accept_friend_request(user_name):
    friend_name = request.json['requester_name']

    result = db.accept_request(user_name, friend_name)

    return jsonify(result)

@app.route('/users/<user_name>/unfriend/<friend_name>', methods=['DELETE'])
def unfriend(user_name, friend_name):
    result = db.unfriend(user_name, friend_name)

    return result

@app.route('/users/find_user', methods=['GET'])
def find_user():
    name = request.args.get('name')

    if name is None:
        return jsonify({'error': 'name is required.'})
    
    result = db.find_user_by_name(name)
    return result


@app.route('/users/<user_name>/recommendations')
def recommendations(user_name):
    result = db.recommend_friends(user_name)
    
    return result
