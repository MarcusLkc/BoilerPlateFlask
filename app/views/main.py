from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)

# created rout at index of website then render the index.html tempalte


@main.route('/')
def index():
	return render_template('index.html')
