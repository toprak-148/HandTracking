# import cv2 as cv
# import mediapipe
# import keyboard
# import time
# from selenium.webdriver.common.by import By
# import speech_recognition as sr

# Eski sürüm

# class HandProcessor:
#     def __init__(self,driver):
#         self.mpHands = mediapipe.solutions.hands
#         self.hands = self.mpHands.Hands(max_num_hands=1)
#         self.mpDraw = mediapipe.solutions.drawing_utils
#         self.last_like_time = 0
#         self.last_retweet_time = 0
#         self.last_scroll_down_time = 0
#         self.last_scroll_up_time = 0
#         self.last_bookmark_time = 0
#         self.last_comment_time = 0

#         self.cooldown_time = 2  # 2 seconds cooldown
#         self.driver = driver

#     def bgr2RGB(self, img):
#         imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#         return imgRGB

#     def handLandMarkModel(self, imgRGB):
#         hlms = self.hands.process(imgRGB)
#         return hlms

#     def like_func(self, hlms, imgRGB):
#         height, width, _ = imgRGB.shape  # _ : channel (we do not use)

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     if (fingerNum < 4 and landmark.y > handlandmarks.landmark[2].y and
#                         handlandmarks.landmark[5].x > handlandmarks.landmark[8].x and
#                         handlandmarks.landmark[9].x > handlandmarks.landmark[12].x and
#                         handlandmarks.landmark [13].x > handlandmarks.landmark[16].x and
#                         handlandmarks.landmark[17].x > handlandmarks.landmark[20].x and
#                         handlandmarks.landmark[20].y > handlandmarks.landmark[2].y):
#                         #print("Like")

#                         current_time = time.time()
#                         if current_time - self.last_like_time > self.cooldown_time:
#                             self.like_tweet()
#                             self.last_like_time = current_time

#                 self.mpDraw.draw_landmarks(imgRGB, handlandmarks, self.mpHands.HAND_CONNECTIONS)

#         return imgRGB

#     def like_tweet(self):
#         try:
#             keyboard.press_and_release('l')
#         except Exception as e:
#             print("Failed to like tweet.")

#     def retweet_func(self, hlms, imgRGB):
#         height, width, _ = imgRGB.shape  # _ : channel (we do not use)

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     if (handlandmarks.landmark[12].y < handlandmarks.landmark[11].y and
#                         handlandmarks.landmark[16].y < handlandmarks.landmark[15].y and
#                         handlandmarks.landmark[20].y < handlandmarks.landmark[19].y and
#                         handlandmarks.landmark[8].y > handlandmarks.landmark[6].y and
#                         fingerNum == 4 or fingerNum == 8):

#                         thumb_tip = handlandmarks.landmark[4]
#                         index_tip = handlandmarks.landmark[8]

#                         thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                         index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                         distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
#                         #print(distance)

#                         if distance < 10:
#                             #print("Retweet!")

#                             current_time = time.time()
#                             if current_time - self.last_retweet_time > self.cooldown_time:
#                                 print("Retweet!")
#                                 self.retweet()
#                                 self.last_retweet_time = current_time


#                 # self.mpDraw.draw_landmarks(img, handlandmarks, self.mpHands.HAND_CONNECTIONS)

#         #return imgRGB

#     def retweet(self):
#         try:
#             keyboard.press_and_release('t')
#             time.sleep(1)
#             retweet = self.driver.find_elements(By.XPATH, '//div[@role="menuitem"]')  # retweet yap
#             retweet[0].click()
#         except Exception as e:
#             print("Failed to retweet.")

#     def scroll_down_func(self, hlms, imgRGB):
#         height, width, _ = imgRGB.shape

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     if (handlandmarks.landmark[12].y > handlandmarks.landmark[9].y and
#                         handlandmarks.landmark[16].y > handlandmarks.landmark[13].y and
#                         handlandmarks.landmark[20].y > handlandmarks.landmark[17].y and
#                         handlandmarks.landmark[4].x < handlandmarks.landmark[5].x and
#                         handlandmarks.landmark[8].y < handlandmarks.landmark[5].y):
#                         #print("Scroll Down")

#                         current_time = time.time()
#                         if current_time - self.last_scroll_down_time > self.cooldown_time:
#                             self.scroll_down_tweet()
#                             self.last_scroll_down_time = current_time

#             #return imgRGB
#     def scroll_down_tweet(self):
#         try:
#             keyboard.press_and_release('j')
#         except Exception as e:
#             print("Failed to scroll down.")

#     def scroll_up_func(self, hlms, imgRGB):
#         height, width, _ = imgRGB.shape

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     if (handlandmarks.landmark[4].y > handlandmarks.landmark[0].y and
#                         handlandmarks.landmark[8].x < handlandmarks.landmark[5].x and
#                         handlandmarks.landmark[12].x < handlandmarks.landmark[9].x and
#                         handlandmarks.landmark[16].x < handlandmarks.landmark[13].x and
#                         handlandmarks.landmark[20].x < handlandmarks.landmark[17].x):
#                         #print("Scroll Up")

#                         current_time = time.time()
#                         if current_time - self.last_scroll_up_time > self.cooldown_time:
#                             self.scroll_up_tweet()
#                             self.last_scroll_up_time = current_time

#             #return imgRGB

#     def scroll_up_tweet(self):
#         try:
#             keyboard.press_and_release('k')
#         except Exception as e:
#             print("Failed to scroll up")



#     def bookmark_func(self, hlms, imgRGB):
#         height, width, _ = imgRGB.shape

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     if (handlandmarks.landmark[8].y > handlandmarks.landmark[7].y and
#                         handlandmarks.landmark[12].y > handlandmarks.landmark[11].y and
#                         handlandmarks.landmark[16].y > handlandmarks.landmark[15].y and
#                         handlandmarks.landmark[20].y > handlandmarks.landmark[19].y and
#                         handlandmarks.landmark[4].y < handlandmarks.landmark[8].y and
#                         handlandmarks.landmark[4].x < handlandmarks.landmark[1].x):

#                         thumb_tip = handlandmarks.landmark[4]
#                         index_tip = handlandmarks.landmark[8]

#                         thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                         index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                         distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

#                         if distance > 15:
#                             #print("Bookmark!")

#                             current_time = time.time()
#                             if current_time - self.last_bookmark_time > self.cooldown_time:
#                                 self.bookmark_tweet()
#                                 self.last_bookmark_time = current_time

#     def bookmark_tweet(self):
#         try:
#             keyboard.press_and_release('b')
#         except Exception as e:
#             print("Failed to bookmark tweet.")

#     def comment_func(self, hlms, imgRGB):

#         height, width, _ = imgRGB.shape

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     thumb_tip = handlandmarks.landmark[4]
#                     index_tip = handlandmarks.landmark[8]

#                     thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                     index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                     distance1 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
#                     #print(f"distance1: {distance1}")

#                     index_tip = handlandmarks.landmark[12]

#                     thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                     index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                     distance2 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
#                     #print(f"distance2: {distance2}")


#                     index_tip = handlandmarks.landmark[16]

#                     thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                     index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                     distance3 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
#                     #print(f"distance3: {distance3}")

#                     index_tip = handlandmarks.landmark[20]

#                     thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                     index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                     distance4 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
#                     #print(f"distance4: {distance4}")


#                     if (distance1 < 80 and distance2 < 30 and distance3 < 30 and distance4 < 30):
#                         #print("comment")
#                         current_time = time.time()
#                         if current_time - self.last_comment_time > self.cooldown_time:
#                             self.comment_tweet()
#                             self.last_comment_time = current_time

#     def comment_tweet(self):
#         try:
#             keyboard.press_and_release('r')
#             r = sr.Recognizer()
#             with sr.Microphone() as source:
#                 try:
#                     # Mikrofonun en fazla 5 saniye içinde ses algılamasını bekler
#                     audio = r.listen(source, timeout=3, phrase_time_limit=10)
#                     voice = r.recognize_google(audio, language='tr-TR')
#                     print("Recognized voice:", voice)
#                     comment_field = self.driver.find_elements(By.XPATH, "//div[@data_testid = 'tweetTextarea_0']")
#                     print(comment_field)
#                     comment_field.send_keys(voice)
#                     #data-testid="tweetButton"
#                 except sr.WaitTimeoutError:
#                     print("Time out: The microphone could not detect sound within 5 seconds.")
#                 except sr.UnknownValueError:
#                     print("Unidentified voice: Voice recognition failed.")
#                 except sr.RequestError as e:
#                     print("Request error; Google Web Speech API could not be reached; {0}".format(e))
#         except Exception as e:
#             print("Failed to comment tweet.")




#     def empty_func(self, hlms, imgRGB):

#         height, width, _ = imgRGB.shape

#         if hlms.multi_hand_landmarks:
#             for handlandmarks in hlms.multi_hand_landmarks:
#                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
#                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

#                     thumb_tip = handlandmarks.landmark[4]
#                     index_tip = handlandmarks.landmark[8]

#                     thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
#                     index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

#                     distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

#                     if (handlandmarks.landmark[4].y < handlandmarks.landmark[3].y and
#                         handlandmarks.landmark[8].y < handlandmarks.landmark[7].y and
#                         handlandmarks.landmark[12].y < handlandmarks.landmark[11].y and
#                         handlandmarks.landmark[16].y < handlandmarks.landmark[15].y and
#                         handlandmarks.landmark[20].y < handlandmarks.landmark[19].y and
#                         handlandmarks.landmark[8].y < handlandmarks.landmark[4].y and
#                         distance > 120):
#                         pass
#                         #print("Empty hand!")

import cv2 as cv
import mediapipe
import keyboard
import time
import threading
from selenium.webdriver.common.by import By
import speech_recognition as sr
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HandProcessor:
    def __init__(self, driver):
        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mediapipe.solutions.drawing_utils
        self.last_like_time = 0
        self.last_retweet_time = 0
        self.last_scroll_down_time = 0
        self.last_scroll_up_time = 0
        self.last_bookmark_time = 0
        self.last_comment_time = 0

        self.cooldown_time = 2  # 2 seconds cooldown
        self.driver = driver

    def bgr2RGB(self, img):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return imgRGB

    def handLandMarkModel(self, imgRGB):
        hlms = self.hands.process(imgRGB)
        return hlms

    def like_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape  # _ : channel (we do not use)

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (fingerNum < 4 and landmark.y > handlandmarks.landmark[2].y and
                        handlandmarks.landmark[5].x > handlandmarks.landmark[8].x and
                        handlandmarks.landmark[9].x > handlandmarks.landmark[12].x and
                        handlandmarks.landmark[13].x > handlandmarks.landmark[16].x and
                        handlandmarks.landmark[17].x > handlandmarks.landmark[20].x and
                        handlandmarks.landmark[20].y > handlandmarks.landmark[2].y):
                        #print("Like")

                        current_time = time.time()
                        if current_time - self.last_like_time > self.cooldown_time:
                            self.like_tweet()
                            self.last_like_time = current_time

                self.mpDraw.draw_landmarks(imgRGB, handlandmarks, self.mpHands.HAND_CONNECTIONS)

        return imgRGB

    def like_tweet(self):
        try:
            keyboard.press_and_release('l')
        except Exception as e:
            print("Failed to like tweet.")

    def retweet_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape  # _ : channel (we do not use)

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[12].y < handlandmarks.landmark[11].y and
                        handlandmarks.landmark[16].y < handlandmarks.landmark[15].y and
                        handlandmarks.landmark[20].y < handlandmarks.landmark[19].y and
                        handlandmarks.landmark[8].y > handlandmarks.landmark[6].y and
                        fingerNum == 4 or fingerNum == 8):

                        thumb_tip = handlandmarks.landmark[4]
                        index_tip = handlandmarks.landmark[8]

                        thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                        index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                        distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                        #print(distance)

                        if distance < 10:
                            #print("Retweet!")

                            current_time = time.time()
                            if current_time - self.last_retweet_time > self.cooldown_time:
                                print("Retweet!")
                                self.retweet()
                                self.last_retweet_time = current_time

    def retweet(self):
        try:
            keyboard.press_and_release('t')
            time.sleep(1)
            retweet = self.driver.find_elements(By.XPATH, '//div[@role="menuitem"]')  # retweet yap
            retweet[0].click()
        except Exception as e:
            print("Failed to retweet.")

    def scroll_down_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[12].y > handlandmarks.landmark[9].y and
                        handlandmarks.landmark[16].y > handlandmarks.landmark[13].y and
                        handlandmarks.landmark[20].y > handlandmarks.landmark[17].y and
                        handlandmarks.landmark[4].x < handlandmarks.landmark[5].x and
                        handlandmarks.landmark[8].y < handlandmarks.landmark[5].y):
                        #print("Scroll Down")

                        current_time = time.time()
                        if current_time - self.last_scroll_down_time > self.cooldown_time:
                            self.scroll_down_tweet()
                            self.last_scroll_down_time = current_time

    def scroll_down_tweet(self):
        try:
            keyboard.press_and_release('j')
        except Exception as e:
            print("Failed to scroll down.")

    def scroll_up_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[4].y > handlandmarks.landmark[0].y and
                        handlandmarks.landmark[8].x < handlandmarks.landmark[5].x and
                        handlandmarks.landmark[12].x < handlandmarks.landmark[9].x and
                        handlandmarks.landmark[16].x < handlandmarks.landmark[13].x and
                        handlandmarks.landmark[20].x < handlandmarks.landmark[17].x):
                        #print("Scroll Up")

                        current_time = time.time()
                        if current_time - self.last_scroll_up_time > self.cooldown_time:
                            self.scroll_up_tweet()
                            self.last_scroll_up_time = current_time

    def scroll_up_tweet(self):
        try:
            keyboard.press_and_release('k')
        except Exception as e:
            print("Failed to scroll up")

    def bookmark_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    if (handlandmarks.landmark[8].y > handlandmarks.landmark[7].y and
                        handlandmarks.landmark[12].y > handlandmarks.landmark[11].y and
                        handlandmarks.landmark[16].y > handlandmarks.landmark[15].y and
                        handlandmarks.landmark[20].y > handlandmarks.landmark[19].y and
                        handlandmarks.landmark[4].y < handlandmarks.landmark[8].y and
                        handlandmarks.landmark[4].x < handlandmarks.landmark[1].x):

                        thumb_tip = handlandmarks.landmark[4]
                        index_tip = handlandmarks.landmark[8]

                        thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                        index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                        distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

                        if distance > 15:
                            #print("Bookmark!")

                            current_time = time.time()
                            if current_time - self.last_bookmark_time > self.cooldown_time:
                                self.bookmark_tweet()
                                self.last_bookmark_time = current_time

    def bookmark_tweet(self):
        try:
            keyboard.press_and_release('b')
        except Exception as e:
            print("Failed to bookmark tweet.")

    def comment_func(self, hlms, imgRGB):
        height, width, _ = imgRGB.shape

        if hlms.multi_hand_landmarks:
            for handlandmarks in hlms.multi_hand_landmarks:
                for fingerNum, landmark in enumerate(handlandmarks.landmark):
                    positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                    thumb_tip = handlandmarks.landmark[4]
                    index_tip = handlandmarks.landmark[8]

                    thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                    index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                    distance1 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                    #print(f"distance1: {distance1}")

                    index_tip = handlandmarks.landmark[12]

                    thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                    index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                    distance2 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                    #print(f"distance2: {distance2}")

                    index_tip = handlandmarks.landmark[16]

                    thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                    index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                    distance3 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                    #print(f"distance3: {distance3}")

                    index_tip = handlandmarks.landmark[20]

                    thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                    index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                    distance4 = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5
                    #print(f"distance4: {distance4}")

                    if (distance1 < 80 and distance2 < 30 and distance3 < 30 and distance4 < 30):
                        #print("comment")
                        current_time = time.time()
                        if current_time - self.last_comment_time > self.cooldown_time:
                            self.last_comment_time = current_time
                            threading.Thread(target=self.comment_tweet).start() 
 
 

    def comment_tweet(self):
            try:
                keyboard.press_and_release('r')
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    try:
                        # Mikrofonun en fazla 5 saniye içinde ses algılamasını bekler
                        audio = r.listen(source, timeout=3, phrase_time_limit=10)
                        voice = r.recognize_google(audio, language='tr-TR')
                        print("Recognized voice:", voice)
                        comment_field = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
                        comment_field.send_keys(voice)
                        
                        # Eğer ses algılanmazsa yorum alanını kapatır
                        if voice == "kapat":
                            comment_field_close = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/button')
                            comment_field_close.click()[0]
                    except sr.WaitTimeoutError:
                        print("Time out: The microphone could not detect sound within 5 seconds.")
                    except sr.UnknownValueError:
                        print("Unidentified voice: Voice recognition failed.")
                    except sr.RequestError as e:
                        print("Request error; Google Web Speech API could not be reached; {0}".format(e))
            except Exception as e:
                print("Failed to comment tweet: {0}".format(e))
            
     # def comment_tweet(self):
     #     try:
     #         keyboard.press_and_release('r')
     #         r = sr.Recognizer()
     #         with sr.Microphone() as source:
     #             try:
     #                 # Mikrofonun en fazla 5 saniye içinde ses algılamasını bekler
     #                 audio = r.listen(source, timeout=3, phrase_time_limit=10)
     #                 voice = r.recognize_google(audio, language='tr-TR')
     #                 print("Recognized voice:", voice)
     #                 comment_field = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0']")
     #                 comment_field.send_keys(voice)
     #                 # data-testid="tweetButton"
     #                 if(audio == ""):
     #                     comment_field_close = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/div/button')
     #                     comment_field_close.click()
     #             except sr.WaitTimeoutError:
     #                 print("Time out: The microphone could not detect sound within 5 seconds.")
     #             except sr.UnknownValueError:
     #                 print("Unidentified voice: Voice recognition failed.")
     #             except sr.RequestError as e:
     #                 print("Request error; Google Web Speech API could not be reached; {0}".format(e))
     #     except Exception as e:
     #         print("Failed to comment tweet.")
     
    def empty_func(self, hlms, imgRGB):
         
         height, width, _ = imgRGB.shape

         if hlms.multi_hand_landmarks:
             for handlandmarks in hlms.multi_hand_landmarks:
                 for fingerNum, landmark in enumerate(handlandmarks.landmark):
                     positionX, positionY = int(landmark.x * width), int(landmark.y * height)

                     thumb_tip = handlandmarks.landmark[4]
                     index_tip = handlandmarks.landmark[8]

                     thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                     index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)

                     distance = ((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2) ** 0.5

                     if (handlandmarks.landmark[4].y < handlandmarks.landmark[3].y and
                         handlandmarks.landmark[8].y < handlandmarks.landmark[7].y and
                         handlandmarks.landmark[12].y < handlandmarks.landmark[11].y and
                         handlandmarks.landmark[16].y < handlandmarks.landmark[15].y and
                         handlandmarks.landmark[20].y < handlandmarks.landmark[19].y and
                         handlandmarks.landmark[8].y < handlandmarks.landmark[4].y and
                         distance > 120):
                         pass
                         #print("Empty hand!")
    
