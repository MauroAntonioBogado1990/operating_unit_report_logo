from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'
    operating_unit_id = fields.Many2one('operating.unit', string='Unidad Operativa')
    operating_unit_report_logo = fields.Binary(related='operating_unit_id.report_logo', readonly=True)
    operating_unit_partner_image = fields.Binary(related='operating_unit_id.partner_id.image_1920', readonly=True)

    @api.onchange('journal_id')
    def _onchange_journal_operating_unit(self):
        if self.journal_id and self.journal_id.operating_unit_id:
            self.operating_unit_id = self.journal_id.operating_unit_id


class PosOrder(models.Model):
    _inherit = 'pos.order'
    operating_unit_id = fields.Many2one('operating.unit', string='Unidad Operativa', readonly=True)

    @api.model
    def create(self, vals):
        # Propagate operating unit from pos config if not provided
        if not vals.get('operating_unit_id') and vals.get('config_id'):
            config = self.env['pos.config'].browse(vals.get('config_id'))
            if config and config.operating_unit_id:
                vals['operating_unit_id'] = config.operating_unit_id.id
        return super(PosOrder, self).create(vals)
