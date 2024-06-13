# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
import base64
import cv2
import face_recognition
import numpy as np
import os
import time
from io import BytesIO
from PIL import Image
from odoo import api, models, fields, _
from odoo.exceptions import UserError
import requests


class HrEmployee(models.Model):
    """This class inherits the model 'hr.employee' to fetch the image of the
    employee, and later it will compare with the fetched image from camera """
    _inherit = 'hr.employee'

    image_url = fields.Char(string='Image URL', help="Url of Image")

    @api.model
    def get_login_screen(self):
        employee = self.search([('user_id', '=', self.env.user.id)], limit=1)
        path = employee.image_url
        # known_image = face_recognition.load_image_file("D:\\WIN_20240605_11_24_15_Pro.jpg")
        if path:
            known_image = face_recognition.load_image_file(path)
            known_face_encoding = face_recognition.face_encodings(known_image)[0]
            face_locations = []
            face_encodings = []
            process_this_frame = True
            face_detected = 0
            name = "Unknown"
            video_capture = cv2.VideoCapture(
                0)  # 0 for webcam, or path to video file

            while True:
                ret, frame = video_capture.read()

                if not ret:
                    break

                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                if process_this_frame:
                    face_locations = face_recognition.face_locations(small_frame)
                    face_encodings = face_recognition.face_encodings(
                        small_frame, face_locations)

                    face_names = []
                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces(
                            [known_face_encoding], face_encoding)

                        if True in matches:
                            face_detected = 1
                            name = employee.name

                        face_names.append(name)
                process_this_frame = not process_this_frame

                for (top, right, bottom,
                    left), name in zip(face_locations, face_names):
                    top *= 4
                    right *= 4
                    bottom *= 4
                    left *= 4

                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom),
                                (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,
                                (255, 255, 255), 1)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                cv2.imshow('Video', frame)
                print("face_detected", face_detected)
                print("name", name)
                return face_detected
            video_capture.release()
            cv2.destroyAllWindows()
        else:
             return 3
class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    is_face = fields.Boolean()
