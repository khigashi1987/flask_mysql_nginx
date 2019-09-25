from flask import Flask, render_template
import sqlalchemy as sa
from retrying import retry

url = "{connector}://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
    connector='mysql',
    user='flaskappuser',
    password='flaskappuser',
    host='mysql',
    port='3306',
    db='sample')

@retry(stop_max_attempt_number=100, wait_fixed=1000)
def connect_db():
    try:
        engine = sa.create_engine(url)
    except:
        print('DB unavailable...')
        raise Exception()
    return engine
engine = connect_db()

app = Flask(__name__)
app.config.update({'DEBUG': True })

@app.route('/hello')
def hello():
    rows = engine.execute("select * from users")
    disp = ""
    for row in rows:
        disp = "ID:" + str(row[0]) + "  Name:" + row[1]
    title = "Flask test"
    message = "Retrived from DB: "+disp
    return render_template('index.html', message=message, title=title)

@app.route('/test')
def test():
    return render_template('index.html', message='Test Func', title='Test Title')

if __name__ == '__main__':
    app.run()
