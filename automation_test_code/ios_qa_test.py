#Created by An Janghyun

import time
import random
import allure
import pytest
from conftest import *
from time import sleep
import test_data as td  #좌표가 들어 있는 파일

#test 1_file

@pytest.mark.api
@pytest.mark.parametrize('lst', td.test_api)
def test_api(lst): #test_api(td.test_api)
    '''<b>테스트 내용</b> : 3가지 API 정상여부 확인(login, farm list, farm list 개수)</br></br>
    <b>진행스탭</b></br>
    1. id, pw를 적어둔다.</br>
    2. https://apging.ole.io의 api를 이용하여 3가지(login, farm list, farm list 개수)를 확인한다.</br>
    3. 상태 코드를 확인한다.</br>
    4. 팜리스트 데이터 개수를 확인한다.</br></br>
    </br><b>기대결과</b> : 상태 코드값이 200이 되야 한다. 팜리스트 데이터 개수가 1개 이상이여야 한다.</br>    
    ''' 
    code ="" 
    if lst[0] =="farm_cnt":
        code = api_farm()[0]
        
        #검증
        assert code != 0, lst[1]
    else:
        code = api_login()[0]
        
        #검증
        assert code == 200, lst[1]    

def comment_tc():
    print("tc")
    #     '''<b>테스트 내용</b> :  로그인 페이지 입장 후 페이지 정상여부 확인</br></br>
    #     <b>진행스탭</b></br>
    #     1. 로그인을 한다.</br>
    #     2. 초기화면으로 이동한다.</br>
    #     3. 설정 메뉴를 확인한다.</br>
    #     </br><b>기대결과</b> : 설정메뉴 제일 하단에 로그아웃 버튼이 있어야 한다.</br>    
    #     ''' 
    #     #설정
    # @pytest.mark.login
    # @pytest.mark.parametrize('lst', td.account) 
    # def test_login_csae(driver, lst): 
    #     '''<b>테스트 내용</b> :  로그인 페이지에서 예외처리 적용 여부 확인</br></br>
    #     <b>진행스탭</b></br>
    #     1. 로그인창에 입장한다.</br>
    #     2. 다음과 같은 케이스를 입력하고 확인한다.</br>
    #     3. 계정 미입력, 비번 미입력</br>
    #     4. 계정 미입력, 비번 입력</br>
    #     5. 계정 입력, 비번 미입력</br>
    #     6. 계정 틀린거, 비번 틀린거</br>
    #     7. 계정 맞는거, 비번 틀린거</br>
    #     8. 계정맞는거, 비번 맞는거</br>
    #     </br><b>기대결과</b> : 계정 비밀번호 정상인것 외에 에러메시지가 출력되야 한다. </br>
    #     'Please enter username','Please enter password','invalid:username', 'invalid:password'가 출력되야 함 </br>
    #     ''' 
    #     login_page_in(driver)
    #     if lst[0] != None:        
    #         App_click(driver, td.Username)    
    #         skeyboard(driver, lst[0])
    #         App_click(driver, td.hide_keyboard)
    #     if lst[1] != None:        
    #         App_click(driver, td.Password)    
    #         skeyboard(driver, lst[1])
    #         App_click(driver, td.hide_keyboard)
    #     App_click(driver, td.Login)
    #     sleep(5)
    #     if lst[2] == "Logout":
    #         sleep(10)  
    #     #검증
    #     q_assert(driver, hashxpath(driver, lst[2]), True, lst[3])  
    #     login_page_out(driver)
    #     '''<b>테스트 내용</b> : 데이터페이지로 정상 이동 확인  </br></br>
    #     <b>진행스탭</b></br>
    #     1. 로그인 후 설정메뉴로 이동한다.</br>
    #     2. 설정메뉴에서 메타데이터 업로드 버튼을 누른다.</br>
    #     3. 메타데이터 페이지 진입 후 데이터 페이지 이동 버튼(Update) 클릭.</br>
    #     4. 페이지 확인 후 데이터 갱신 버튼 클릭</br>
    #     5. 데이터 출력 확인 후 윈드팜 하나 클릭</br>
    #     6. 윈드터빈 출력 후 해당 윈드터빈 클릭</br>
    #     7. 인스펙션 출력 확인 후 뒤로가기(닫기) 클릭</br>
    #     8. 메타데이터 페이지 이동 확인</br>
    #     9. 메타데이터 페이지에서 뒤로가기(닫기)버튼 클릭</br>
    #     10. 초기화면 입장 확인.</br>
    #     </br><b>기대결과</b> : 페이지 이동 후 팜리스트가 정상적으로 불러와져야 한다.</br>
    #     팜리스트 데이터가 정상 출력 확인되야 한다.</br> 
    #     초기화면으로 돌아가는 버튼기능이 정상적이여야 한다.</br>   
    #     '''

    #     '''<b>테스트 내용</b> : Checklist로 정상 이동 확인</br></br>
    #     <b>진행스탭</b></br>
    #     1. 초기화면에서 스타트 버튼 클릭.</br>
    #     2. Checklist (1/4)로 진입 확인(제목, 카메라셔터, 다음 버튼).</br> 
    #     3. 넥스트 버튼 클릭.</br>
    #     4. Checklist (2/4)로 진입 확인(제목, 엑스트라, 이전, 다음, 고급설정).</br> 
    #     5. 넥스트 버튼 클릭.</br>
    #     6. Checklist (3/4)로 진입 확인(제목, 고급설정, 날개 선택, 이전, 다음).</br> 
    #     7. 넥스트 버튼 클릭.</br>
    #     8. Checklist (4/4)로 진입 확인(제목, 고급설정, 미션타입, 미션버튼, 이전, 컨펌).</br> 
    #     9. 컨펌 버튼 클릭.</br>
    #     10. 1분 대기 후 인스펙션 화면 닫기 버튼 클릭    
    #     </br><b>기대결과</b> : Checklist 화면에서 넥스트 버튼을 누르면 다음 단계의 Checklist가 정상 출력되야 한다.</br>    
    #     ''' 
    #     '''<b>테스트 내용</b> : Checklist 기능 정상 작동 확인</br></br>
    #     <b>진행스탭</b></br>
    #     1.초기화면에서 스타트 버튼 클릭</br>
    #     2. Checklist(1/4) 기능(다음 버튼 클릭)을 확인한다. </br>
    #     3.다음 버튼을 눌러 Checklist(2/4)의 기능(팜리스트 설정[선택, 엑스트라 인풋박스에 텍스트 입력])을 확인한다. </br>
    #     4.다음 버튼을 눌러 Checklist(3/4)의 기능(날개 리셋, 날개 선택 좌,상,우)을 확인한다.</br>
    #     5.다음 버튼을 눌러 Checklist(4/4)의 기능(미션 버튼 클릭)을 확인한다.</br>
    #     6.Checklist(4/4)에서 고급설정버튼을 누른 후 이동 확인 후 뒤로가기 버튼을 눌러 전환을 확인한다.</br>
    #     7.이전 버튼을 누른다.</br>
    #     8.Checklist(3/4)에서 고급설정버튼을 누른 후 이동 확인 후 뒤로가기 버튼을 눌러 전환을 확인한다.</br>
    #     9.이전 버튼을 누른다.</br>
    #     10.Checklist(2/4)에서 고급설정버튼을 누른 후 이동 확인 후 뒤로가기 버튼을 눌러 전환을 확인한다.</br>
    #     11.이전 버튼을 누른다.</br>
    #     12.Checklist(1/4)에서 닫기 버튼을 눌러 Checklist 창이 닫힌지 확인한다.</br>
    #     13.인스펙션 닫기 버튼을 눌러 초기화면으로 전환한다.</br>
    #     </br><b>기대결과</b> : Checklist(1/4)에서 닫기, 넥스트 버튼 기능이 작동해야 한다.</br>    
    #     Checklist(2/4)에서 엑스트라 입력, 이전버튼, 넥스트버튼, 고급설정 이동 버튼 기능이 정상 작동해야 한다.</br>
    #     Checklist(1/4)에서 선택, 이전버튼, 넥스트 버튼, 고급설정 이동 버튼 기능이 작동해야 한다.</br>
    #     Checklist(1/4)에서 미션 선택, 고급설정 이동 버튼, 닫기, 컨펌 버튼, 고급설정 이동 버튼 기능이 작동해야 한다.</br>
    #     ''' 
    #     '''<b>테스트 내용</b> :  미션 이벤트 예외처리 </br></br>
    #     <b>진행스탭</b></br>
    #     1. 인스펙션 화면에 입장한다.</br>
    #     2. 미션 텍스트 버튼을 누른다.</br>
    #     3. 픽휠에 나오는 미션이벤트를 확인한다.</br>
    #     </br><b>기대결과</b> : 미션 이벤트 선택 후 텍스트가 일치 해야 한다. </br>    
    #     ''' 
    print("tc end")

@pytest.mark.login
def test_common_login(driver):

    #Setting Menu
    qcl(driver, "vll_btn_setting")

    #Camera Setting
    q_assert(driver, driver.find_element_by_accessibility_id("vll_btn_camera_setting").is_displayed(), True, "설정버튼을 못찾았습니다.")
    qcl(driver, "vll_btn_camera_setting")
    qcl(driver, "icon btn close white")

    #Release Mode
    [driver.tap([([x+y for x,y in zip(list(driver.find_element_by_accessibility_id("vll_btn_test_password_"+str(i)).location.values()),[100, 70])] )],50) for i in range(1, 5)]
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_release_mode").is_enabled(), True, "데브모드가 설정되지 않았습니다.")

    #Login
    #로그인 여부 판단 후 비로그인 시 로그인으로 변경하기
    q_assert(driver, driver.find_element_by_accessibility_id("vll_btn_nearth_wind").is_displayed(), True, "로그인 버튼이 출력되지 않았습니다.")

    if driver.find_element_by_accessibility_id("vll_lb_nearth_wind").get_attribute('label') == "NearthWIND Login":
        print("로그인이 되어 있지 않습니다. 로그인을 합니다.")
        qcl(driver, "vll_btn_nearth_wind")
        sleep(15)
        #Web View
        #Login Page
        driver.find_element_by_xpath('//XCUIElementTypeOther[@name="Zoomable"]/XCUIElementTypeOther[4]/XCUIElementTypeTextField').send_keys('sa')
        driver.find_element_by_xpath('//XCUIElementTypeOther[@name="Zoomable"]/XCUIElementTypeOther[5]/XCUIElementTypeSecureTextField').send_keys('pass')
        qcl(driver, "Login")
        sleep(3)    
    else:
        print("로그인 되어 있습니다.")

@pytest.mark.meta
def test_common_meta(driver):
    try:
        driver.find_element_by_accessibility_id("vll_btn_metadata_upload").is_displayed()
    except:
        qcl(driver, "vll_btn_setting")
    
    #Setting Menu
    q_assert(driver, driver.find_element_by_accessibility_id("vll_btn_setting").is_displayed(), True, "설정버튼을 못찾았습니다.")
    q_assert(driver, driver.find_element_by_accessibility_id("vll_btn_metadata_upload").is_displayed(), True, "메타데이터 업로드 버튼을 못찾았습니다.")
    
    qcl(driver, "vll_btn_metadata_upload")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_title").get_attribute("label"), 'Upload Metadata', "메타데이터 화면이 아닙니다.")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_top").get_attribute("label"), 'Top', "Top 버튼 미출력")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_delete").get_attribute("label"), 'Delete', "Cancel 버튼 미출력")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_edit").get_attribute("label"), 'Edit', "Edit 버튼 미출력")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_upload").get_attribute("label"), 'Upload', "Upload 버튼 미출력")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_restore").get_attribute("label"), 'Restore', "Restore 버튼 미출력")
    print("메타데이터 업로드 페이지 이동 성공")

    #메타데이터 페이지에 메타데이터가 있는지 파악
    if len([i for i in get_value(driver) if len(i) >= 18]) >= 1: 
    
        # #Select meta data
        driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="CellMetadata_btn_checkbox"])[1]').click()

        # #Extra
        driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="CellMetadata_lb_extra"])[1]').click()
        q_assert(driver, driver.find_element_by_accessibility_id("Extra").get_attribute("label"), 'Extra', "Extra popup 없음")
        qcl(driver, "OK")

        # #Title Popup
        driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="CellMetadata_lb_metadata"])[1]').click()
        q_assert(driver, len(get_value(driver)), 3, "metatitle popup")
        qcl(driver, "OK")

        # #Down Function
        # #Top
        # #Delete
        qcl(driver, "VCMetadata_lb_delete")
        q_assert(driver, len(list(set(["Cancel", "OK", "Delete Metadata"]) - set(get_value(driver)))), 0, "Delete Metadata")
        qcl(driver, "PopupDeleteMetadata_btn_ok")
        
        #Restore
        qcl(driver, "VCMetadata_btn_restore")
        q_assert(driver, driver.find_element_by_accessibility_id("Restore Metadata").get_attribute("label"), 'Restore Metadata', "restore page error")
        
        #Restore Metadata
        if len([i for i in get_value(driver) if len(i) >= 18]) >= 1:
            driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="CellMetadata_btn_checkbox"])[1]').click()    
            #Restore
            qcl(driver, "Restore")
        else:
            print("메타데이터가 없습니다.")
            qcl(driver, "icon_metadata_arrow_left")
        
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_title").get_attribute("label"), 'Upload Metadata', "메타데이터 화면이 아닙니다.")

        #첫번째 메타데이터 선택
        driver.find_element_by_xpath('(//XCUIElementTypeButton[@name="CellMetadata_btn_checkbox"])[1]').click()

        #Edit
        qcl(driver, "VCMetadata_lb_edit")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_btn_edit_bd_order").get_attribute("label"), 'bd Order', "bd Order 버튼 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_btn_edit_cancel").get_attribute("label"), 'Cancel', "Cancel 버튼 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_btn_edit_save").get_attribute("label"), 'Save', "Save 버튼 미출력")
        
        # #Data Wind Farm, Turbine, Inspection
        
        # #bd Order
        qcl(driver, "VCMetadata_btn_edit_bd_order")
        q_assert(driver, driver.find_element_by_accessibility_id("PopupEditbdOrder_lb_title").get_attribute("label"), 'bd Order', "bd Order 팝업텍스트 미출력 오류")
        q_assert(driver, driver.find_element_by_accessibility_id("PopupEditbdOrder_lb_bd_order_desc").get_attribute("label"), 'Select bd in order', "Select bd in order 텍스트 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("Cancel").get_attribute("label"), 'Cancel', "Cancel 버튼 미출력 오류")
        q_assert(driver, driver.find_element_by_accessibility_id("OK").get_attribute("label"), 'OK', "OK 미출력 오류")
        
        # #reset
        qcl(driver, "PopupEditbdOrder_btn_reset_bd_order")
        q_assert(driver, driver.find_element_by_accessibility_id("PopupEditbdOrder_lb_validation").get_attribute("label"), 'Please check bd', "Please check bd 텍스트 미출력 오류")

        #order a, b, c
        [driver.tap([(i)],50) for i in [[550, 402], [470, 400], [520, 340]]]
        q_assert(driver, driver.find_element_by_accessibility_id("PopupEditbdOrder_lb_bd_order_0").get_attribute("label"), 'A', "날개 A 미출력 오류")
        q_assert(driver, driver.find_element_by_accessibility_id("PopupEditbdOrder_lb_bd_order_1").get_attribute("label"), 'C', "날개 C 미출력 오류")
        q_assert(driver, driver.find_element_by_accessibility_id("PopupEditbdOrder_lb_bd_order_2").get_attribute("label"), 'B', "날개 B 미출력 오류")
        
            #Cancel
            #qcl(driver, "PopupEditbdOrder_btn_cancel")

        #Save
        qcl(driver, "PopupEditbdOrder_btn_ok")
        q_assert(driver, 0 if 'Select bd in order' not in get_value(driver) else 1, 0, "날개 오더 팝업 사라지지 않음")  

        #save
        qcl(driver, "VCMetadata_btn_edit_save")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_top").get_attribute("label"), 'Top', "Top 버튼 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_delete").get_attribute("label"), 'Delete', "Cancel 버튼 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_edit").get_attribute("label"), 'Edit', "Edit 버튼 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_upload").get_attribute("label"), 'Upload', "Upload 버튼 미출력")
        q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_restore").get_attribute("label"), 'Restore', "Restore 버튼 미출력")

        #Upload
        #미진행
    else:
        print("메타데이터가 하나도 없으므로, 생략합니다.")

    #Zoomable Data
    qcl(driver, "VCMetadata_btn_update")
    q_assert(driver, driver.find_element_by_accessibility_id("VCWindFarmList_lb_title").get_attribute("label"), 'Data', "데이터 페이지 미이동")
    
    #Refresh Button
    qcl(driver, "VCWindFarmList_btn_refresh")
    sleep(14)
    
    #Wind Farm Data
    q_assert(driver, 0 if len(get_value(driver)) > 100 else 1, 0, "리스트 불러오지 못함")
    print("핌리스트 불러오기 성공")
    
    #Back Button
    qcl(driver, "VCWindFarmList_btn_close")
    q_assert(driver, driver.find_element_by_accessibility_id("VCMetadata_lb_title").get_attribute("label"), 'Upload Metadata', "메타데이터 화면이 아닙니다.")
    
    #back button
    qcl(driver, "VCMetadata_btn_close")
    q_assert(driver, driver.find_element_by_accessibility_id("vll_btn_setting").is_displayed(), True, "설정버튼을 못찾았습니다.")

@pytest.mark.m00
def test_m00(driver):

    #Drone Model Type UI
    [qcl(driver, "vll_btn_test_password_5") for i in range(0, 5)]
    if driver.find_element_by_accessibility_id("vll_lb_drone_model").get_attribute("value") == 'No Aircraft detected': 
        qcl(driver, "PopupSelectDrone_btn_fix_drone_model")
    qcl(driver, "PopupSelectDrone_btn_m600")
    qcl(driver, "PopupSelectDrone_btn_ok")

    sleep(5)

    #ver
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_app_version").is_displayed() , True, "버전이 나오지 않는다." )
    
    #Time
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_ipad_time").is_displayed() , True, "아이패드 시간이 나오지 않는다." )
    
    #Connect
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_connected_status").get_attribute("value"),'Disconnected', "연결되어 있다." )
    
    #Inspection Page
    qcl(driver, "vll_btn_start")

    #M600 Checklist(1/4)
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute('label'), 'Checklist (1/4)',"프리체크리스트 1/4가 아니다.")
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_camera_status").get_attribute('label'), 'Click shutter button',"클릭 셔터 버튼 텍스트가 나오지 않는다.")

    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_back").is_displayed() , True, "닫기 버튼이 보이지 않는다." )
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").is_displayed() , True, "프리 체크리스트(1/4)가 보이지 않는다." )
    
    #Text
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_camera_status").is_displayed() , True, "카메라 상태값이 보이지 않는다." )
    
    #Remote Control Image
    q_assert(driver, driver.find_element_by_accessibility_id("icon_m600_rc_shutter_button").is_enabled() , True, "m00 셔터 버튼 이미지가 보이지 않는다." )
    
    #Next Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_next").is_displayed() , True, "다음 화면으로 이동하는 버튼이 보이지 않는다." )
    qcl(driver, "ChecklistViewPro_btn_next")
    sleep(5)

    #M600 Checklist(2/4)
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute("label"),'Checklist (2/4)', "프리 체크리스트 (2/4) 페이지가 아니다." )
    
    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_back").is_displayed() , True, "닫기 버튼이 보이지 않는다." )
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").is_displayed() , True, "타이틀 텍스트가 보이지 않는다." )
    
    #Advanced Settings Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_advanced_settings").is_displayed() , True, "어드벤스 세팅 버튼이 보이지 않는다." )
    qcl(driver, "ChecklistViewPro_btn_advanced_settings")
    sleep(2)
    qcl(driver, "ChecklistViewPro_btn_back")
    sleep(5)

    #WindFarm, WindTurbine, Inspection, Extra Select or input
    qcl(driver, "ChecklistViewPro_lb_windfarm_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("테스트")
    qcl(driver,"Change")
    sleep(4)
    qcl(driver, "ChecklistViewPro_lb_windturbine_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("탐라해상4호기백업")
    qcl(driver,"Change")
    sleep(4)
    qcl(driver, "ChecklistViewPro_lb_inspection_pladeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("#1")
    qcl(driver,"Change")
    sleep(3)
    
    driver.find_element_by_id("PopupAddInspection_tf_inspection").send_keys(str(random.randint(0, 1000)-1))
    qcl(driver,"PopupAddInspection_btn_add")

    #Extra input
    qcl(driver, "ChecklistViewPro_tv_extra")
    TouchAction(driver).tap(driver.find_element_by_xpath('//XCUIElementTypeTextView[@name="ChecklistViewPro_tv_extra"]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewPro_tv_extra").send_keys("tts")
    driver.hide_keyboard() #키보드 가리기
    
    # Prev Button
    qcl(driver,"ChecklistViewPro_lb_prev")
    sleep(5)
    assert driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute('label') == 'Checklist (1/4)'

    #Next Button
    sleep(3)
    qcl(driver,"ChecklistViewPro_btn_next")
    sleep(5)

    #M600 Checklist(3/4)
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute("label"),'Checklist (3/4)', "프리 체크리스트 (3/4)이 아니다." )
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_bd_order_title").get_attribute("label"),'bd', "날개 타이틀이 보이지 않는다." )
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_bd_order_desc").get_attribute("label"),'Select bd in order', "날개 셀렉트 오더가 보이지 않는다." )
    
    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_back").is_displayed() , True, "닫기 버튼이 보이지 않는다." )
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").is_displayed() , True, "타이틀이 보이지 않는다." )
    
    #Advanced Settings Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_advanced_settings").is_displayed() , True, "어드벤스 세팅 버튼이 보이지 않는다." )
    qcl(driver, "ChecklistViewPro_btn_advanced_settings")
    sleep(2)
    qcl(driver, "ChecklistViewPro_btn_back")
    sleep(2)
    
    #bd Reset Button
    qcl(driver, "ChecklistViewPro_btn_reset_bd_order")
    sleep(3)
    
    #bd Select A, B, C
    [driver.tap([(i)],50) for i in [[512, 302], [412, 402], [612, 402]]]
    
    #Prev Button
    qcl(driver,"ChecklistViewPro_lb_prev")
    sleep(5)
    assert driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute('label') == 'Checklist (2/4)'

    #Next Button
    sleep(3)
    qcl(driver,"ChecklistViewPro_btn_next")
    sleep(5)

    #M600 Checklist(4/4)
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute("label"),'Checklist (4/4)', "프리 체크리스트 4/4페이지가 아니다." )
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_mission_type_title").get_attribute("label"),'Mission Type', "미션타입 텍스트가 나오지 않는다." )

    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_back").is_displayed() , True, "닫기 버튼이 나오지 않는다." )
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").is_displayed() , True, "타이틀 텍스트가 나오지 않는다." )
    
    #Text
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewPro_btn_advanced_settings").is_displayed() , True, "어드벤스 세팅버튼이 나오지 않는다." )
    qcl(driver, "ChecklistViewPro_btn_advanced_settings")
    
    #Advanced Settings Button
    qcl(driver, "ChecklistViewPro_btn_back")
    
    #Mission Select Button
    qcl(driver, "ChecklistViewPro_btn_mission_type_6_2")
    
    #Prev Button
    qcl(driver,"ChecklistViewPro_lb_prev")
    assert driver.find_element_by_accessibility_id("ChecklistViewPro_lb_title").get_attribute('label') == 'Checklist (3/4)'
    assert driver.find_element_by_accessibility_id("ChecklistViewPro_lb_bd_order_title").get_attribute('label') == 'bd'
    assert driver.find_element_by_accessibility_id("ChecklistViewPro_lb_bd_order_desc").get_attribute('label') == 'Select bd in order'

    ##Next Button
    qcl(driver,"ChecklistViewPro_btn_next")
    sleep(3)
    
    #Confirm Button
    qcl(driver,"ChecklistViewPro_btn_confirm")
    sleep(61)
    qcl(driver,"OK")
    sleep(7)
    screen_txt = get_value(driver)
    q_assert(driver, True if "Checklist (4/4)" not in  screen_txt else False , True, "프리 체크리스트가 완료되지 않았다." )
    
    sleep(5)
    
    #Confirm Buttuon
    ran_inspet = str(random.randint(0, 1000)-1)
    ran_extra = "qatest"
    ran_bl = "30.0"
    qcl(driver,"VCInspection_btn_setting")
    qcl(driver, "ChecklistViewPro_btn_advanced_settings")
    
    #Mission Type
    qcl(driver,"ChecklistViewPro_btn_ad_mission_type_6_1")
    
    #FocalLength
    qcl(driver, "ChecklistViewPro_btn_ad_focal_length_42")
    
    #FStop
    qcl(driver, "ChecklistViewPro_tf_ad_fstop")
    TouchAction(driver).tap(driver.find_element_by_xpath('//XCUIElementTypeTextField[@name="ChecklistViewPro_tf_ad_fstop"]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewPro_tf_ad_fstop").send_keys(ran_bl)
    driver.hide_keyboard() #키보드 가리기
    
    #WindFarm
    qcl(driver, "ChecklistViewPro_lb_ad_windfarm_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("테스트")
    qcl(driver,"Change")
    
    #WindTurbine
    qcl(driver, "ChecklistViewPro_lb_ad_windturbine_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("테스트")
    qcl(driver,"Change")
    
    #Inspection
    qcl(driver, "ChecklistViewPro_lb_ad_inspection_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("##1")
    qcl(driver,"Change")
    
    #Extra
    qcl(driver, "ChecklistViewPro_tv_ad_extra")
    TouchAction(driver).tap(driver.find_element_by_xpath('//XCUIElementTypeTextView[@name="ChecklistViewPro_tv_ad_extra"]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewPro_tv_ad_extra").send_keys(ran_extra)
    driver.hide_keyboard()
    
    #bd Reset
    qcl(driver, "ChecklistViewPro_btn_ad_reset_bd_order")
    
    #bd select
    [driver.tap([(i)],50) for i in [[800, 370], [740, 420], [820, 420]]]
    
    #advanced setting all check
    screen_txt = get_value(driver)
    td_data = [ 'A', 'B', 'C', '6-1', ran_bl, '테스트', '호기', "#1"]
    q_assert(driver, len(list(set(td_data) - set(screen_txt))),0, "어드밴스 세팅에 설정내용이 적용되지 않았다." )
    
    #Confirm Buttuon
    qcl(driver, "ChecklistViewPro_btn_confirm")
    sleep(61)
    qcl(driver,"OK")
    
    sleep(7)
    
    #Checklist
    qcl(driver, "VCInspection_btn_preflight_checklist")
    sleep(5)
    q_assert(driver, len(list(set(['ESC Status', 'Checklist']) - set(get_value(driver)))), 0 , "체크리스트페이지가 정상적이지 않다." )
    
    #close()
    qcl(driver, "CancelButton")
    
    #text
    #Remote Controller Mode
    qcl(driver, "VCInspection_btn_remote_controller")
    sleep(5)
    q_assert(driver, len(list(set(['Mode 2', 'Mode 1', 'Mode', 'Mode 3']) - set(get_value(driver)))), 0, "모드값 변경 창이 정상 출력되지 않았다." )
    
    #close()
    qcl(driver, "icon_btn_close_white")
    #Mode1,#Mode2,#Mode3

    #Image Transmission settings
    qcl(driver, "VCInspection_btn_video_signal")
    
    #Bandwidth Allocation
    driver.find_element_by_xpath("//XCUIElementTypeSlider").send_keys("0.5")
    sleep(5)
    q_assert(driver, len(list(set(['Enable'40%']) - set(get_value(driver)))), 0, "설정 페이지가 정상 출력되지 않았다." )
    
    #close()
    qcl(driver, "icon_btn_close_white")
    sleep(3)
    
    #go landing page
    qcl(driver, "VCInspection_btn_close")

@pytest.mark.m0
def test_m0(driver):

    #Drone Model Type UI
    [qcl(driver, "vll_btn_test_password_5") for i in range(0, 5)]
    if driver.find_element_by_accessibility_id("vll_lb_drone_model").get_attribute("value") == 'No Aircraft detected': 
        qcl(driver, "PopupSelectDrone_btn_fix_drone_model")
    qcl(driver, "PopupSelectDrone_btn_m0")
    qcl(driver, "PopupSelectDrone_btn_ok")

    sleep(5)
    #ID에 m0이 출력되지 않으면 다시 진행한다. 크래프트로 확인할것!!

    #ver
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_app_version").is_displayed() , True, "아이패드 버전이 정상 출력되지 않는다." )
    
    #Time
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_ipad_time").is_displayed() , True, "아이패드 시간이 정상 출력이 되지 않는다." )
    
    #System Status #m0
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_drone_model").get_attribute("value") , 'MATRICE 300 RTK', "M0 설정이 되지 않았다." )
    
    #Connect
    q_assert(driver, driver.find_element_by_accessibility_id("vll_lb_connected_status").get_attribute("value") , 'Disconnected', "기체와 연결이 되지 않은 상태가 아니다." )

    #Inspection Page
    qcl(driver, "vll_btn_start")
    sleep(5)
    
    #M0 Checklist(1/4)
    q_assert(driver, driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="ChecklistViewHopping_lb_title"])[2]').get_attribute('label'),'Checklist (1/4)', "프리 1/4 페이지가 아니다." )
    q_assert(driver, driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="ChecklistViewHopping_lb_camera_status"])[2]').get_attribute('label'),"Click shutter button", "클릭 셔터버튼 텍스트가 나오지 않았다." )
    
    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_back").is_enabled() , True, "뒤로가기 버튼이 출력되지 않았다." )
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_lb_title").is_enabled() , True, "타이틀 텍스트가 출력되지 않았다." )
    
    #Text
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_lb_camera_status").is_enabled() , True, "카메라 상태 텍스트가 출력되지 않았다." )
    
    #Remote Control Image
    q_assert(driver, driver.find_element_by_accessibility_id("icon_m0_rc_shutter_button").is_enabled() , True, "조종기 이미지가 출력되지 않았다." )
    
    #Next Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_next").is_enabled() , True, "다음 버튼이 출력되지 않았다." )
    qcl(driver, "ChecklistViewHopping_btn_next")
    sleep(5)
    q_assert(driver, driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="ChecklistViewHopping_lb_title"])[2]').get_attribute('label'),'Checklist (2/4)', "프리 체크리스트(2/4)가 출력되지 않았다." )
    
    #M0 Checklist(2/4)
    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_back").is_enabled() , True, "닫기 버튼이 출력되지 않았다." ) 
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_lb_title").is_enabled() , True, "프리 체크리스트 텍스트가 출력되지 않았다." )
    
    #Advanced Settings Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_advanced_settings").is_enabled() , True, "고급 설정 버튼이 출력되지 않았다." )
    qcl(driver, "ChecklistViewHopping_btn_advanced_settings")
    sleep(3)
    qcl(driver, "ChecklistViewHopping_btn_back")

    #WindFarm, WindTurbine, Inspection, Extra Select or input
    qcl(driver, "ChecklistViewHopping_lb_windfarm_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("테스트")
    sleep(2)
    qcl(driver,"Change")
    sleep(4)
    qcl(driver, "ChecklistViewHopping_lb_windturbine_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("탐라해상4호기백업")
    sleep(2)
    qcl(driver,"Change")
    sleep(4)
    qcl(driver, "ChecklistViewHopping_lb_inspection_placeholder")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("#1")
    sleep(2)
    qcl(driver,"Change")
    sleep(3)

    #Inspection Add new Popup Add a new inspection
    driver.find_element_by_id("PopupAddInspection_tf_inspection").send_keys(str(random.randint(0, 1000)-1))
    qcl(driver,"PopupAddInspection_btn_add")        

    #Extra input
    qcl(driver, "ChecklistViewHopping_tv_extra")
    TouchAction(driver).tap(driver.find_element_by_xpath('(//XCUIElementTypeTextView[@name="ChecklistViewHopping_tv_extra"])[2]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewHopping_tv_extra").send_keys("tts")
    driver.hide_keyboard() #키보드 가리기

    #Next Button
    qcl(driver,"ChecklistViewHopping_btn_next")
    sleep(5)

    #M0 Checklist(3/4)
    q_assert(driver, driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="ChecklistViewHopping_lb_bd_order_title"])[2]').get_attribute('label'),'bd', "날개 텍스트가 출력되지 않았다." )
    q_assert(driver, driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="ChecklistViewHopping_lb_bd_order_desc"])[2]').get_attribute('label'),'Select bd in order', "셀렉트 날개 인 오더 텍스트가 출력되지 않았다." )

    #Close Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_back").is_enabled() , True, "닫기 버튼이 출력되지 않았다." )
    
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_lb_title").is_enabled() , True, "프리 체크리스트 (3/4)가 출력되지 않았다." )
    
    #Text
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_advanced_settings").is_enabled() , True, "고급 설정 버튼이 출력되지 않았다." )
    
    #Advanced Settings Button
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_advanced_settings").is_enabled() , True, "고급설정 버튼이 출력되지 않았다." )
    
    qcl(driver, "ChecklistViewHopping_btn_advanced_settings")
    sleep(3)
    qcl(driver, "ChecklistViewHopping_btn_back")
    #bd Reset Button
    qcl(driver, "ChecklistViewPro_btn_reset_bd_order")
    #bd Select A, B, C
    [driver.tap([(i)],50) for i in [[512, 302], [412, 402], [612, 402]]]
    sleep(2)
    #Next Button
    qcl(driver,"ChecklistViewHopping_btn_next")
    sleep(7)

    #M0 Checklist(4/4)
    
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_back").is_enabled() , True, "닫기 버튼이 출력되지 않았다." )
    #Title
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_lb_title").is_enabled() , True, "프리 체크리스트 (4/4) 텍스트가 출력되지 않았다.")
    #Text
    q_assert(driver, driver.find_element_by_accessibility_id("ChecklistViewHopping_btn_advanced_settings").is_enabled(), True, "고급 설정 버튼이 출력되지 않았다." )
    qcl(driver, "ChecklistViewHopping_btn_advanced_settings")
    #Advanced Settings Button
    qcl(driver, "ChecklistViewHopping_btn_back")
    #Mission Select Button
    qcl(driver, "ChecklistViewHopping_btn_mission_type_BF6_2")
    #ISO Preset Select Button
    qcl(driver, "ChecklistViewHopping_btn_iso_preset_2")
    #bdLength Input
    qcl(driver, "ChecklistViewHopping_tf_bd_length")
    TouchAction(driver).tap(driver.find_element_by_xpath('(//XCUIElementTypeTextField[@name="ChecklistViewHopping_tf_bd_length"])[2]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewHopping_tf_bd_length").send_keys("35.0")
    driver.hide_keyboard() #키보드 가리기

    #Next Button

    #Confirm Button
    qcl(driver,"ChecklistViewHopping_btn_confirm")
    sleep(61)
    qcl(driver,"OK")
    screen_txt = get_value(driver)
    q_assert(driver, True if "Checklist (4/4)" not in  screen_txt else False, True, "프리 체크리스트 4/4 페이지가 사라지지 않았다." )

    #M0 Checklist Advanced Settings
    #inspection Settings
    qcl(driver, "VCInspection_btn_close")
    qcl(driver, "vll_btn_start")
    qcl(driver,"ChecklistViewHopping_btn_next")
    qcl(driver, "ChecklistViewHopping_btn_advanced_settings")

    ran_inspet = str(random.randint(0, 1000)-1)
    ran_extra = "qatest"
    ran_bl = "32.1"

    #Mission Type
    qcl(driver,"ChecklistViewHopping_btn_ad_mission_type_BF6_1")

    #bd Length
    qcl(driver, "ChecklistViewHopping_tf_ad_bd_length")
    TouchAction(driver).tap(driver.find_element_by_xpath('(//XCUIElementTypeTextField[@name="ChecklistViewHopping_tf_ad_bd_length"])[2]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewHopping_tf_ad_bd_length").send_keys(ran_bl)
    driver.hide_keyboard() #키보드 가리기

    #ISO Preset
    qcl(driver, "ChecklistViewHopping_btn_ad_iso_preset_2")

    #Extra
    qcl(driver, "ChecklistViewHopping_tv_ad_extra")
    TouchAction(driver).tap(driver.find_element_by_xpath('(//XCUIElementTypeTextView[@name="ChecklistViewHopping_tv_ad_extra"])[2]'), count=2).perform()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("delete").click()
    driver.find_element_by_id("ChecklistViewHopping_tv_ad_extra").send_keys(ran_extra)
    driver.hide_keyboard() #키보드 가리기

    #WindFarm
    qcl(driver, "ChecklistViewHopping_btn_ad_windfarm_list")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("테스트")
    qcl(driver,"Change")
    sleep(2)

    #WindTurbine
    qcl(driver, "ChecklistViewHopping_btn_ad_windturbine_list")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("탐라해상4호기백업")
    qcl(driver,"Change")
    sleep(2)

    #Inspection
    qcl(driver, "ChecklistViewHopping_btn_ad_inspection_list")
    driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys("#1")
    qcl(driver,"Change")
    sleep(2)

    #bd Reset
    qcl(driver, "ChecklistViewHopping_btn_ad_reset_bd_order")

    #bd select
    [driver.tap([(i)],50) for i in [[800, 370], [740, 420], [820, 420]]]
    sleep(5)

    #advanced setting all check
    screen_txt = get_value(driver)
    td_data = [ 'A', 'B', 'C', 'BF6-1', '테스트', '탐라해상4호기백업', '2']
    q_assert(driver, len(list(set(td_data) - set(screen_txt))),0, "고급설정 세팅값이 정상 설정되지 않았다." )

    #Confirm Buttuon
    qcl(driver, "ChecklistViewHopping_btn_confirm")

    sleep(70)
    qcl(driver,"OK")
    sleep(10)
    #go landing page
    qcl(driver, "VCInspection_btn_close")

@pytest.mark.mission_text
def test_mission_text(driver):
    #inspection
    qcl(driver, "vll_btn_start")
    sleep(5)

    #Mission Text
    qcl(driver, "ChecklistViewPro_btn_back")
    sleep(3)

    #Error type text select
    qcl(driver, "VCInspection_btn_test_mission_text")

    #Popup Text
    ko = {}
    f = open("/Users/anjanghyun/Desktop/nd/ko.lproj/Localizable.strings", "r")

    lines = f.readlines()
    for line in lines:
        line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
        if " = " in line:
            lst = line.replace(";","").replace('"',"").split(" = ")
            ko[lst[0]] = lst[1]
    f.close()

    a, b, lst = "","",[]
    while True:
        a = driver.find_element_by_xpath("//XCUIElementTypePickerWheel").get_attribute('value')
        if a != None:
            lst.append(a)
            if a != b:
                b = a
                driver.tap([['930', '700'], "50"])
            elif a == b:
                break
        else:
            driver.tap([['930', '700'], "50"])
    qcl(driver, "Cancel")

    #다음은 해당 이벤트를 선택해서 메시지를 보는 시스템을 만들어 본다.
    for i in lst:
        qcl(driver, "VCInspection_btn_test_mission_text")
        print("code = " + i)
        driver.find_element_by_xpath("//XCUIElementTypePickerWheel").send_keys(i)
        qcl(driver, "Change")
        sleep(3)
        con = ko[i].replace("\\n"," ")
        print("c1 : " + con)
        req = driver.page_source
        rst = req[req.find(con):req.find(con)+300].replace("\n\n"," ").split('" ')[0]
        rst = rst.split(" (Code")[0]
        print("c2 : " + rst)
        q_assert(driver, con , rst, "예외처리 메시지가 다름" )
        if con == rst:
            print("성공")
        else:
            print("실패")