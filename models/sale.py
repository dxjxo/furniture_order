# -*- coding:utf-8 -*-
__author__ = 'dxj'
from odoo import api, fields, models, _


class FurnitureOrder(models.Model):
    _inherit = 'sale.order'
    _description = "...."
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ('cl', '测量'),
        ('ct', '出图'),
        ('confirm_plan', '确认方案'),
        ('pay', '已付款'),
        ('decompose', '拆单'),
        ('kl', '开料'),
        ('dk', '打孔'),
        ('fb', '封边'),
        ('try', '试装'),
        ('yuy', '预约'),
        ('transport', '运输'),
        ('install', '安装'),
        ('after_order', '需售后'),
        ('bx', '报修'),
        ('con_wxplan', '确认维修方案'),
        ('repair', '维修'),
        ('check', '验收'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    street = fields.Char('详细地址')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('城市')
    phone = fields.Char('电话')
    quxian = fields.Char('区县')
    contact = fields.Char('联系人')
    state_id = fields.Many2one("res.country.state", string='省')
    country_id = fields.Many2one('res.country', string='国家')
    enclosure = fields.Binary('Image')
    qr_code = fields.Binary('Image')
    desc = fields.Text('Description')
    wuliu = fields.Selection([
        ('sd', '申通'),
        ('sf', '顺风'),
        ('db', '德邦'),

    ], string='物流方式', copy=False, index=True, default='sd')

    saleafter_cate = fields.Selection([
        ('az', '安装问题'),
        ('sc', '生产问题'),
        ('color', '颜色问题'),

    ], string='售后类别', copy=False, index=True, track_visibility='onchange')
