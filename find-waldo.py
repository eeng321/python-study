from PIL import Image
import face_recognition as fr

image = fr.load_image_file(r"C:\Users\eeng\Documents\python-study\resources\wwaldo.jpg")
floc = fr.face_locations(image)

flm_list = fr.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(floc)))

known = fr.load_image_file(r"C:\Users\eeng\Documents\python-study\resources\waldo\waldo2.jpg")
waldo_encoding = fr.face_encodings(known)[0]

for i in range(5,len(floc)):
    unknown_encoding = fr.face_encodings(image)[i]
    results = fr.compare_faces([waldo_encoding], unknown_encoding)
    print(results)
    if results:
        # Print the location of each face in this image
        top, right, bottom, left = floc[i]
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()

# for face_location in floc:

#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

#     # You can access the actual face itself like this:
#     face_image = image[top:bottom, left:right]
#     pil_image = Image.fromarray(face_image)
#     pil_image.show()