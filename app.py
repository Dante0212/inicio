from flask import Flask, render_template
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT NOW()')  # ejemplo simple
    current_time = cur.fetchone()[0]
    cur.close()
    conn.close()
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
