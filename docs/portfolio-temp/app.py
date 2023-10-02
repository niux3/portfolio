from time import time
from flask import Flask, render_template
from csv import DictWriter
from pathlib import Path
from sqlalchemy import MetaData, create_engine, Table


app = Flask(__name__)


@app.route('/')
def index():
    ROOT = Path(__file__).resolve().parent
    DB_SQLITE = ROOT / 'data' / 'data-dev.db'
    meta = MetaData()
    engine = create_engine(f'sqlite:///{DB_SQLITE}')
    meta.reflect(bind=engine)
    connect = engine.connect()
    portfolios = Table('portfolios', meta, autoload_with=engine)
    query = portfolios.select()
    data_raw = connect.execute(query).fetchall()[:5]
    data_reverse = data_raw.copy()
    data_reverse.reverse()

    data = data_reverse + data_reverse + data_reverse + data_reverse[:-1] + data_raw + data_raw + data_raw + data_raw
    ctx = {
        'objects_list': data,
        'len_data': len(data_raw),
        'version': time()
    }
    return render_template('home.html', **ctx)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
