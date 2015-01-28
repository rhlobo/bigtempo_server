from ..app import persistence as db, restless_webapis, flask_instance


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String)
    name = db.Column(db.String)
    url = db.Column(db.String)
    retailer_id = db.Column(db.Integer, db.ForeignKey('retailer.id'))
    retailer = db.relationship('Retailer', backref=db.backref('products', lazy='dynamic'))


restless_webapis.create_api(Product,
                            methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                            results_per_page=100);
