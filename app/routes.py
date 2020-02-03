from app import app, redirect, render_template, url_for, flash, LoginForm

@app.route('/')
def index():
    data = {'username': 'Red'}
    return render_template('index.html', name=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Username {}. Password {}. Remember me {}.'.format(form.username.data, form.password.data,
                                                                 form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
