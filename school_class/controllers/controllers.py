# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolClass(http.Controller):
#     @http.route('/school_class/school_class/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_class/school_class/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_class.listing', {
#             'root': '/school_class/school_class',
#             'objects': http.request.env['school_class.school_class'].search([]),
#         })

#     @http.route('/school_class/school_class/objects/<model("school_class.school_class"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_class.object', {
#             'object': obj
#         })
