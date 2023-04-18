from flask import Flask, render_template,  request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///konf.db'
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Lerc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.Integer, nullable=False)
    introduction = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Lerc %r>' % self.id


@app.route('/')
def hello():
    return render_template("hell.html")


@app.route('/posts')
def posts():
    articles = Lerc.query.order_by(Lerc.id.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def post_page(id):
    post = Lerc.query.get(id)
    return render_template("post.html", post=post)


@app.route('/posts/<int:id>/war1ace')
def post_delete(id):
    post = Lerc.query.get_or_404(id)

    try:
        db.session.delete(post)
        db.session.commit()
        return redirect('/posts')
    except:
        return "Delete error"


@app.route('/add', methods=['POST', 'GET'])
def add_lecture():
    if request.method == "POST":
        title = request.form['title']
        deadline = request.form['deadline']
        introduction = request.form['introduction']
        text = request.form['text']

        lerc = Lerc(title=title, deadline=deadline, introduction=introduction, text=text)

        try:
            db.session.add(lerc)
            db.session.commit()
            return redirect('/posts')
        except ValueError as e:
            return "Error"
        except FileNotFoundError as e:
            return "Error"
    else:
        return render_template("add_lecture.html")


if __name__ == '__main__':
    app.run()
