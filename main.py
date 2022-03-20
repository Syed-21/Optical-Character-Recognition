import cv2
import gtts
import pytesseract
from PIL import Image
from playsound import playsound

camera = cv2.VideoCapture(1)
while True:
    _, image = camera.read()
    cv2.imshow('text detection', image)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test1.jpg', image)
        break

camera.release()
cv2.destroyAllWindows()


def tesseract():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    imagepath = 'test1.jpg'
    text = pytesseract.image_to_string(Image.open(imagepath))
    print(text[:-1])
    t1 = gtts.gTTS(text)
    t1.save('speech.mp3')
    playsound('speech.mp3')


tesseract()
