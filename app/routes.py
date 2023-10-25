# app/routes.py
from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import JobSearchForm
from app.selenium_bot import search_jobs

@app.route("/", methods=['GET', 'POST'])
def home():
    form = JobSearchForm()
    if form.validate_on_submit():
        keywords = form.keywords.data
        location = form.location.data
        search_jobs(keywords, location)
        flash(f'Jobs searched for {keywords} in {location}', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)
