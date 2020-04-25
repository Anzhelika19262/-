from flask import Flask, render_template
from data import db_session, jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.sqlite")


@app.route("/")
def work_log():
    session = db_session.create_session()
    log = session.query(jobs.Jobs).all()
    return render_template("work_log.html", logs=log)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
