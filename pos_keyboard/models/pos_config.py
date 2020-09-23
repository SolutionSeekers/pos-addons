# -*- coding: utf-8 -*-

from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    numpad_only = fields.Boolean(default=True)