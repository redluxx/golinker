#!/usr/bin/env python
""" Go-Links Webapp """
from flask import Flask, request, render_template, redirect, url_for, flash
from sqlalchemy import desc, asc
from sqlalchemy.sql import or_
from golinks.models import DB, GoRecord
from golinks import settings

WEBAPP = Flask(__name__)

WEBAPP.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
WEBAPP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
WEBAPP.secret_key = settings.SECRET_KEY
DB.init_app(WEBAPP)


def render_template_with_settings(template, **kwargs):
    """ Add all the sends when rendering the template """
    return render_template(template, settings=settings, **kwargs)


@WEBAPP.route('/')
def index():
    """ Base page """
    return render_template_with_settings(
        'index.html',
        all_records=GoRecord.query.order_by(GoRecord.name.asc()).all()
    )


@WEBAPP.route('/golinks/delete/<name>/')
def golink_delete(name):
    """ Used to delete gorecords """
    record = GoRecord.query.filter_by(name=name).first()
    DB.session.delete(record)
    DB.session.commit()

    flash("Successfully deleted '{.name}'".format(record))

    return redirect(url_for('.index'))


@WEBAPP.route('/<name>')
@WEBAPP.route('/<name> <optional_argument>')
def redirect_to_link(name, optional_argument=None):
    """ Used to redirect to a GoRecord """
    record = GoRecord.query.filter_by(name=name).first()

    if record is None:
        return redirect(url_for('golink_search', search=name))

    record.visits = record.visits + 1
    DB.session.add(record)
    DB.session.commit()

    link = record.link(optional_argument)
    return redirect(link)


@WEBAPP.route('/golinks/edit/<name>/', methods=['GET'])
def golink_edit(name):
    """ Used to edit GoRecords """
    record = GoRecord.query.filter_by(name=name).first_or_404()

    return render_template_with_settings(
        'index.html',
        edit_record=record, 
        all_records=GoRecord.query.all()
    )


@WEBAPP.route('/golinks/search/', methods=['POST'])
def golink_search_redirect_post():
    """ Used to Rediect a POST search to a GET """
    search = request.form.get('search')
    if not search:
        return redirect(url_for('.index'))

    return redirect(url_for('golink_search', search=search))


@WEBAPP.route('/golinks/search/<search>/', methods=['GET'])
def golink_search(search):
    """ Used to Search for a GoRecord """
    search_like = '%{}%'.format(search)
    search_q = GoRecord.query.filter(or_(
        GoRecord.name.like(search_like),
        GoRecord.url.like(search_like),
    ))

    all_records = search_q.all()

    return render_template_with_settings(
        'index.html',
        all_records=all_records,
        previous_search_text=search
    )


@WEBAPP.route('/golinks/submit/', methods=['POST'])
def golink_submit():
    """ Used to Create or Edit a GoRecord """
    gid = request.form.get('gid')
    name = request.form.get('name')
    url = request.form.get('url')
    favicon = request.form.get('ffav')

    if not GoRecord.url_checker(url):
        flash("Incorrect URL format: '{}'".format(url))
        return redirect(url_for('.index')) 

    if favicon is None or not GoRecord.url_checker(favicon):
        flash("Adjusting Favicon URL - either None or incorrect format: '{}'".format(favicon))
        favicon = GoRecord.faviconer(url)


    record = GoRecord.query.filter_by(gid=gid).first()
    if record:
        oldname = record.name 
        record.name = name
        record.url = url
        record.favicon = favicon
        if name == oldname:
            flash("Successfully updated '{.name}'".format(record))
        else:
            flash("Successfully updated '{}' to '{.name}'".format(oldname, record))
    else:
        record = GoRecord(name, url)
        flash("Successfully created '{.name}'".format(record))

    DB.session.add(record)
    DB.session.commit()

    return redirect(url_for('.index'))


if __name__ == '__main__':

    with WEBAPP.app_context():
        DB.create_all()

        if settings.ADD_DEMO_RECORDS:
            for demo_name, demo_url in settings.DEMO_RECORDS:
                try:
                    DB.session.add(GoRecord(demo_name, demo_url))
                    DB.session.commit()
                except:
                    pass

    WEBAPP.debug = settings.DEBUG
    WEBAPP.port = settings.PORT
    WEBAPP.hostname = settings.HOSTNAME
    WEBAPP.run()
