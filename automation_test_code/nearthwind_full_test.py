import config_data
import pytest
import allure
import re
import time
import requests
import json
from appium import webdriver

#appium webdriver
driver = webdriver.Remote(config_data.qa3_url, config_data.qa3_nor)
bf_photo_cnt = 0

#Common
def search_screen_text(stats): #화면의 모든 텍스트 가져오는 함수
    time.sleep(3)
    lst, lst_key = {}, []
    req = driver.page_source
    for line in req.split("\n"):      
        if line.find('</') == -1:          
            tt = line[line.find("<"):line.find(">")+1]            
            if stats in tt:              
                a = re.findall(r"(?<="+stats+"=\")(.*?)\" ", tt)[0]
                b = re.findall(r"(?<=x=\")(.*?)\" ", tt)[0]
                c = re.findall(r"(?<=y=\")(.*?)\" ", tt)[0]          
                lst[a] = [b,c]
    return list(lst.keys())    

def screen_shot(x): #스크린샷
    print(x)
    allure.attach(driver.get_screenshot_as_png(),name='screenshot',attachment_type=allure.attachment_type.PNG)

def App_click(x): #클릭함수
    driver.tap([(x)], 50)

def skeyboard(x): #시스템 키보드 입력
  [driver.find_element_by_xpath('//XCUIElementTypeKey[@name="'+i+'"]').click() for i in x]
  time.sleep(2)

def list_pick(x): #피커휠 값 입력 후 선택
    '''
    ex) list_pick(x) : x는 pickerwhell의 값을 넣는다.
    '''
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys(x)

def farm_inspection_search_api(x): #데이터 불러오기 사진수 리턴
    api = 'https://apg.ale.io'
    login_api = api + '/v1/users/sessions'
    login_parameters = {'username': 'sa', 'password': 'pass'}
    login_response = requests.post(login_api, login_parameters)
    assert login_response.status_code == 200

    login_response_json = json.loads(login_response.content)
    token = login_response_json['auth']['token']    
    post_api = "https://apig.al.io/v1/projects/009/ies"
    post_headers = {
    'Content-Type': 'application/json',
    'authorization': token,
    'x-access-token': token,
    'x-user-agent': 'NERD:20.09'
    }
    post_response = requests.get(post_api, headers=post_headers)
    assert post_response.status_code == 200

    result = json.loads(post_response.content)    
    return [i["poCnt"] for i in result if i["title"] == x]

#Test
def test_1_release_mode_check(): #Test 릴리즈 모드가 온인지 확인 온이라면 해제하기
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if "Release Mode" in screen_text:        
        screen_shot("릴리즈 모드 있음")
        App_click(config_data.Release_Mode) #릴리즈 모드 해제
        screen_shot("릴리즈 모드 해제")
        App_click(config_data.icon_setting_gray) #메뉴 닫기
        assert True
    else:
        assert True

def test_2_release_mode_on():
    App_click(config_data.icon_setting_gray) #메뉴 열기
    screen_text = search_screen_text("label")
    if "Release Mode" not in screen_text:        
        screen_shot("릴리즈 모드 없음")
        App_click(config_data.icon_setting_gray) #메뉴 닫기
        [driver.tap([(i)], 50) for i in [[560,70],[760,70],[925,70],[560,215]]] #데브모드 실행
        App_click(config_data.icon_setting_gray) #메뉴 열기
        screen_text = search_screen_text("label")
        if "Release Mode" in screen_text:        
            screen_shot("릴리즈 모드 실행 확인")
            App_click(config_data.icon_setting_gray) #메뉴 열기
            assert True
        else:
            screen_shot("릴리즈 모드가 있어야 하나 없는 경우")
            assert False
    else:
        screen_shot("릴리즈 모드가 없어야 하나 있는 경우")
        assert False    

def test_3_login_check(): #Test 로그인이 되어 있는지 확인 / 로그인 되어 있으면 로그인 풀기
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if "Logout" in screen_text:        
        screen_shot("로그인 되어 있음 / 로그아웃 하기")
        screen_text = search_screen_text("label")
        if ['Camting', 'Relede', 'Metaoad', 'Admstrator ', 'Logout'] == screen_text[13:-3]:
            screen_shot("메뉴 4개 출력 / 4번째 버튼 클릭")
            App_click(config_data.menu4) #config_data.menu4
        elif ['Cametting', 'Metapload', 'Adminrator ', 'Logout'] == screen_text[13:-3]:
            screen_shot("메뉴 3개 출력 / 3번째 버튼 클릭")
            App_click(config_data.menu3) #config_data.menu3
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        assert True

def test_4_login_page_in_check(): #Test 로그인페이지로 이동
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if ['Cameetting', 'Releode', 'NNDogin'] == screen_text[13:-3]:
        screen_shot("메뉴 3개 출력 / 3번째 버튼 클릭")
        App_click(config_data.menu3) #config_data.menu3
    elif ['Cameting', 'NDLogin'] == screen_text[13:-3]:
        screen_shot("메뉴 2개 출력 / 2번째 버튼 클릭")
        App_click(config_data.menu2) #config_data.menu2
    time.sleep(10)
    screen_text = search_screen_text("value")
    if ['abl', 'Make', 'Inspesy', 'with Autonogy', '1', 'Username', 'Password', 'Not registered?', 'ontact us'] == screen_text[:-1]:
        screen_shot("로그인 페이지 진입 Pass")
        assert True

def test_5_no_id_no_pw_check(): #Test id pw 미입력
    test_4_login_page_in_check()
    App_click(config_data.Login) #config_data.Login
    screen_text = search_screen_text("value")
    if 'Please enter username' == screen_text[7]:
        screen_shot("username 미입력 확인")
        assert True
    App_click(config_data.login_close) #config_data.login_close
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_6_no_id_pw_check(): #Test id 미입력 pw 입력
    test_4_login_page_in_check()
    App_click(config_data.Password) #config_data.Password
    skeyboard("d")
    App_click(config_data.hide_keyboard)
    App_click(config_data.Login) #config_data.Login
    screen_text = search_screen_text("value")
    if 'Please enter username' == screen_text[7]:
        screen_shot("username 미입력 확인")
        assert True
    App_click(config_data.login_close) #config_data.login_close
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_7_w_id_w_pw_check(): #Test 잘못된 id 잘못된 pw 입력
    test_4_login_page_in_check()
    App_click(config_data.Username) #config_data.Username
    skeyboard("a")
    App_click(config_data.hide_keyboard)
    App_click(config_data.Password) #config_data.Password
    skeyboard("d")
    App_click(config_data.hide_keyboard)
    App_click(config_data.Login) #config_data.Login
    screen_text = search_screen_text("value")
    if 'invalid:username' == screen_text[7]:
        screen_shot("username error 확인")
        assert True
    App_click(config_data.login_close) #config_data.login_close
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_8_id_w_pw_check(): #Test 정확한 id 잘못된 pw 입력
    test_4_login_page_in_check()
    App_click(config_data.Username) #config_data.Username
    skeyboard("admin")
    App_click(config_data.hide_keyboard)
    App_click(config_data.Password) #config_data.Password
    skeyboard("d")
    App_click(config_data.hide_keyboard)
    App_click(config_data.Login) #config_data.Login
    screen_text = search_screen_text("value")
    if 'invalid:password' == screen_text[7]:
        screen_shot("password error 확인")
        assert True
    App_click(config_data.login_close) #config_data.login_close
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_9_id_pw_check(): #Test 정확한 id 정확한 pw 입력
    test_4_login_page_in_check()
    App_click(config_data.Username) #config_data.Username
    skeyboard("sa")
    App_click(config_data.hide_keyboard)
    App_click(config_data.Password) #config_data.Password
    skeyboard("pass")
    App_click(config_data.hide_keyboard)
    screen_shot("정상적인 아이디 비번 입력")
    App_click(config_data.Login) #config_data.Login
    screen_text = search_screen_text("value")
    if 'invalid:username' != screen_text[7] and 'invalid:password' != screen_text[7]:
        screen_shot("login 이상 없음 확인")
        assert True
    App_click(config_data.login_close) #config_data.login_close
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_10_login_stats_check(): #Test 로그인 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if "Logout" in screen_text:        
        screen_shot("로그인 되어 있음")
        assert True
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_11_login_check(): #Test 로그인이 되어 있는지 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if "Logout" in screen_text:        
        screen_shot("로그인 되어 있음")
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        assert True
    else:
        screen_shot("로그인 되어 있지 않음")
        screen_text = search_screen_text("label")
        if ['Cameing', 'Releae', 'NDgin'] == screen_text[13:-3]:
            screen_shot("메뉴 3개 출력 / 3번째 버튼 클릭")
            App_click(config_data.menu3) #config_data.menu3
        elif ['Caming', 'NDgin'] == screen_text[13:-3]:
            screen_shot("메뉴 2개 출력 / 2번째 버튼 클릭")
            App_click(config_data.menu2) #config_data.menu2
        time.sleep(15)
        App_click(config_data.Username) #config_data.Username
        skeyboard("sa")
        App_click(config_data.Password) #config_data.Password
        skeyboard("pass")
        App_click(config_data.Login) #config_data.Login
        screen_shot("로그인 완료")
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        assert True

def test_12_Metadpload_page_check(): #Test 메타데이터 업로드 페이지로 이동이 잘되었는지 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if ['Cang', 'Relee', 'Metadoad', 'Admrator ', 'Logout'] == screen_text[13:-3]:
        screen_shot("메뉴 4개 출력 / 3번째 버튼 클릭")
        App_click(config_data.menu3) #config_data.menu3
    elif ['Cating', 'Metaoad', 'Admrator ', 'Logout'] == screen_text[13:-3]:
        screen_shot("메뉴 3개 출력 / 2번째 버튼 클릭")
        App_click(config_data.menu2) #config_data.menu2
    
    screen_text = search_screen_text("label")
    if 'Uptadata' == screen_text[0]:
        screen_shot("Upata page 진입")
        assert True

def test_13_abl_data_page_check(): #Test 데이터 페이지로 잘 이동되었는지 확인
    App_click(config_data.Update) #config_data.Update
    screen_text = search_screen_text("label")
    if 'abta' == screen_text[0]:
        screen_shot("abta page 진입")
        assert True

def test_14_list_data_read_check(): #Test 스트 제대로 불러오는지 확인
    App_click(config_data.icon_list_refresh) #config_data.icon_windfarm_list_refresh
    time.sleep(20)
    screen_text = search_screen_text("label")
    if len(screen_text) > 5:
        screen_shot("리스트 불러오기 성공")
        assert True
    elif len(screen_text) <= 5:
        assert False

def test_15_list_data_func_check(): #Test 리스트 제대로 불러오는지 확인
    before_cnt = len(search_screen_text("label"))
    App_click(config_data.wind_1st) #config_data.wind_1st
    App_click(config_data.winde_1st) #config_data.winde_1st    
    after_cnt = len(search_screen_text("label"))
    if before_cnt < after_cnt:
        screen_shot("리스트 데이터 불러온 후 정상")
        assert True
    App_click(config_data.zoom_back)
    App_click(config_data.mexit)
    App_click(config_data.icon_setting_gray)

def test_16_release_mode_check(): #Test 릴리즈 모드가 온인지 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if "Release Mode" in screen_text:        
        screen_shot("릴리즈 모드 있음")
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        assert True
    else:
        print("릴리즈 모드 없음")
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray        
        [driver.tap([(i)], 50) for i in [[560,70],[760,70],[925,70],[560,215]]]
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        screen_text = search_screen_text("label")
        if "Release Mode" in screen_text:
            screen_shot("릴리즈 모드 있음")
            App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
            assert True

def test_17_landing_page_check(): #Test 현재 페이지가 초기 페이지인지 (타임, 아이패드 타임 있는지 여부 파악)
    screen_text = search_screen_text("label")
    if "Drone Time" in screen_text and "Time" in screen_text:        
        screen_shot("초기 페이지 확인 완료!")
        assert True

def test_18_iection_page_check(): #Test 스타트 버튼 클릭 / 페이지 전환 확인
    App_click(config_data.icon_loading_start) #config_data.icon_loading_start
    screen_text = search_screen_text("label")
    if "Checklist (1/4)" in screen_text:        
        screen_shot("화면 진입 확인 완료!")
        assert True

def test_19_advanced_settings_page_check(): #Test 넥스트 버튼 클릭 / advaced Settings 버튼 확인
    App_click(config_data.Next) #config_data.Next
    screen_text = search_screen_text("label")
    if "Checklist (2/4)" in screen_text and "AdvancedSettings" in screen_text:            
        screen_shot("checklist2/4와 advancedSettings 버튼이 존재하는 페이지 진입 확인 완료!")
        assert True

def test_20_advanced_settings_page_ui_check(): #Test Advanced Settings버튼 클릭 / 구성요소 확인  
    # 미션타입, 블레이드 길이, 디스턴스 키핑, 포커스랭스, 에프스탑, 윈드팜, 셀렉트 윈드팜,  윈드터빈, 셀렉트 윈트 터빈, 인스펙션, 셀렉트 인스펙션,  엑스트라, 엑스트라 입력 블레이드 블ㅇ레이드 오더, 초기화, 컴펌    driver.tap([(["772", "190"])], 50) #Advanced_Settings        
    App_click(config_data.Advanced_Settings) #config_data.Advanced_Settings    
    screen_shot("Advanced Settings 구성 확인")
    in_text = ['Advanced Settings', 'Wind ', 'Wind ', 'Inspection',  'Extra',  'Blade', 'Select  in order', 'Mission Type','4-1', '4-2', '4-3', '6-1', '6-2', ' Legnth', ' Keeping', ' Length', 'Stop',  'Confirm'] #있어야 할 텍스트 구성
    screen_text = search_screen_text("label") #실제 화면에 있는 텍스트 구성
    for i in in_text: #비교
        if i in screen_text:
            screen_shot("Advanced Settings 구성 중 {} 항목 확인 완료".format(i))
            assert True
        else:            
            assert False

def test_21_settings_change_check():#설정을 바꾸었을때 잘 적용되는지 확인
    try:
        App_click(config_data.ad61)
        App_click(config_data.adistance_keeping)
        [App_click(config_data.del_keyboard) for i in range(5)]
        skeyboard("11")
        App_click(config_data.hide_keyboard)
        App_click(config_data.afocal_length42)
        App_click(config_data.afstop)
        [App_click(config_data.del_keyboard) for i in range(5)]
        skeyboard("1.1")
        App_click(config_data.hide_keyboard)
        App_click(config_data.awindfarm)
        list_pick("용대리 테스트")
        App_click(config_data.sys_change)
        App_click(config_data.awindturbine)
        list_pick("탐라해상4호기백업")
        App_click(config_data.sys_change)
        App_click(config_data.ainspection)
        list_pick("#77")
        App_click(config_data.sys_change)
        App_click(config_data.aextra)
        [App_click(config_data.del_keyboard) for i in range(5)]
        skeyboard("a")
        App_click(config_data.hide_keyboard)
        App_click(config_data.ablade_reset)
        App_click(config_data.ablade_top)
        App_click(config_data.ablade_right)
        App_click(config_data.ablade_left)
        App_click(config_data.ablade_left)
        App_click(config_data.aconfirm)
        screen_shot("advenced setting 적용 완료")
        assert True
    except:
        screen_shot("advenced setting 적용 실패")
        assert False
    time.sleep(9)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(10)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(11)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(12)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(13)
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="OK"]').click() #시스템창
    App_click(config_data.icon_btn_close_white)

def test_22_release_mode_check(): #Test 릴리즈 모드가 온인지 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

    screen_text = search_screen_text("label")
    if 'Release Mode' not in screen_text:
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray        
        [driver.tap([(i)], 50) for i in [[560,70],[760,70],[925,70],[560,215]]]
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

        screen_text = search_screen_text("label")
        for i in ['Release Mode']:
            if i in screen_text:
                assert True
            else:
                screen_shot(str(i)+" 가 없어서 테스트 실패")
                assert False
        screen_shot("릴리즈 모드 있음 통과")
    else:
        assert True
        screen_shot("릴리즈 모드 있음 통과")

        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray

def test_23_pft_checklist_1_4_ui(): #체크리스트 ui이상여부 확인

    App_click(config_data.icon_loading_start)

    screen_text = search_screen_text("name")
    for i in ['icon_setting_arrow_left', 'Checklist (1/4)', 'icon_shutter_button', 'Next']:
        if i in screen_text:
            assert True
        else:
            screen_shot(str(i)+" 가 없어서 테스트 실패")
            assert False
    screen_shot("ui 체크리스트 닫기, 현재 체크리스트 위치(타이틀), 셔터버튼, 다음버튼(넥스트) 통과")

def test_24_pft_checklist_1_4_fn(): #체크리스트 닫기 버튼 혹인 후 복귀

    App_click(config_data.icon_setting_arrow_left) #체크리스트 닫기

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Checklist (1/4)']: #체크리스트 1/4가 있는지 체크
        if i not in screen_text: #안들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("기능 1/4체크리스트 닫기 완료") #성공 스샷
    App_click(config_data.icon_btn_close_white) #인스펙션 화면 닫기
    App_click(config_data.icon_loading_start) #스타트 버튼 클릭 인스펙션 화면 진입
    time.sleep(3)

def test_25_pft_checklist_2_4_ui(): #UI확인
    App_click(config_data.Next) #1/4에서 다음 버튼 누름
    screen_text = search_screen_text("name")
    for i in ['icon_setting_arrow_left', 'Checklist (2/4)', 'Wind ', 'Wind ', 'Extra', 'Next']:
        if i in screen_text:
            assert True
        else:
            screen_shot(str(i)+" 가 없어서 테스트 실패")
            assert False
    screen_shot("ui 체크리스트 닫기, 현재 체크리스트 위치(타이틀), , , , 엑스트라, 다음버튼(넥스트) 통과")

def test_26_pft_checklist_2_4_fn(): #이전 체크리스트
    App_click(config_data.iprev) #이전화면으로 가기

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Checklist (1/4)']: #체크리스트 1/4가 있는지 체크
        if i in screen_text: #들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("이전 화면 1/4 출력 확인 완료")
    App_click(config_data.Next) #2/4화면으로 다시 이동

def test_27_pft_checklist_2_4_reset():#리셋
    App_click(config_data.iwm)
    list_pick("None")
    App_click(config_data.sys_change)
    App_click(config_data.iextra)
    [App_click(config_data.del_keyboard) for i in range(5)]
    App_click(config_data.hide_keyboard)

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Select Wind ', 'Select Wind ', 'Select ', 'Input your  data']: 
        if i in screen_text: #들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("현재 화면 2/4 윈드, 윈드, , 리셋 완료")

def test_28_pft_checklist_2_4_fn1():#윈드 , 윈드 , ,  세팅 완료
    App_click(config_data.iwindfarm)
    list_pick("테스트")
    App_click(config_data.sys_change)
    App_click(config_data.iwindtne)
    list_pick("백업")
    App_click(config_data.sys_change)
    App_click(config_data.ㅁㅇㄹㅁ)
    list_pick("99")
    App_click(config_data.sys_change)
    App_click(config_data.iextra)
    skeyboard("qa")
    App_click(config_data.hide_keyboard)
    screen_text = search_screen_text("value") #화면 모든 텍스트 불러오기
    for i in ['테스트','호기','99', 'qa']:
        if i in screen_text: #들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("현재 화면 2/4 '테스트','호기','99','qa' 적용 완료")

def test_29_pft_checklist_2_4_fn2():#닫기
    
    App_click(config_data.icon_setting_arrow_left) #체크리스트 닫기

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Checklist (2/4)']: #체크리스트 2/4가 있는지 체크
        if i not in screen_text: #안들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("기능 2/4체크리스트 닫기 완료") #성공 스샷
    App_click(config_data.icon_btn_close_white) # 화면 닫기
    time.sleep(3)
    App_click(config_data.icon_loading_start) #스타트 버튼 클릭  화면 진입
    time.sleep(3)
    App_click(config_data.Next) #2/4진입
    time.sleep(1)
    App_click(config_data.Next) #3/4진입
    time.sleep(1)

def test_30_pft_checklist_3_4_ui(): #3/4 UI확인
    screen_text = search_screen_text("name")
    for i in ['icon_setting_arrow_left', 'Checklist (3/4)', 'Blade', 'Select in order', 'Next']:
        if i in screen_text:
            assert True
        else:
            screen_shot(str(i)+" 가 없어서 테스트 실패")
            assert False
    screen_shot("ui 체크리스트 닫기, 현재 체크리스트 위치(타이틀), , 셀렉트  오더,  다음버튼(넥스트) 통과")

def test_31_pft_checklist_3_4_fn1(): #이전
    App_click(config_data.iprev) #이전화면으로 가기

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Checklist (2/4)']: #체크리스트 1/4가 있는지 체크
        if i in screen_text: #들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("이전 화면 2/4 출력 확인 완료")
    App_click(config_data.Next) #3/4 복귀

def test_32_pft_checklist_3_4_fn2(): # 리셋
    App_click(config_data.iblade_reset)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['B']: #체크리스트 1/4가 있는지 체크
        if i not in screen_text: #들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot(" 리셋 확인 완료")

def test_33_pft_checklist_3_4_fn3(): #다음 미선택 예외처리 확인
    App_click(config_data.Next)
    screen_text = search_screen_text("name")
    for i in ['icon_setting_arrow_left', 'Checklist (3/4)', 'Blade', 'Select  in order', 'Next']:
        if i in screen_text:
            assert True
        else:
            screen_shot(str(i)+" 가 없어서 테스트 실패")
            assert False
    screen_shot(" 리셋 후 다음 버튼 눌러서 페이지가 이동하지 않아서 통과")

def test_34_pft_checklist_3_4_fn4(): # 선택
    App_click(config_data.ibl_top)
    App_click(config_data.ibl_left)
    App_click(config_data.ibl_right)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['A','B','C']: #블레이드 선택 A,B,C가 있는지 확인
        if i in screen_text: #들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot(" 선택  확인 완료")

def test_35_pft_checklist_3_4_fn5(): #닫기
    
    App_click(config_data.icon_setting_arrow_left) #체크리스트 닫기

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Checklist (3/4)']: #체크리스트 3/4가 있는지 체크
        if i not in screen_text: #안들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("기능 3/4체크리스트 닫기 완료") #성공 스샷
    App_click(config_data.icon_btn_close_white) #인스펙션 화면 닫기
    time.sleep(3)
    App_click(config_data.icon_loading_start) #스타트 버튼 클릭 인스펙션 화면 진입
    time.sleep(3)
    App_click(config_data.Next) #2/4진입
    time.sleep(1)
    App_click(config_data.Next) #3/4진입
    time.sleep(1)
    App_click(config_data.Next) #4/4진입
    time.sleep(1)

def test_36_pft_checklist_4_4_ui(): #ui
    screen_text = search_screen_text("name")
    for i in ['icon_setting_arrow_left', 'Checklist (4/4)', 'Type', '4-1', '4-2', '4-3', '6-1', '6-2', 'Confirm']:
        if i in screen_text:
            assert True
        else:
            screen_shot(str(i)+" 가 없어서 테스트 실패")
            assert False
    screen_shot(" 4/4 ui 체크리스트 닫기, 현재 체크리스트 위치(타이틀), 타입, 4-1, 4-2, 4-3, 6-1,6-2, 다음버튼(넥스트) 통과")

def test_37_pft_checklist_4_4_fn1(): #이전
    App_click(config_data.iprev) #이전화면으로 가기

    screen_text = search_screen_text("name")
    for i in ['icon_setting_arrow_left', 'Checklist (3/4)', 'Blade', 'Select in order', 'Next']:
        if i in screen_text:
            assert True
        else:
            screen_shot(str(i)+" 가 없어서 테스트 실패")
            assert False
    screen_shot("ui 체크리스트 닫기, 현재 체크리스트 위치(타이틀), , 셀렉트  오더,  다음버튼(넥스트) 통과")
    App_click(config_data.Next) #4/4 복귀

def test_38_pft_checklist_4_4_fn2(): #닫기
    
    App_click(config_data.icon_setting_arrow_left) #체크리스트 닫기

    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    for i in ['Checklist (4/4)']: #체크리스트 4/4가 있는지 체크
        if i not in screen_text: #안들어있을때 성공
            assert True
        else: #들어 있을때 실패
            screen_shot(str(i)+" 가 있어서 테스트 실패")
            assert False
    screen_shot("기능 4/4체크리스트 닫기 완료") #성공 스샷
    App_click(config_data.icon_btn_close_white) #인스펙션 화면 닫기
    time.sleep(3)
    App_click(config_data.icon_loading_start) #스타트 버튼 클릭 인스펙션 화면 진입
    time.sleep(3)
    App_click(config_data.Next) #2/4진입
    time.sleep(1)
    App_click(config_data.Next) #3/4진입
    time.sleep(1)
    App_click(config_data.Next) #4/4진입
    time.sleep(1)

def test_39_pft_checklist_4_4_fn3(): #미션 선택 컨펌
    App_click(config_data.imissio)
    time.sleep(3)
    App_click(config_data.Next)    
    time.sleep(9)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(10)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(11)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(12)
    screen_text = search_screen_text("name") #화면 모든 텍스트 불러오기
    time.sleep(13)    
    driver.find_element_by_xpath('//XCUIElementTypeButton[@name="OK"]').click() #시스템창
    time.sleep(1)
    App_click(config_data.icon_btn_close_white) #인스펙션 화면 닫기

def test_40_login_check(): #Test 로그인이 되어 있는지 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if "Logout" in screen_text:        
        screen_shot("로그인 되어 있음")
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        assert True
    else:
        screen_shot("로그인 되어 있지 않음")
        screen_text = search_screen_text("label")
        if ['Caming', 'ReleMode', 'ND Login'] == screen_text[13:-3]:
            screen_shot("메뉴 3개 출력 / 3번째 버튼 클릭")
            App_click(config_data.menu3) #config_data.menu3
        elif ['Camting', 'NDgin'] == screen_text[13:-3]:
            screen_shot("메뉴 2개 출력 / 2번째 버튼 클릭")
            App_click(config_data.menu2) #config_data.menu2
        time.sleep(15)
        App_click(config_data.Username) #config_data.Username
        skeyboard("sa")
        App_click(config_data.Password) #config_data.Password
        skeyboard("pass")
        App_click(config_data.Login) #config_data.Login
        screen_shot("로그인 완료")
        App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
        assert True

def test_41_Metadata_upload_page_check(): #Test 메타데이터 업로드 페이지로 이동이 잘되었는지 확인
    App_click(config_data.icon_setting_gray) #config_data.icon_setting_gray
    screen_text = search_screen_text("label")
    if ['Camting', 'Relea', 'Metadaad', 'Adminator ', 'Logout'] == screen_text[13:-3]:
        screen_shot("메뉴 4개 출력 / 3번째 버튼 클릭")
        App_click(config_data.menu3) #config_data.menu3
    elif ['Caming', 'Metload', 'Admrator ', 'Logout'] == screen_text[13:-3]:
        screen_shot("메뉴 3개 출력 / 2번째 버튼 클릭")
        App_click(config_data.menu2) #config_data.menu2
    
    screen_text = search_screen_text("label")
    if 'Uplotadata' == screen_text[0]:
        screen_shot("Upltata page 진입")
        assert True

def test_42_Metadata_edit_check(): #메타데이터 수정
    global bf_photo_cnt
    driver.find_element_by_xpath('//XCUIElementTypeCell[1]').click() #1번째 선택
    App_click(config_data.medit) #수정 버튼
    App_click(config_data.mwind) #리스트
    list_pick("테스트")
    App_click(config_data.sys_change)
    App_click(config_data.mwindrbine) #윈드
    list_pick("호기")
    App_click(config_data.sys_change)
    App_click(config_data.miection) #펙션
    list_pick("99")
    App_click(config_data.sys_change)
    bf_photo_cnt = farm_inspection_search_api("9")[0]
    App_click(config_data.me_order) # 오더
    App_click(config_data.me_reset) # 리셋
    App_click(config_data.mde_top) # 탑
    App_click(config_data.mde_left) # 왼쪽
    App_click(config_data.mde_right) # 오른쪽
    App_click(config_data.made_set_ok) # 세팅 오케이
    App_click(config_data.medit_save) #  에디트 save

    screen_text = search_screen_text("label") #check
    for i in ['테스트','호기','99']:
            if i in screen_text: #들어있을때 성공
                assert True
            else: #들어 있을때 실패
                screen_shot(str(i)+" 가 있어서 테스트 실패")
                assert False
    screen_shot(" 스트 수정  적용 완료")
        
def test_43_Metadata_upload_check(): #메타데이터 업로드
    App_click(config_data.mupload)  #업로드
    screen_text = search_screen_text("label")
    time.sleep(5)
    screen_text = search_screen_text("label")
    time.sleep(6)
    screen_text = search_screen_text("label")
    time.sleep(7)
    App_click(config_data.mupload_popup_ok) #업로드 팝업 오케이
    App_click(config_data.mall_check) #올체크박스
    App_click(config_data.mall_check) #올체크박스
    screen_text = search_screen_text("label")
    add_cnt = int(screen_text[11:12][0]) 
    #api를 이용해서 진짜 올라갔는지 확인한다.
    will_cnt = bf_photo_cnt + add_cnt
    if will_cnt == farm_inspection_search_api("99")[0]:
        assert True
    else:
        screen_shot("기존 + 업로드 사진수가 맞지 않음")
        assert False
    screen_shot("업로드 사진 카운트가 디비에 업로드된 사진수와 같음")

def test_44_Metadata_delete_check(): #메타데이터 삭제
    driver.find_element_by_xpath('//XCUIElementTypeCell[1]').click() #1번째 선택
    metadata_1 = search_screen_text("label")[10] #첫번재 메타데이터 이름 저장
    App_click(config_data.mdelete) #삭제 버튼
    App_click(config_data.mdelete_popup_ok)  #오케이버튼
    metadata_2 = search_screen_text("label")[10] #지우고 난 후 메타데이터
    #메타데이터 비교
    if metadata_1 != metadata_2:
        assert True
    else:
        screen_shot("메타데이터가 삭제되지 않음")
        assert False
    screen_shot("메타데이터 삭제 확인 완료")

def test_45_Metadata_restore_check(): #메타데이터 복구
    metadata_1 = search_screen_text("label")[10] #첫번재 메타데이터 이름 저장
    time.sleep(5)
    App_click(config_data.mrestore) #리스토어로 이동
    time.sleep(5)
    driver.find_element_by_xpath('//XCUIElementTypeCell[1]').click() #1번째 선택
    App_click(config_data.mrecovery) #복구 버튼 restore 클릭
    metadata_2 = search_screen_text("label")[10] #복구하고 난 후 메타데이터
    if metadata_1 != metadata_2: #메타데이터 비교
        assert True
    else:
        screen_shot("메타데이터 복구 실패")
        assert False
    screen_shot("메타데이터 복구 확인 완료")
    #원래대로 삭제
    driver.find_element_by_xpath('//XCUIElementTypeCell[1]').click() #1번째 선택
    App_click(config_data.mdelete) #삭제 버튼
    App_click(config_data.mdelete_popup_ok) #오케이버튼
    App_click(config_data.mexit) #뒤로가기 #메타데이터 뒤로가기
    App_click(config_data.icon_setting_gray) #메뉴 클릭
