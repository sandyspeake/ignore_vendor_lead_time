# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import datetime, time

class StockWarehouseOrderpoint(models.Model):
    _inherit="stock.warehouse.orderpoint"
    
    def _get_product_context(self):
        """
        Override to check if company settings allow for vendor lead time to be ignored
        Used to call `virtual_available` when running an orderpoint.
        """
        self.ensure_one()
        
        if self.company_id.ignore_vendor_lead_time:
            return {
                'location': self.location_id.id
            }
        else:
            return {
                'location': self.location_id.id,
                'to_date': datetime.combine(self.lead_days_date, time.max)
            }
        