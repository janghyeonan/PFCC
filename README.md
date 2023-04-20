#테스트 자동화 관련 폴더/파일

##PFCC
PFCC(Python File Cleanup Collection)는 파일 처리, 테스트, API 개발과 관련된 다양한 목적을 위한 파이썬 스크립트 모음입니다.

## 폴더 안내
여러 폴더로 구성되어 있으며, 각각의 스크립트파일로 되어 있습니다.:

### automation_test_code
이 폴더는 프로젝트의 자동화된 테스트와 관련된 스크립트가 포함되어 있습니다:
- `conftest.py`: pytest를 위한 구성 파일입니다.(공통 함수 포함)
- `ios_qa_test.py`: iOS 애플리케이션 테스트 스크립트입니다.
- `nd_app_full_test.py`: 웹 애플리케이션의 전체 기능을 테스트하는 스크립트입니다.(전체 시나리오 테스트)
- `test_data.py`: 테스트 데이터가 추가된 스크립트입니다.

### database_etc
이 폴더는 데이터베이스 관리 및 API 개발과 관련된 스크립트가 포함되어 있습니다:
- `api_post_insert.py`: POST 요청을 사용하여 API에 데이터를 삽입하는 스크립트입니다.
- `aws_lambda_function.py`: AWS Lambda에서 Python 코드를 실행하는 스크립트입니다.
- `database_api_flask.py`: Flask를 사용하여 API를 생성하는 스크립트입니다.
- `jenkins_run.py`: Jenkins 작업을 실행하는 스크립트입니다.

### github_action_file
이 폴더는 GitHub Actions와 관련된 스크립트가 포함되어 있습니다:
- `main.py`: GitHub Action workflow를 만드는 스크립트입니다.
- `subinfo.py`: 텔레그램 연동 정보가 들어 있는 스크립트입니다.

### test_api_flask
이 폴더는 Flask API를 테스트하는 스크립트가 포함되어 있습니다:
- `app.py`: API용 Flask 애플리케이션입니다.
- `restxapi.py`: RESTful API로 만든 스크립트입니다.


## 사용법
각 스크립트의 사용 방법에 대한 자세한 지침은 각 폴더의 README 파일에서 찾을 수 있습니다.


## 라이선스
이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 `LICENSE` 파일을 참조하십시오.