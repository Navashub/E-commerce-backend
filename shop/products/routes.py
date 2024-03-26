from flask import redirect, render_template, url_for, flash, request
from shop import db, app
from .models import Brand, Category
from .forms import Addproducts
from sqlalchemy.exc import IntegrityError

import secrets



@app.route('/')
def home():
    return " "



@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        try:
            db.session.commit()
            flash(f'The Brand {getbrand} was added to your database', 'success')
        except IntegrityError:
            db.session.rollback()
            flash(f'The Brand {getbrand} already exists in the database', 'error')
        return redirect(url_for('addbrand'))
        # flash(f'The Brand {getbrand} was added to your database', 'success')
        # db.session.commit()
        # return redirect(url_for('addbrand'))
    
    return render_template('products/addbrand.html', brands='brands')


# @app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
# def updatebrand(id):
#     if 'email' not in session:
#         flash(f'Please login first', 'danger')
#     updatebrand = Brand.query.get_or_404(id)
#     brand = request.form.get('brand')
#     if request.method == 'POST':
#         updatebrand.name = brand
#         flash(f'Your brand has been updated', 'success')
#         db.session.commit()
#         return redirect(url_for('brands'))
#     return render_template('products/updatebrand.html', title='Update brand page', updatebrand=updatebrand)

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    # if 'email' not in session:
    #     flash(f'Please login first', 'danger')
    #     return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('category')
        category = Category(name=getbrand)
        db.session.add(category)
        flash(f'The Category {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    
    return render_template('products/addbrand.html')


# @app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
# def updatecat(id):
#     if 'email' not in session:
#         flash(f'Please login first', 'danger')
#     updatecat = Category.query.get_or_404(id)
#     category = request.form.get('category')
#     if request.method == 'POST':
#         updatecat.name = category
#         flash(f'Your category has been updated', 'success')
#         db.session.commit()
#         return redirect(url_for('category'))
#     return render_template('products/updatebrand.html', title='Update Category page', updatecat=updatecat)

@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title='Add product page', form=form, brands=brands, categories=categories)