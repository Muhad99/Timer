from flask import Flask, flash, abort, render_template, Response, request
from datetime import datetime
from flask_bootstrap import Bootstrap
import time


app = Flask(__name__)

bootstrap = Bootstrap(app)



@app.route('/')
def index():
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    return render_template('index.html', date_time=date_time)
     
           
    
    


if __name__ == '__main__':
 app.run(debug=True)