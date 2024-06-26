from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads
import os



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myshop.db'
app.config['SECRET_KEY'] = 'navasmuller6152'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
# patch_request_class(app) 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes
from shop.products import routes
from shop.carts import carts