#!/usr/bin/env python
""" Go-Links Webapp """
from flask import Flask, request, render_template, redirect, url_for, flash, current_app as app
from sqlalchemy import desc, asc
from sqlalchemy.sql import or_
from golinks.models import DB, GoRecord
from golinks import utils

@app.route('/')
def index():
    """ Base page """
    return render_template(
        'index.html',
        all_records=GoRecord.query.order_by(GoRecord.name.asc()).all()
    )


@app.route('/golinks/delete/<name>/')
def golink_delete(name):
    """ Used to delete gorecords """
    record = GoRecord.query.filter_by(name=name).first()
    DB.session.delete(record)
    DB.session.commit()

    flash("Successfully deleted '{.name}'".format(record))

    return redirect(url_for('.index'))


@app.route('/<name>', methods=['GET', 'POST'])
@app.route('/<name> <optional_argument>', methods=['GET', 'POST'])
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


@app.route('/golinks/edit/<name>/', methods=['GET'])
def golink_edit(name):
    """ Used to edit GoRecords """
    record = GoRecord.query.filter_by(name=name).first_or_404()

    return render_template(
        'index.html',
        edit_record=record, 
        all_records=GoRecord.query.order_by(GoRecord.name.asc()).all()
    )


@app.route('/golinks/search/', methods=['POST'])
def golink_search_redirect_post():
    """ Used to Rediect a POST search to a GET """
    search = request.form.get('searchinput')
    if not search:
        return redirect(url_for('.index'))

    return redirect(url_for('golink_search', search=search))


@app.route('/golinks/search/<search>/', methods=['GET'])
def golink_search(search):
    """ Used to Search for a GoRecord """
    search_like = '%{}%'.format(search)
    search_q = GoRecord.query.filter(or_(
        GoRecord.name.like(search_like),
        GoRecord.url.like(search_like),
    ))

    all_records = search_q.all()

    return render_template(
        'index.html',
        all_records=all_records,
        previous_search_text=search
    )


@app.route('/golinks/submit/', methods=['POST'])
def golink_submit():
    """ Used to Create or Edit a GoRecord """
    gid = request.form.get('gid')
    name = request.form.get('name')
    url = request.form.get('url')
    favicon = request.form.get('ffav')

    if not utils.url_checker(url):
        flash("Incorrect URL format: '{}'".format(url))
        return redirect(url_for('.index')) 

    if not utils.url_checker(favicon):
        flash("Adjusting Favicon URL - either empty or incorrect format: '{}'".format(favicon))
        favicon = utils.faviconer(url)

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
        record = GoRecord(name, url, favicon)
        flash("Successfully created '{.name}'".format(record))

    DB.session.add(record)
    DB.session.commit()

    return redirect(url_for('.index'))