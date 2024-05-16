# -*- coding: utf-8 -*-

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    ignore_vendor_lead_time = fields.Boolean(string="Ignore Vendor Lead Time")
