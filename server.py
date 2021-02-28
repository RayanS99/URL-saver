from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'URL ' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urls', methods=['GET', 'POST'])
def urls():

    if request.method == 'POST':
        url_title = request.form['title']
        url_content = request.form['content']
        new_url = URL(title=url_title, content=url_content)
        db.session.add(new_url)
        db.session.commit()
        return redirect('/urls')
    else:
        all_urls = URL.query.all()
        return render_template('urls.html', urls=all_urls)

@app.route('/urls/delete/<int:id>')
def delete(id):
    url = URL.query.get_or_404(id)
    db.session.delete(url)
    db.session.commit()
    return redirect('/urls')

@app.route('/urls/new', methods=['GET', 'POST'])
def new_url():
    if request.method == 'POST':
        url.title = request.form['title']
        url.content = request.form['content']
        new_url = URL(title=url_title, content=url_content)
        db.session.add(new_url)
        db.session.commit()
        return redirect('/urls')
    else:
        return render_template('new_urls.html')

if __name__ == "__main__":
    app.run(debug=True)