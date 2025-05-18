from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import db, login_manager
from .models import User, Product
from .forms import LoginForm, RegisterForm, ProductForm, EditProfileForm
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    search = request.args.get('search')
    category = request.args.get('category')
    products = Product.query
    if search:
        products = products.filter(Product.title.ilike(f'%{search}%'))
    if category:
        products = products.filter_by(category=category)
    products = products.all()
    return render_template('product_list.html', products=products)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid credentials')
    return render_template('login.html', form=form)

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed = generate_password_hash(form.password.data)
        user = User(email=form.email.data, username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('signup.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = EditProfileForm(username=current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash("Profile updated")
    return render_template('dashboard.html', form=form)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            title=form.title.data,
            category=form.category.data,
            description=form.description.data,
            price=form.price.data,
            image_url=form.image_url.data,
            owner=current_user
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('product_form.html', form=form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    product = Product.query.get_or_404(id)
    if product.owner != current_user:
        return redirect(url_for('main.dashboard'))
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        form.populate_obj(product)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('product_form.html', form=form)

@main.route('/delete/<int:id>')
@login_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    if product.owner == current_user:
        db.session.delete(product)
        db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    return render_template('product_detail.html', product=product)

@main.route('/cart/add/<int:id>')
@login_required
def add_to_cart(id):
    product = Product.query.get_or_404(id)
    current_user.cart.append(product)
    db.session.commit()
    return redirect(url_for('main.view_cart'))

@main.route('/cart')
@login_required
def view_cart():
    return render_template('cart.html', cart=current_user.cart)

@main.route('/cart/remove/<int:id>')
@login_required
def remove_from_cart(id):
    product = Product.query.get_or_404(id)
    current_user.cart.remove(product)
    db.session.commit()
    return redirect(url_for('main.view_cart'))

@main.route('/checkout')
@login_required
def checkout():
    for product in current_user.cart:
        current_user.purchases.append(product)
    current_user.cart.clear()
    db.session.commit()
    flash("Checkout complete!")
    return redirect(url_for('main.previous_purchases'))

@main.route('/previous')
@login_required
def previous_purchases():
    return render_template('previous.html', purchases=current_user.purchases)
