from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'
    operating_unit_id = fields.Many2one('operating.unit', string='Operating Unit')


class PosOrder(models.Model):
    _inherit = 'pos.order'
    operating_unit_id = fields.Many2one('operating.unit', string='Operating Unit', readonly=True)
