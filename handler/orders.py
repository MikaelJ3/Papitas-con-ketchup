from dao.orders import OrdersDao
import time


class OrdersHandler:
    def create_new_order(self, credit_card):
        dao = OrdersDao()
        current_date = time.strftime("%d%m%Y")
        order_id = dao.create_new_order(credit_card, current_date)
        return order_id
