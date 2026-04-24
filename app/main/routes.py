from app.main import bp
from flask import render_template
from datetime import datetime
from zoneinfo import ZoneInfo

@bp.route('/')
def home():
    return render_template('home.html')
