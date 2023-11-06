# Copyright (c) 2023, Dev and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator,Document):
	def on_submit(self):
		self.status = "Completed"
	pass
