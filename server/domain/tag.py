from ..app import persistence as db, restless_webapis, flask_instance


tags = db.Table('tags',
                db.Column('tag_id', db.String(32), db.ForeignKey('tag.id')),
                db.Column('product_id', db.String(32), db.ForeignKey('product.id')))


class Tag(db.Model):
    id = db.Column(db.String(32), primary_key=True)


restless_webapis.create_api(Tag,
                            methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                            results_per_page=-1);
