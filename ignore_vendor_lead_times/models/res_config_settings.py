# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    ignore_vendor_lead_time = fields.Boolean(
        "Ignore Vendor Lead Time",
        related="company_id.ignore_vendor_lead_time",
        readonly=False
    )
