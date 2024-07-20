from flask import Blueprint, render_template, redirect, url_for, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        return redirect(url_for('main.index'))

    return render_template('login.html')

@main.route('/register-user', methods=['GET', 'POST'])
def register():
    if request.method == "POST":

        return redirect(url_for('main.index'))

    return render_template('register_user.html')

@main.route('/book-page', methods=['GET', 'POST'])
def book_page():
    if request.method == "POST":

        return redirect(url_for('main.index'))

    return render_template('book_page.html')

@main.route('/loan-page', methods=['GET', 'POST'])
def loan_page():
    if request.method == "POST":

        return redirect(url_for('main.index'))

    return render_template('loan_page.html')

@main.route('/deadline-page', methods=['GET', 'POST'])
def deadline_page():
    if request.method == "POST":

        return redirect(url_for('main.index'))

    return render_template('deadline_page.html')

