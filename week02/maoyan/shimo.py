from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get('https://shimo.im/welcome')
    time.sleep(1)

    
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('********')
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('*******')
    time.sleep(1)
    browser.find_element_by_xpath('//button[contains(@class,"submit")]').click()

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    print('登录成功')
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()