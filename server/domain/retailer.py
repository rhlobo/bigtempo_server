from ..app import persistence as db, restless_webapis, flask_instance


class Retailer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apikey = db.Column(db.String, unique=True)
    #products = db.relationship('Product', backref=db.backref('retailer', lazy='dynamic'))


restless_webapis.create_api(Retailer,
                            methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                            results_per_page=-1);
