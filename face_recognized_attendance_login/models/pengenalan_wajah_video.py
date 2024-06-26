import cv2
import face_recognition

known_image = face_recognition.load_image_file("C:\\Users\\awart\\OneDrive\\Gambar\\Rol Kamera\\WIN_20240605_11_24_15_Pro.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

face_locations = []
face_encodings = []
process_this_frame = True

video_capture = cv2.VideoCapture(0)  # 0 for webcam, or path to video file

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    # rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
            name = "Unknown"

            if True in matches:
                face_detected = 1
                name = employee.name
                # print("Wajah dikenali! Menutup video...")
                # video_capture.release()
                # cv2.destroyAllWindows()
                # exit()

            face_names.append(name)
            # return face_detected

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
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

    cv2.imshow('Video', frame)

    if "Unknown" in face_names or cv2.waitKey(1) & 0xFF == ord('q'):
        print("face_detected", face_detected)
        print("Employee name", face_names)
        return face_detected


video_capture.release()
cv2.destroyAllWindows()
