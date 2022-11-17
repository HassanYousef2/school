# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'
    _record_name = 'name'

    name = fields.Char()
    
    subject_id = fields.Many2one('subjects', string='Subject')
    student_id = fields.Many2one('res.partner', string='Student')
    student_country_id = fields.Many2one('res.country', related='student_id.country_id')
    teacher_id = fields.Many2one('res.partner', string='Teacher',)

    @api.onchange('subject_id')
    def get_class_name(self):
            today = date.today()
            year = today.strftime("%Y")
            month = today.month
            
            for rec in self:
                rec.name= '%s - %s - %s' % (rec.subject_id.name,year,month)

    def name_get(self):
            result = []
            today = date.today()
            year = today.strftime("%Y")
            month = today.month
            
            
            for rec in self:
                result.append((rec.id, '%s - %s - %s' % (rec.subject_id.name,year,month)))
	
            return result


class subjects(models.Model):
    _name='subjects'
    _record_name='subject_name'

    name = fields.Char()