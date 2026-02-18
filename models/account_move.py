from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    operating_unit_id = fields.Many2one('operating.unit', string='Unidad Operativa')
