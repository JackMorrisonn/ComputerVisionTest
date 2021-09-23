import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

hands = mp_hands.Hands()

handMask = cv2.createBackgroundSubtractorMOG2()

cap = cv2.VideoCapture(0)
isPresent = False

positionGrid = [[0 for x in range(2)]for y in range(21)]

def getX(index):
	return positionGrid[index][0]

def getY(index):
	return positionGrid[index][1]


def checkNumber():
	total = 0
	#tips = [4, 8, 12, 16, 20]
	#knuckles = [5, 5, 19, 13, 17]

	if getX(8) < getX(20):
		#Left Hand
		if getX(4) < getX(5):
			total += 1

	else:
		#Right Hand
		if getX(4) > getX(5):
			total += 1

	if getY(8) < getY(6):
		total += 1

	if getY(12) < getY(10):
		total += 1

	if getY(16) < getY(14):
		total += 1

	if getY(20) < getY(19):
		total += 1

	return total




#Hand recognition courtesy of Google's MediaPipe hand recognition framework
while True:
	success, image = cap.read() 
	width = image.shape[1]
	height = image.shape[0]
	image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_RGB2BGR)
	blank = np.zeros(shape=[360, 640, 3], dtype=np.uint8)
	results = hands.process(image)

	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

	if results.multi_hand_landmarks:
		for hand_landmarks in results.multi_hand_landmarks:
			mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

			#Drawing on a blank canvas rather than on a webcam
			#mp_drawing.draw_landmarks(blank, hand_landmarks, mp_hands.HAND_CONNECTIONS)

			for id, lm in enumerate(hand_landmarks.landmark):
				h, w, c = image.shape
				realx = int(lm.x * w)
				realy = int(lm.y * h)

				positionGrid[id][0] = realx
				positionGrid[id][1] = realy


	cv2.putText(image, str(checkNumber()), (width - 100, height - 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 4)

	#Draw on webcam
	cv2.imshow("Image", image)
	
	#Draw on blank canvas
	#cv2.imshow("Blank", blank)

	if cv2.waitKey(1) == ord('q'):
		break
cap.release()

cv2.destroyAllWindows()
