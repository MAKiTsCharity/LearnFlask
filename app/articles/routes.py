from app.articles import bp
from flask import render_template

@bp.route('/')
def all_articles():
    articles = [
        {'id': 1, 'title': 'This is an example article.', 'content': 'This is an example content.'},
        {'id': 2, 'title': 'This is an example article (again).', 'content': 'This is an example content too!'},
        {'id': 3, 'title': 'This is an example article... yet another one.', 'content': 'This is an example content as well.'},
        ]
    return render_template('article_list.html',articles=articles)