# 외우는거 아님. 그냥 필요할 때 복붙
import time
import os
import pyperclip

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('no-sandbox') #tab 액션 가능
#chrome_options.add_argument('headless') #창 안띄움

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get('https://home.tmon.co.kr/') # 네이버, 쿠팡은 막힘

def find(wait, css_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))) #상호작용 할 수 있는게 보이느냐
    #return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))) #elemnet 가 있느냐

login_button = find(wait, 'a.login')
login_button.click()

input_id = find(wait, 'input#userid')
pyperclip.copy('티몬 아이디')
input_id.send_keys(Keys.COMMAND, 'v')

input_pw = find(wait, 'input#pwd')
pyperclip.copy('티몬 비번')
input_pw.send_keys(Keys.COMMAND, 'v')
input_pw.send_keys('\n')

time.sleep(3)

# search = find(wait, 'input[name=keyword]')
# search.send_keys('아이폰 케이스\n')
# button = find(wait, 'a.search')
# button.click()

chrome.close()