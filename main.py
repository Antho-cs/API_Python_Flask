from flask import Flask, Response, render_template, jsonify, request, redirect
from Table import *
from conf import app
import uuid

db.create_all()


@app.route('/')
def index():
    # Query all data and then pass it to the template
    user = User.query.all()
    return render_template("index.html", user=user)


@app.route('/add_data')
def add_data():
    return render_template('crea_user.html')


@app.route('/crea_user', methods=["POST"])
def creation_user():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    user = User(uuid.uuid4(), first_name, last_name, email)

    db.session.add(user)
    db.session.commit()

    return redirect('/')


@app.route('/update_user/<id>', methods=["POST"])
def update_user(id):
    user = User.query.get(id)

    print(user)
    new_first_name = request.form.get("first_name")
    new_last_name = request.form.get("last_name")
    new_email = request.form.get("email")

    if len(new_first_name) != 0:
        print("First name présent" + new_first_name)
        user.set_first_name(new_first_name)

    if len(new_last_name) != 0:
        print("Last name présent" + new_last_name)
        user.set_last_name(new_last_name)

    if len(new_email) != 0:
        print("Email présent" + new_email)
        user.set_email(new_email)

    db.session.add(user)
    db.session.commit()

    return redirect('/')


@app.route('/delete/<id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/')


@app.route('/user/<id>')
def user_profile(id):
    user = User.query.get(id)
    # Cherche les amis suivant l'id utilisateur
    friends = Friends.query.filter_by(user_id=id).all()
    amis = []
    for f in friends:
        ami = User.query.get(f.user_friend_id)
        amis.append(ami)

    return render_template("user_page.html", user=user, amis=amis)

if __name__ == "__main__":
    app.run(load_dotenv=True, port=os.getenv('PORT'), debug=(bool(strtobool(os.getenv('DEBUG')))))


