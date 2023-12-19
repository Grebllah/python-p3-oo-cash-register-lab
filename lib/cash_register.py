#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self._total = 0
    self.items = []
    self.last_transaction = 0
  @property
  def total(self):
    return self._total
  @total.setter
  def total(self, amount_to_add):
    self._total = amount_to_add
  def items(self):
    return self.items
  def add_item(self, item_to_add, price, quantity = 1):
    self._total = self.total + price * quantity
    self.last_transaction = price * quantity
    for num in range(quantity):
      self.items.append(item_to_add)
  def apply_discount(self):
    self._total = int(self.total * ((100 - self.discount) / 100))
    if self.discount > 0:
      print(f"After the discount, the total comes to ${self.total}.")
    elif self.discount == 0:
      print("There is no discount to apply.")
  def void_last_transaction(self):
    self._total = self._total - self.last_transaction
