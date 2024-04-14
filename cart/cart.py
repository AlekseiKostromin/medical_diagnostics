
class Cart:

    def add(self, labtest, quantity=1, override_quantity=False):
        """
        Добавить товар в корзину либо обновить его количество.
        """
        labtest_id = str(labtest.id)
        if labtest_id not in self.cart:
            self.cart[labtest_id] = {'quantity': 0,
                                     'price': str(labtest.price)}
        if override_quantity:
            self.cart[labtest_id]['quantity'] = quantity
        else:
            self.cart[labtest_id]['quantity'] += quantity
        self.save()

    def remove(self, labtest):
        """
        Удалить товар из корзины.
        """
        labtest_id = str(labtest.id)
        if labtest_id in self.cart:
            del self.cart[labtest_id]
        self.save()
