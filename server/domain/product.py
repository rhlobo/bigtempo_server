from ..app import persistence as db, restless_webapis, flask_instance
from .tag import tags


class Product(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    retailer_id = db.Column(db.String(32), db.ForeignKey('retailer.id'), primary_key=True)
    tags = db.relationship('Tag',
                           backref=db.backref('products', lazy='dynamic'),
                           lazy='dynamic',
                           secondary=tags,
                           primaryjoin='and_(Product.id == tags.c.product_id, Product.retailer_id == tags.c.product_retailer)',
                           secondaryjoin='Tag.id == tags.c.tag_id')

restless_webapis.create_api(Product,
                            methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                            results_per_page=100);
