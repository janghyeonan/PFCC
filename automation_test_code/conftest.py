#Created by An Janghyun

import re
import json
import pytest
import allure
import datetime
import requests
import test_data as td
from time import sleep
from bs4 import BeautifulSoup
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


#pytest 공통 함수

@pytest.fixture(scope="module")
def driver():
    '''
    :qa1을 실행시켜주는 driver 함수이다.
    '''
    driver = webdriver.Remote(td.dev2_url, td.dev_ipa)

    bright_up(driver)
    driver.find_element_by_id("확인").click()
    qcl(driver, "vl_btn_start")
    sleep(3)
    driver.find_element_by_id("앱을 사용하는 동안 허용").click()
    driver.tap([(list(driver.find_element_by_accessibility_id("ChecklistViewPro_btn_back").location.values()))],50)
    sleep(3)
    driver.tap([(list(driver.find_element_by_accessibility_id("VCInspection_btn_close").location.values()))],50)
    sleep(3)
    [driver.tap([([x+y for x,y in zip(list(driver.find_element_by_accessibility_id("vl_btn_test_password_"+str(i)).location.values()),[100, 70])] )],50) for i in range(1, 5)]
    
    yield driver
    
    driver.quit()

@pytest.fixture(scope="module")
def driver2():
    '''
    :qa3을 실행시켜주는 driver 함수이다.
    '''
    driver = webdriver.Remote(td.qa2_url, td.qa2_nor)

    bright_up(driver)
    driver.find_element_by_id("확인").click()
    qcl(driver, "vl_btn_start")
    sleep(3)
    driver.find_element_by_id("앱을 사용하는 동안 허용").click()
    driver.tap([(list(driver.find_element_by_accessibility_id("ChecklistViewPro_btn_back").location.values()))],50)
    sleep(3)
    driver.tap([(list(driver.find_element_by_accessibility_id("VCInspection_btn_close").location.values()))],50)
    sleep(3)
    [driver.tap([([x+y for x,y in zip(list(driver.find_element_by_accessibility_id("vl_btn_test_password_"+str(i)).location.values()),[100, 70])] )],50) for i in range(1, 5)]
    
    yield driver
    
    driver.quit()

def bright_up(x): 
    '''
    :아이패드 밝기를 올려주는 함수 bright_up(driver)
    d = driver
    '''
    TouchAction(x).press(x=1000.0,y=0.0).wait(50).move_to(x=1000.0,y=50.0).release().perform() #좌측 사이드바 내리기
    z = 0
    if x.get_window_size()["height"] > 768:
        z = 256
    TouchAction(x).press(x=885.0,y=345.0+z).wait(100).move_to(x=885.0,y=150.0+z).release().perform() #화면 밝기 내리기 한번에
    sleep(1)
    if z == 0:
        TouchAction(x).press(x=1024.0,y=768.0).wait(50).move_to(x=1024.0,y=718.0).release().perform() #사이드바 올리기
    else:
        TouchAction(x).press(x=1000.0,y=0.0).wait(50).move_to(x=1000.0,y=50.0).release().perform() #좌측 사이드바 내리기

def qcl(d, x): # 한개면 바로 클릭, 2개 이상이면, 1024, 768 미만인것만 클릭하기, 그리고 좌표를 따지면 +10씩 더 더해주기
    print("> " + x)
    sleep(1)
    lst = d.find_elements_by_accessibility_id(x)
    cnt = len(lst)
    if cnt == 1:
        list1 = list(d.find_element_by_accessibility_id(x).location.values())
        if int(list1[0]) <= 1024 and int(list1[1]) <= 768:
            print([x+y for x,y in zip(list1, [10, 10])])
            d.tap([([x+y for x,y in zip(list1, [10, 10])])],50)
    elif cnt >= 2:
        try:
            temp_xy = ""
            for i in d.find_elements_by_accessibility_id(x):
                xy = list(i.location.values())
                if temp_xy != xy:
                    print("이전내용과 달라서 클릭.")
                    if int(xy[0]) <= 1024 and int(xy[1]) <= 768:
                        print([x+y for x,y in zip(xy, [10, 10])])
                        d.tap([([x+y for x,y in zip(xy, [10, 10])])],50)
                        temp_xy = xy
                else:
                    print("이전과 같아서 클릭하지 않음.")
                    temp_xy = xy
        except:
            pass
    sleep(1)

def get_value(x):
    '''
    :앱의 현재 페이지의 vlue값을 전부 가져와서 리스트로 리턴해 준다.
    d = driver
    '''
    lst = []
    req = x.page_source
    sleep(10)
    for line in req.split("\n"):
        if line.find('</') == -1:
            tt = line[line.find("<"):line.find(">")+1]
            if "value" in tt:
                lst.append(re.findall(r"(?<=value=\")(.*?)\" ", tt)[0])
    lst = list(set(lst))
    return lst

def q_assert(x, y, z, txt):
    '''
    스크린샷을 찍고 검증을 하는 함수
    파라미터(driver, 검증대상, 비교대상, 에러시 텍스트)
    '''
    allure.attach('<head></head><body>'+txt+" DT:" + str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))+' test result : <font color="blue">Pass</font> </body>', name=txt, attachment_type=allure.attachment_type.HTML)
    allure.attach(x.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    assert y  ==  z

def api_login():
    '''
    login api를 체크해서 접속 코드 및 토큰을 리턴해 주는 함수
    '''
    login_parameters = {'username': td.api_id, 'password': td.api_pw}
    login_response = requests.post(td.api_url+"/v1/users/sessions", login_parameters)
    code = login_response.status_code
    token = json.loads(login_response.content)['auth']['token']
    return  [code, token]

def api_farm():
    '''
    farm list api를 체크해서 접속 코드 및 팜리스트 개수를 리턴해 주는 함수
    ''' 
    post_api = 'https://apiging.ble.io/v1/projects?categories=true'
    token = api_login()[1]
    post_headers = {
    'Content-Type': 'application/json',
    'authorization': token,
    'x-access-token': token,
    'x-user-agent': 'NERD:20.09'}
    post_response = requests.get(post_api, headers=post_headers)    
    code = post_response.status_code
    result_cnt = len(json.loads(post_response.content))
    return [code, result_cnt]
    
def api_search_farm_inspectioni(x):
    '''
    api로 데이터 불러와서 해당 인스펙션에 사진수를 리턴해주는 함수
    '''
    token = api_login()[1]
    post_api = td.api_url + '/v1/projts/009/cagories'
    post_headers = {
    'Content-Type': 'application/json',
    'authorization': token,
    'x-access-token': token,
    'x-user-agent': 'NERD:20.09'
    }
    post_response = requests.get(post_api, headers=post_headers)
    result = json.loads(post_response.content)    
    return [i["photoCount"] for i in result if i["title"] == x]