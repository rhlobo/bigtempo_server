from ..app import persistence as db, restless_webapis, flask_instance
from .tag import tags


class Product(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    retailer_id = db.Column(db.String, db.ForeignKey('retailer.id'))
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('products', lazy='dynamic'),
                           lazy='dynamic')

restless_webapis.create_api(Product,
                            methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                            results_per_page=100);
