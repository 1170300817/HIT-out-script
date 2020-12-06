# -*- encoding: utf-8 -*-
import time
import os

import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
alphabet = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()'

# 模拟浏览器打开网站
# browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
for i in range(8, 32):
    date_string = "2020年12月" + str(i) + "日"
    # 需要修改成自己的executable_path
    browser = webdriver.Chrome(options=chrome_options,
                               executable_path=r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    browser.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange')
    # 将窗口最大化
    browser.maximize_window()
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/button[1]').click()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[1]/input").send_keys(
        "********")  # 输入学号
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[2]/input[1]").send_keys(
        "*********")  # 输入密码
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/form/p[5]/button").click()

    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div[5]/a[3]").click()  # 出入校申请
    #
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[2]/a/div").click()  # 新增
    time.sleep(1)
    # browser.switch_to.alert.accept()
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[9]/div/label[1]").click()  # 勾选临时出校
    time.sleep(1)
    js = "document.getElementById('rq').removeAttribute('readonly')"
    browser.execute_script(js)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[13]/input").send_keys(date_string)  # 填写日期
    # 随机生成出校理由字符串
    characters = random.sample(alphabet, 10)
    browser.find_element_by_xpath("/html/body/div[1]/div/div[15]/textarea").send_keys(characters)  # 出校理由
    browser.find_element_by_xpath("/html/body/div[3]/div[1]/input").click()  # 勾选一堆东西
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/input").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[3]/input").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[4]/input").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[5]/input").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[6]/input").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[8]/input").click()
    browser.find_element_by_xpath("/html/body/div[3]/div[9]/input").click()
    browser.find_element_by_xpath("/html/body/div[6]").click()  # 提交
    # js = 'document.getElementByName("right_btn").click();' # 提交
    # browser.execute_script(js)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[10]/div[3]/a[2]").click()
    time.sleep(1)
    print(date_string + "出校申请成功")
    browser.quit()

os.system("taskkill /im chromedriver.exe /F")
os.system("taskkill /im chrome.exe /F")
