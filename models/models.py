# -*- coding: utf-8 -*-

from odoo import models, fields, api

class open_academy(models.Model):
    _name = 'open.academy'
    _description = 'open.academy module'

    title = fields.Char(required=True)
    description = fields.Text()
