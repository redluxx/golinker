""" Go-Links Webapp """
from flask import Flask, request, render_template, redirect, url_for, flash, current_app as app
from sqlalchemy import desc, asc
from golinks.models import DB, Settings


@app.route('/settings')
def settings():
    return render_template(
        'settings.html',
        all_settings=Settings.query.order_by(Settings.name.asc()).all())
