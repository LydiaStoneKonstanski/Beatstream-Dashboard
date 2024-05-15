# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from .plots import PlotCreator

from ..connections.beatstream_connection import BeatstreamConnection, User, Recommendation
from sqlalchemy import func
beatstream_connection = BeatstreamConnection()
beatstream_session = beatstream_connection.new_session()

plot_creator = PlotCreator()

@blueprint.route('/index')
@login_required
def index():
    total_users = 0 #f"{beatstream_session.query(func.count(User.id)).first()[0]:,}"
    active_users = 0 #f"{beatstream_session.query(func.count(User.id)).filter(User.current_song != "None").first()[0]:,}"

    return render_template('pages/index.html', segment='index', total_users=total_users, active_users=active_users)

@blueprint.route('/typography')
@login_required
def typography():
    return render_template('pages/typography.html')

@blueprint.route('/color')
@login_required
def color():
    return render_template('pages/color.html')

@blueprint.route('/icon-tabler')
@login_required
def icon_tabler():
    return render_template('pages/icon-tabler.html')

@blueprint.route('/neobackground')
def neobackground():
    return render_template('images/neobackground.png')

@blueprint.route('/sample-page')
@login_required
def sample_page():
    bar = plot_creator.create_total_model_score_chart()
    return render_template('pages/sample-page.html', plot=bar)
@blueprint.route('/slide')
@login_required
def slide():
    return render_template('pages/slide.html')

@blueprint.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')

@blueprint.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')

@blueprint.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')

@blueprint.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')

@blueprint.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')

@blueprint.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
