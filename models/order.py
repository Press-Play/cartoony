from base import db, timestamp_now

class OrderState():
    # Initial state where we are still processing the order.
    INITIAL = 0

    # ALl open states.
    OPEN_PENDING = 11
    OPEN_CONFIRMED = 12
    OPEN_COMPLETE = 13
    OPEN_STATES = [
        OPEN_PENDING,
        OPEN_CONFIRMED,
        OPEN_COMPLETE,
    ]

    # All closed states.
    CLOSED_REJECTED = 21
    CLOSED_FAILED = 22
    CLOSED_CANCELLED = 23
    CLOSED_STATES = [
        CLOSED_REJECTED,
        CLOSED_FAILED,
        CLOSED_CANCELLED,
    ]

class OrderLog():
    __collcetion__ = 'orderslog'

    def __init__(self, order_id, state = OrderState.INITIAL):
        self.order_id = order_id
        self.state = state

    def insert(self):
        result = db[OrderLog.__collcetion__].insert_one({
            'order_id': self.order_id,
            'timestamp': timestamp_now(),
            'state': self.state,
        })
        print('One order log: {0}'.format(result.inserted_id))
        return result.inserted_id

class Order():
    __collcetion__ = 'orders'

    def __init__(self, email, photo, style_id, status = OrderState.INITIAL, paid = True, project_id = None):
        self.email = email
        self.photo = photo
        self.style_id = style_id
        self.status = status
        self.paid = paid
        self.project_id = project_id

    def isOpen(self):
        return self.state in OrderState.OPEN_STATES

    def isClosed(self):
        return self.state in OrderState.CLOSED_STATES

    def insert(self):
        result = db[OrderLog.__collcetion__].insert_one({
            'email': self.email,
            'timestamp': timestamp_now(),
            'photo': self.photo,
            'style_id': self.style_id,
            'status': self.status,
            'paid': self.paid,
            'project_id': self.project_id,
        })
        print('One order: {0}'.format(result.inserted_id))
        return result.inserted_id

# For testing only.
if __name__ == '__main__':
    o = Order('email', 'photo', 12)
    oid = o.insert()

    l = OrderLog(oid)
    l.insert()