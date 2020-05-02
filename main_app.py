from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('main.html', title='Главная')


@app.route("/about")
def about():
    return render_template('about.html', title='О сайте')


@app.route("/types_of_expertises")
def experts():
    return render_template('experts.html', title='Виды экспертиз')


@app.route("/types_of_expertises/identificial")
def identif():
    return render_template('identif.html', title='Идентификационная экспертиза')


@app.route("/types_of_expertises/threat")
def threat():
    return render_template('threat.html', title='Дела об угрозе')


@app.route("/types_of_expertises/protect_honor")
def protect():
    return render_template('protect.html', title='Защита чести и достоинства')


@app.route("/types_of_expertises/author")
def author():
    return render_template('author.html', title='Автороведческая экспертиза')


@app.route("/news")
def news():
    return render_template('news.html', title='Новости')


@app.route("/types_of_expertises/abuse")
def abuse():
    return render_template('abuse.html', title='Оскробление')


@app.route("/library")
def biblio():
    return render_template('biblio.html', title='Библиотека')


@app.route("/contacts")
def contacts():
    return render_template('cont.html', title='Контакты')


@app.route("/types_of_expertises/corruption")
def corrupt():
    return render_template('corrupt.html', title='Антикоррупционные дела')


@app.route("/types_of_expertises/diagnostical")
def diagn():
    return render_template('diagn.html', title='Диагностическая экспертиза')


@app.route("/types_of_expertises/extremism")
def extremism():
    return render_template('extremism.html', title='Экстремизм')


if __name__ == '__main__':
    app.run(debug=True)
