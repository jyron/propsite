from app import app, db
from app.models import *
from app.forms import PostForm, cat_list
from flask import render_template, url_for, flash, redirect
import datetime
from random import choice
x = datetime.datetime.now()
date = x





@app.route('/')
@app.route('/home')
def home():
    props=Proposal.query.all()
    return render_template('home.html', title='Frontpage - Prop Site', date=x, props=props)


@app.route('/about')
def about():
    return render_template('about.html', title='About - Prop Site')


@app.route('/proposals')
def proposals():
    return render_template('proposals.html', title='Proposals - Prop Site', date=x)


@app.route('/create-proposal', methods=['GET', 'POST'])
def create_proposal():
    form = PostForm()
    form.category.choices = cat_list
    if form.validate_on_submit():
        prop = Proposal(category = form.category.data, issue=form.issue.data,
                        brief=form.brief.data, solution=form.detail.data)
        db.session.add(prop)
        db.session.commit()
        flash('Your proposal for {} is being reviewed, please allow 1 day for approval'.format(
            form.issue.data))
        return redirect(url_for('home'))

    return render_template('create-proposal.html', title='Create a Proposal - Prop Site', form=form)
