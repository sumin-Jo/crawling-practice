from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
browser.get("http://naver.com") 
print(browser.title) 
browser.close()


# 위에는 도커를 사용하는 예제인데 아래와 같은 에러가 난다. 이게 뭘까...ㅠㅠ

# Traceback (most recent call last):
#   File "/Users/suminjo/Documents/crawling/root/exem/selenium/docker_test.py", line 4, in <module>
#     browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 186, in __init__
#     capabilities = options.to_capabilities()
#                    ^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'to_capabilities'