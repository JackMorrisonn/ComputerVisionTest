# ComputerVisionTest

---

### About the project

This project was created as a test of my initial research and exploration into computer vision and computer tracking. Using Google's MediaPipe framework for hand tracking as well as the OpenCv library for the computer vision, this program is able to count the amount of fingers held up on a single hand in real time. Due to the way that MediaPipe's finger ID system works, it is unable to do more than one hand at a time, since the ID values for each node are the same regardeless of if there is more than one hand up. 

---

### Functionality

When the program is run it simply opens up a view of whichever camera is selected as the main camera for the computer. When a hand is held up, MediaPipe tracks the markers it uses to detect hand position and draws them on the screen to construct a skeleton. I then was able to access the x and y values and normalise them so they were relative to the screen size. The values for each x and y position are stored in a 20 x 2 array, where index 0 is the x value and index 1 is the y value. 

It then checks to see if the tip of each finger is below the marker used for the middle knuckes on the finger, meaning that it would be considered "down". If it is not down then it adds 1 to the total. For the thumb, the principle is the same except it checks for the horizontal positon to see if it is greater than the position of the index knuckle. The function `checkNumber()` is called every frame and returns the total number of fingers held up in real time.

This allows for any combination of fingers to be held up and still return an accurate number.

---

### Test Cases

<img src="https://github.com/JackMorrisonn/ComputerVisionTest/blob/main/1finger.png" alt="One Finger" width="600"/>

<img src="https://github.com/JackMorrisonn/ComputerVisionTest/blob/main/2fingers.png" alt="Two Fingers" width="600"/>

<img src="https://github.com/JackMorrisonn/ComputerVisionTest/blob/main/3fingers.png" alt="Three Fingers" width="600"/>

<img src="https://github.com/JackMorrisonn/ComputerVisionTest/blob/main/4Fingers.png" alt="Four Fingers" width="600"/>
