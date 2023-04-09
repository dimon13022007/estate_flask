from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return '<Article %r>' % self.id




@app.route('/')
def comingsoon():
    return render_template('index.html')


@app.route('/contacts')
def contacts():

    return render_template('contacts.html')


@app.route('/ff')
def kkt():
    return render_template("main_page.html")


@app.route('/house1')
def house_1():
    return render_template('first_house.html')


@app.route('/house2')
def house_2():
    return render_template('second_house.html')


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.text).all()
    return render_template('posts.html', articles=articles)


@app.route('/house3')
def house_3():
    return render_template('third_house.html')

@app.route('/house4')
def house_4():
    return render_template('4_house.html')


@app.route('/house5')
def house_5():
    return render_template('5_house.html')


@app.route('/house6')
def house_6():
    return render_template('6_house.html')


@app.route('/for_us')
def for_us():
    return render_template('for_us.html')


@app.route('/advertisement', methods=['POST', 'GET'])
def add_advertisement():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']



        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return 'error'

    else:
        return render_template('advertisement.html')




if __name__ == "__main__":
    app.run(debug=True)












