""" Go-Links Webapp """
from flask import Flask, request, render_template, redirect, url_for, flash, current_app as app
from sqlalchemy import desc, asc
from golinks.models import DB, Settings


@app.route('/settings')
def settings():
    return render_template(
        'settings.html',
        all_settings=Settings.query.order_by(Settings.name.asc()).all())


@app.route('/settings/submit/', methods=['POST'])
def settings_submit():
    name = request.form.get('name')
    status = request.form.get('status')

    setting = Settings.query.filter_by(name=name).first()
    if status == "True":
        setting.status = False
    else:
        setting.status = True

    DB.session.add(setting)
    DB.session.commit()

    flash("Setting '{.name}' is now '{}'".format(setting, setting.status))

    return redirect(url_for('.settings'))