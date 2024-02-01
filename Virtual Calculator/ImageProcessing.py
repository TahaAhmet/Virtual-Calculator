import cv2
from cvzone.HandTrackingModule import HandDetector
        
class Button:
    def __init__(self, pos, width, height, value, color=(225, 225, 225), border_color=(50, 50, 50), text_color=(50, 50, 50)):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value
        self.color = color
        self.border_color = border_color
        self.text_color = text_color

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      self.color, cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      self.border_color, 3)
        cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), cv2.FONT_HERSHEY_PLAIN,
                    2, self.text_color, 2)

    def checkClick(self, x, y, img):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, str(self.value), (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        5, (0, 0, 0), 5)
            if self.value == 'AC':
                return 'AC'
            else:
                return True
        else:
            return False

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)  # width
cap.set(4, 720)  # height
detector = HandDetector(detectionCon=0.8, maxHands=1)



# Creating Buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '='],
                    ['0', '.', '/', '+']]
buttonForAC = [['AC']]

# Button Color
buttonColor = (200, 200, 200)
buttonBorderColor = (40, 40, 40)
buttonTextColor = (40, 40, 40)


buttonList = []
for y in range(4):
    for x in range(4):
        xpos = x * 100 + 750
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x], buttonColor, buttonBorderColor, buttonTextColor))

for y in range(1):
    for x in range(1):
        xpos = x * 100 + 1050
        ypos = y * 100 + 50
        buttonList.append(Button((xpos, ypos), 100, 100, buttonForAC[y][x], buttonColor, buttonBorderColor, buttonTextColor))

# Variables
myEquation = ''
delayCounter = 0

# Loop
while True:
    # Get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detection of hand
    hands, img = detector.findHands(img, flipType=False)

    # Draw all buttons
    cv2.rectangle(img, (750, 50), (800 + 350, 50 + 100),
                  (225, 225, 225), cv2.FILLED)

    cv2.rectangle(img, (750, 50), (800 + 350, 50 + 100),
                  (50, 50, 50), 3)

    for button in buttonList:
        button.draw(img)

    # Check for Hand
    if hands:
        # Find distance between fingers
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8], lmList[12], img)
        print(length)
        x, y = lmList[8]

        # If clicked check which button and perform action
        if length < 50 and delayCounter == 0:
            for i, button in enumerate(buttonList):
                result = button.checkClick(x, y, img)
                if result == 'AC':
                    myEquation = myEquation[:-1]  # Remove the last character
                elif result == 'AC':
                    cv2.destroyAllWindows()
                    cap.release()
                elif result:
                    myValue = buttonListValues[int(i / 4)][int(i % 4)]  # get correct number
                    if myValue == '=':
                        myEquation = str(eval(myEquation))
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # To avoid multiple clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Display the result with dynamic font size
    font = cv2.FONT_HERSHEY_PLAIN
    font_size = 3
    text_thickness = 3
    text_color = (50, 50, 50)
    text_position = (750, 120)

    text_width, _ = cv2.getTextSize(myEquation, font, font_size, text_thickness)[0]

    if text_width > 350:  
        font_size = int(350 / text_width * font_size)

    cv2.putText(img, myEquation, text_position, font, font_size, text_color, text_thickness)

    # Display Image
    cv2.imshow("Image", img)

    # Check for 'q' key press
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        cap.release()
        break  # Break out of the loop when 'q' is pressed

cv2.destroyAllWindows()
cap.release()