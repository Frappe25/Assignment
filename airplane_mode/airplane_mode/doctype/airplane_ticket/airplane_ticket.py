# Copyright (c) 2023, Dev and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		items = []
		for x in self.add_ons:
			if x.item not in items:
				items.append(x.item)
			else:
				self.add_ons.remove(x)


	def before_save(self):
		self.total_amount = self.flight_price
		for item in self.add_ons:
				self.total_amount = self.total_amount + item.amount

	def on_submit(self):
		if self.status!="Boarded":
			frappe.throw("status should be boarded")
		pass
	def on_submit(self):
		number = random.randint(1,100)
		string = ("ABCDE")
		seat = random.sample(string,1)
		self.seat = f'{number}{seat[0]} '