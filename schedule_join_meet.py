# py script to join meet with mic and audio turned off.
# This script uses chrome browser & chrome web driver to perform the task.
import time
# Needs selenium module to perform the task.
from selenium import webdriver
# Needs Options from selenium module to disable the unwanted permissions.
from selenium.webdriver.chrome.options import Options
# Needs schedule module to schedule the joining time of meet.
import schedule

def job():
  opt = Options()
  # Maximize chrome browser
  opt.add_argument("start-maximized")

  # Mic, camera, location and notifications are turned off.
  opt.add_experimental_option("prefs", {
      "profile.default_content_setting_values.media_stream_mic": 2, 
      "profile.default_content_setting_values.media_stream_camera": 2,
      "profile.default_content_setting_values.geolocation": 2, 
      "profile.default_content_setting_values.notifications": 2 
  })
  
  link = '_link_' # replace _link_ with your link
  browser = webdriver.Chrome(options=opt)
  browser.get(link)
  
  # increase the sleep time in case of slow internet connection to avoid stopping of script
  time.sleep(3)

  # fills the email id
  email = 'email_id' # replace email_id with your email id
  browser.find_element_by_id("i0116").send_keys(email)

  # clicks next
  browser.find_element_by_id("idSIButton9").click()
  time.sleep(2)

  # fills the password
  password = '_password_' # replace _password_ with your password
  browser.find_element_by_id("i0118").send_keys(password)
  time.sleep(3)

  # clicks on sign in
  browser.find_element_by_id("idSIButton9").click()
  time.sleep(3)

  # clicks on 'No' for stay sign in.
  browser.find_element_by_id("idBtn_Back").click()
  time.sleep(25)

  # clicks on the target link (the channel link)
  browser.find_element_by_class_name("team-name-text").click()
  time.sleep(15)

  # clicks on join button
  browser.find_element_by_class_name("ts-btn-primary").click()
  time.sleep(3)

  # clics on contiue without audio or video
  browser.find_element_by_class_name("ts-btn-fluent-secondary-alternate").click()
  time.sleep(3)

  # clicks on join now button (joins the meet)
  browser.find_element_by_class_name("ts-btn-primary").click()
  time.sleep(15)

  # Clicks on 3 dot menu
  browser.find_element_by_id("callingButtons-showMoreBtn").click()
  time.sleep(5)

  # switches to full screen
  browser.find_element_by_id("full-screen-button").click()

# set the time when you want to join the meet  
schedule.every().day.at("09:24").do(job)
schedule.every().day.at("11:24").do(job)
schedule.every().day.at("13:54").do(job)
schedule.every().day.at("14:31").do(job)

# you can specific day.
# schedule.every().monday.at("14:44").do(job)

 # Run the task
while True:
  schedule.run_pending()