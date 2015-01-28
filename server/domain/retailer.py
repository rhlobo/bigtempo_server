from ..app import persistence as db, restless_webapis, flask_instance


class Retailer(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    products = db.relationship('Product', backref='retailer', lazy='dynamic')


restless_webapis.create_api(Retailer,
                            methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                            results_per_page=-1,
                            exclude_columns=['products']);
