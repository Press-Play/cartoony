from base import db

class Order:
    def __init__(self, email, photo, style_id, status = 0, paid = True, project_id = None):
        self.email = email
        self.photo = photo
        self.style_id = style_id
        self.status = status
        self.paid = paid
        self.project_id = project_id

    def insert(self):
        result = db.orders.insert_one({
            'email': self.email,
            'photo': self.photo,
            'style_id': self.style_id,
            'status': self.status,
            'paid': self.paid,
            'project_id': self.project_id,
        })
        print('One order: {0}'.format(result.inserted_id))

if __name__ == '__main__':
    o = Order('email', 'photo', 12)
    o.insert()