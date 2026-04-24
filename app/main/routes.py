from app.main import bp
from flask import render_template
from datetime import datetime
from zoneinfo import ZoneInfo

@bp.route('/')
def home():
    return render_template('home.html')

timezones = {
    "UTC": "UTC",
    "New York (US Eastern)": "America/New_York",
    "Los Angeles (US Pacific)": "America/Los_Angeles",
    "London (UK)": "Europe/London",
    "Berlin (Central Europe)": "Europe/Berlin",
    "Moscow": "Europe/Moscow",
    "Dubai": "Asia/Dubai",
    "Mumbai (India)": "Asia/Kolkata",
    "Beijing (China)": "Asia/Shanghai",
    "Tokyo (Japan)": "Asia/Tokyo",
    "Sydney (Australia)": "Australia/Sydney",
    "São Paulo (Brazil)": "America/Sao_Paulo",
}

@bp.route('/clock')
def clock():
    timezone_ids = [tz for name, tz in timezones.items()]
    timezone_names = [name for name, tz in timezones.items()]
    current_times = [datetime.now(ZoneInfo(tz)).isoformat() for tz_name, tz in timezones.items()]
    return render_template('clock.html', times=lambda: zip(timezone_ids,timezone_names,current_times))
