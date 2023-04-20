#Created by An Janghyun

#cli command
#appium -p 4101 --default-capabilities '{"systemPort": 8101, "udid": "002458020-001304C426D1002E"}'
#appium -p 4102 --default-capabilities '{"systemPort": 8102, "udid": "000234540-00067C8E0C04402E"}'
#appium -p 4103 --default-capabilities '{"systemPort": 8103, "udid": "000235430-000A78183E41402E"}'
#appium -p 4104 --default-capabilities '{"systemPort": 8104, "udid": "f6e79b22345234543529d96c8cc976db8af4"}'
#appium -p 4105 --default-capabilities '{"systemPort": 8105, "udid": "152BF623452345948-2F496D3ADC8C"}'

# class td:
qa1_url = 'http://127.0.0.1:4101/wd/hub'
qa1_nor = {"platformVersion": "13.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "7200","deviceName": "QA 1","noReset": "true","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "0000812412020-001304C426125125D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa"}
qa1_ipa = {"platformVersion": "13.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "72000","deviceName": "QA 1","noReset": "false","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "00008012412420-001241241304C426D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa","app": "/Users/anjanghyun/Desktop/qa/ipa/Nd.ipa","appPushTimeout":"300000"}

qa2_url = 'http://127.0.0.1:4102/wd/hub'
qa2_nor = {"platformVersion": "14.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "7200","deviceName": "QA 2","noReset": "true","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "0000812412020-001304C426125125D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa"}
qa2_ipa = {"platformVersion": "14.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "72000","deviceName": "QA 2","noReset": "false","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "00008012412420-001241241304C426D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa","app": "/Users/anjanghyun/Desktop/qa/ipa/Nd.ipa","appPushTimeout":"300000"}

qa3_url = 'http://127.0.0.1:4103/wd/hub'
qa3_nor = {"platformVersion": "14.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "7200","deviceName": "QA 3","noReset": "true","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "0000812412020-001304C426125125D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa"}
qa3_ipa = {"platformVersion": "14.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "72000","deviceName": "QA 4","noReset": "false","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "00008012412420-001241241304C426D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa","app": "/Users/anjanghyun/Desktop/qa/ipa/Nd.ipa","appPushTimeout":"300000"}

dev2_url = 'http://127.0.0.1:4104/wd/hub'
dev2_nor = {"platformVersion": "13.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "7200","deviceName": "dev2","noReset": "true","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "0000812412020-001304C426125125D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa"}
dev2_ipa = {"platformVersion": "13.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "72000","deviceName": "dev2","noReset": "false","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "00008012412420-001241241304C426D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa","app": "/Users/anjanghyun/Desktop/qa/ipa/Nd.ipa","appPushTimeout":"300000"}

sim_url = 'http://127.0.0.1:4723/wd/hub'
sim_nor = {"platformVersion": "14.5","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "7200","deviceName": "sim","noReset": "true","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "0000812412020-001304C426125125D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa"}
sim_ipa = {"platformVersion": "14.0","platformName": "ios","automationName": "XCUITest","newCommandTimeout": "72000","deviceName": "sim","noReset": "false","xcodeOrgId": "4BNKET@#ESEGERET$$@DF5VR","xcodeSigningId": "iPhone Developer","udid": "00008012412420-001241241304C426D1002E","wdaLocalPort" :"8101","bundleId": "com.nd-Qa","app": "/Users/anjanghyun/Desktop/qa/ipa/Nd.ipa","appPushTimeout":"300000"}


api_id = "idid"                            #api용 id
api_pw = "pwpw"                       #api용 pw
api_url = "https://api-staging.ale.io" #api용 url
                                                 #초기화면 서브 설정메뉴 리스트
login_list = ["Make", "Easy", "with Autonology", "Not registered?", "Contact us"] #로그인 웹 페이지 검증 리스트
test_api = [["login","로그인 api가 정상 확인"],["rm", "리스트 api가 정상 확인"],["nt","리스트 개수가 정상 확인"] ]            #api 검증 부붐
account = [
    [None, None, 'Please enter username', "아이디, 비밀번호 미입력 시 에러 확인"],
    ['test', None, 'Please enter password', "정확한 아이디, 비밀번호 미 입력시 에러 확인"],
    [None, 'test', 'Please enter username', "아이디 미입력, 아무 비밀번호 입력시 에러 확인"],
    ['test', 'qa', 'invalid:username', "잘못된 아이디, 잘못된 비밀번호 입력시 에러 확인"],
    ['sa', 'qa', 'invalid:password', "정확한 아이디, 잘못된 비밀번호 입력시 에러 확인"],
    ['sa','pass','Logout',"정확한 아이디,비밀번호 입력 후 로그인 확인"]] #노/노,입력/노,노/입력,틀린/틀린,정상/틀린,정상/정상


ll = [
"FINISHEDED_THEPOSITIONED_THEREACHED",
"FINISHEDED_THEROOTED_THEREACHED",
"FINISHEDED_THETIPED_THEREACHED",
"FINISHEDED_THENOSEED_THEREACHED",
"FINISHEDED_THENOED_THEFLYED_THEZONE",
"FINISHEDED_THECAMED_THETRANSITION",
"ERRORED_THESWED_THEEXCEPTION",
"ERRORED_THECOLLISIONED_THEDETECTED",
"ERRORED_THECTRED_THEDOED_THENOTED_THEUSE",
"ERRORED_THECTRED_THECONTROLED_THEUSERED_THEMISMATCH",
"FINISHEDED_THEUSERED_THESTOPPEDED_THEMISSION",
"ERRORED_THEGIMBALED_THESETED_THECMDED_THEFAILED",
"ERRORED_THEWRONGED_THEJOBED_THEINFO",
"ERRORED_THEINITED_THEMISSIONED_THEISED_THENOTED_THEFINISHED",
"ERRORED_THEINITED_THELIDARED_THEFAILEDED_THETOED_THEDETECTED_THENOSE",
"ERRORED_THEINITED_THELIDARED_THETIMEOUT",
"ERRORED_THEINITED_THEWRONGED_THEINITED_THEDIST",
"ERRORED_THECAMERAED_THEAUTOFOCUSED_THEFAIL",
"ERRORED_THESTDED_THELIDARED_THEFAILEDED_THETOED_THEDETECTED_THETIP",
"ERRORED_THESTDED_THEDLED_THEFAILEDED_THEPUB",
"ERRORED_THESTDED_THEDLED_THEFAILEDED_THEBLADEED_THEDETECT",
" ",
"ERRORED_THESTDED_THEGIMBALED_THESTATUSED_THEISED_THEINVALID",
"ERRORED_THESTDED_THEGIMBALED_THECONVERGINGED_THETIMEOUT",
"ERRORED_THESTDED_THELIDARED_THETIMEOUT",
"ERRORED_THEWPED_THEWRONGED_THEWPTYPE",
"ERRORED_THEWPED_THELIDARED_THEFAILEDED_THETOED_THEDETECTED_THETIP",
"ERRORED_THECAMED_THEGIMBALED_THESTATUSED_THEISED_THEINVALID",
"ERRORED_THECAMED_THEGIMBALED_THECONVERGINGED_THETIMEOUT"]