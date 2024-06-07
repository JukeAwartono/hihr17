# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request
from odoo.addons.hr_attendance.controllers.main import HrAttendance
from odoo.tools import float_round
import datetime
import json
from odoo.exceptions import ValidationError, RedirectWarning, UserError


class FaceRecognizedHrAttendance(HrAttendance):

    # @staticmethod
    # def _get_employee_info_response_face(employee):
    #     response = {}
    #     if employee:
    #         response = {
    #             'id': employee.id,
    #             'employee_name': employee.name,
    #             'employee_avatar': employee.image_1920,
    #             'hours_today': float_round(employee.hours_today, precision_digits=2),
    #             'total_overtime': float_round(employee.total_overtime, precision_digits=2),
    #             'last_attendance_worked_hours': float_round(employee.last_attendance_worked_hours, precision_digits=2),
    #             'last_check_in': employee.last_check_in,
    #             'attendance_state': employee.attendance_state,
    #             'hours_previously_today': float_round(employee.hours_previously_today, precision_digits=2),
    #             'kiosk_delay': employee.company_id.attendance_kiosk_delay * 1000,
    #             'attendance': {'check_in': employee.last_attendance_id.check_in,
    #                            'check_out': employee.last_attendance_id.check_out},
    #             'overtime_today': request.env['hr.attendance.overtime'].sudo().search([
    #                 ('employee_id', '=', employee.id), ('date', '=', datetime.date.today()),
    #                 ('adjustment', '=', False)]).duration or 0,
    #             'use_pin': employee.company_id.attendance_kiosk_use_pin,
    #             'display_systray': employee.company_id.attendance_from_systray,
    #             'display_overtime': employee.company_id.hr_attendance_display_overtime,
    #             'is_face': True
    #         }
    #     return response

    @http.route('/hr_attendance/systray_check_in_out',
                type="json",
                auth="user")
    def systray_attendance(self, latitude=False, longitude=False):
        employee = request.env.user.employee_id
        get_login_screen = employee.get_login_screen()
        geo_ip_response = self._get_geoip_response(mode='systray',
                                                       latitude=latitude,
                                                       longitude=longitude)
        employee._attendance_action_change(geo_ip_response)
        if get_login_screen:
            return self._get_employee_info_response(employee)
        else:
            # return self._get_employee_info_response_face(employee)
            return "No matching face"
            # raise UserError(_("No matching face"))
            # raise ValueError(_('Location attendance not found!'))
