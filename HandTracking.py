import cv2 as cv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import keyboard
from hand_processing import HandProcessor

def load_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            credentials[key] = value
    return credentials
def start():
    credentials = load_credentials('twitter_credentials.txt')
    
    twitter_username = credentials['username']
    twitter_password = credentials['password']
    
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://twitter.com/login")
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "text")))
    
    input_username_by_name = driver.find_element(By.NAME, "text")
    input_username_by_name.send_keys(twitter_username)
    next_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
    next_button.click()
    '''
    next_button = driver.find_elements(By.XPATH, "//div[@role='button']")
    next_button[-1].click()
    '''
    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
    input_password = driver.find_element(By.NAME, "password")
    input_password.send_keys(twitter_password)
    
    log_in_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
    log_in_button.click()
    
    time.sleep(4)
    keyboard.press_and_release('j') #ilk tweete geç
    
    '''
    log_in_button = driver.find_element(By.XPATH, "//div[@data-testid = 'LoginForm_Login_Button']")
    log_in_button.click()
    '''
    
    camera = cv.VideoCapture(0)
    hand_processor = HandProcessor(driver)
    
    window_name = "WebCam"
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.setWindowProperty(window_name, cv.WND_PROP_TOPMOST, 1)
    
    while camera.isOpened():
        success, img = camera.read()
    
        rgbImage = hand_processor.bgr2RGB(img)
        hlms = hand_processor.handLandMarkModel(rgbImage)
    
        processed_like_func = hand_processor.like_func(hlms, img)
        processed_retweet_func = hand_processor.retweet_func(hlms, img)
        processed_scroll_down_func = hand_processor.scroll_down_func(hlms, img)
        processed_scroll_up_func = hand_processor.scroll_up_func(hlms, img)
        processed_bookmark_func = hand_processor.bookmark_func(hlms, img)
        processed_empty_func = hand_processor.empty_func(hlms, img)
        processed_comment_func = hand_processor.comment_func(hlms, img)
    
        cv.imshow("WebCam", processed_like_func)
    
    
        if cv.waitKey(1) & 0xFF == 27:
            break
    
    cv.destroyAllWindows()
    camera.release()