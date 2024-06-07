from odoo.addons.hr_attendance.controllers.main import HrAttendance
from odoo import http, _
from odoo.http import request
import face_recognition


class HrAttendanceFace(HrAttendance):

    @http.route('/hr_attendance/systray_check_in_out',
                type="json",
                auth="user")
    def systray_attendance(self, latitude=False, longitude=False):
        employee = request.env.user.employee_id
        # print(employee, "employyyyyyyyyyyyyyyyyyyyyyyy")
        # geo_ip_response = self._get_geoip_response(mode='systray',
        #                                            latitude=latitude,
        #                                            longitude=longitude)
        # employee._attendance_action_change(geo_ip_response)
        # return self._get_employee_info_response(employee)

