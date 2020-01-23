import face_recognition

# sample known images of sachin and kohli
known_images = ['sachin.jpg','sachin1.jpg','sachin2.jpg','virat_kohli.jpg','virat_kohli1.jpg','Ankit_new.jpg']

# unknown image which we want to detect of above players or person
detect_image = "unknown_sachin.jpg"
unknown_picture = face_recognition.load_image_file("unknown/"+detect_image)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

detection_flag = 0

for img in known_images:
	temp_img = face_recognition.load_image_file("known/"+img)
	known_image_encoding = face_recognition.face_encodings(temp_img)[0]
	results = face_recognition.compare_faces([known_image_encoding], unknown_face_encoding)

	if results[0] == True:
		detection_flag = 1
		face_identify = img.split('.')[0]
		detected_output = "It's a picture of "+face_identify
	else:
		not_detected_output = "It is unknown picture!"

if detection_flag == 1:
	print(detected_output)
else:
	print(not_detected_output)
