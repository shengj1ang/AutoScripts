import undetected_chromedriver as webdriver
import time

# 创建一个Chrome浏览器实例
browser = webdriver.Chrome()

# 打开网页
browser.get('https://www.gov.uk/change-driving-test')

time.sleep(2)

browser.get('https://driverpracticaltest.dvsa.gov.uk/login')


input("")


# 关闭浏览器
browser.quit()
