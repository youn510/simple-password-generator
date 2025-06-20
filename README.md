# 간단한 암호 생성기 (Simple Password Generator)

## 프로젝트 개요

이 프로젝트는 사용자가 설정한 조건(비밀번호 길이, 포함할 문자 유형)에 따라 강력하고 무작위적인 비밀번호를 생성해주는 간단한 데스크톱 애플리케이션입니다. Python의 기본 GUI 라이브러리인 `Tkinter`를 사용하여, 별도의 설치나 복잡한 설정 없이 바로 실행하여 사용할 수 있도록 제작되었습니다.

## 목적

* Python과 `Tkinter`를 활용한 기본적인 GUI 애플리케이션 개발 경험을 쌓습니다.
* 사용자 정의 가능한 조건에 따라 문자열을 조합하고 무작위로 생성하는 로직을 구현합니다.
* 클립보드 연동과 같은 운영체제 인터페이스 기능을 경험합니다.
* "완전하고 단독 실행 가능한 SW"라는 요구사항을 충족하는 유용한 미니 프로젝트를 완성합니다.

## 상세 기능

1.  **비밀번호 길이 설정:**
    * 8자에서 32자 사이의 비밀번호 길이를 슬라이더(Scale)와 연동된 라벨을 통해 시각적으로 설정할 수 있습니다.
2.  **포함 문자 유형 선택:**
    * **대문자 (A-Z):** 대문자를 포함할지 여부를 선택합니다.
    * **소문자 (a-z):** 소문자를 포함할지 여부를 선택합니다.
    * **숫자 (0-9):** 숫자를 포함할지 여부를 선택합니다.
    * **특수 문자 (!@#$%^&*...):** 다양한 특수 문자를 포함할지 여부를 선택합니다.
    * **유효성 검사:** 최소 한 가지 문자 유형을 선택해야 비밀번호를 생성할 수 있습니다.
3.  **'생성' 버튼:**
    * 설정된 길이와 문자 유형에 따라 새로운 무작위 비밀번호를 생성하여 하단에 표시합니다.
    * 선택된 각 문자 유형에서 최소 1개 이상의 문자를 포함하도록 보장하여 더욱 강력한 비밀번호를 만듭니다.
4.  **생성된 비밀번호 표시:**
    * 생성된 비밀번호는 편집 불가능한 텍스트 상자에 명확하게 표시됩니다.
5.  **'클립보드에 복사' 버튼:**
    * 생성된 비밀번호를 한 번의 클릭으로 사용자의 시스템 클립보드에 복사합니다.

## 입출력 형태

* **입력:**
    * **슬라이더 조작:** 마우스로 슬라이더를 움직여 비밀번호 길이를 조정합니다.
    * **체크박스 클릭:** 마우스로 체크박스를 클릭하여 포함할 문자 유형을 선택/해제합니다.
    * **버튼 클릭:** '비밀번호 생성' 또는 '클립보드에 복사' 버튼을 마우스로 클릭합니다.
* **출력:**
    * **텍스트:** 현재 설정된 비밀번호 길이, 생성된 비밀번호가 텍스트 형태로 화면에 표시됩니다.
    * **팝업 알림:** 비밀번호가 클립보드에 복사되었음을 알리는 메시지 박스가 나타납니다.
    * **경고 메시지:** 유효하지 않은 설정(예: 문자 유형 미선택) 시 경고 팝업이 나타납니다.

## 개발 환경 및 기술 스택

* **Python 3.x:** 프로그래밍 언어 (Python 3.6 이상 권장).
* **Tkinter:** Python에 내장된 표준 GUI 라이브러리. (별도의 추가 설치 필요 없음)
* **`random` 모듈:** 비밀번호 문자열의 무작위 생성을 위해 사용됩니다.
* **`string` 모듈:** 알파벳, 숫자, 특수 문자 등의 문자열 상수를 쉽게 가져오기 위해 사용됩니다.

## 실행 방법

이 프로젝트는 Python이 설치된 모든 운영체제(Windows, macOS, Linux)에서 별도의 설치 없이 바로 실행할 수 있습니다.

### 1. 사전 준비물

* **Python 3.x:** 컴퓨터에 Python 3.6 버전 이상이 설치되어 있어야 합니다.
    * Python 설치 여부 확인: 터미널/명령 프롬프트에서 `python --version` 또는 `python3 --version`을 입력하여 버전을 확인합니다.
    * 설치되어 있지 않다면, [Python 공식 웹사이트](https://www.python.org/downloads/)에서 최신 버전을 다운로드하여 설치합니다. (설치 시 "Add Python to PATH" 옵션을 꼭 체크하세요.)

### 2. 설치 과정 (소스 코드 준비)

Git을 사용하여 소스 코드를 가져오는 방법과, Git 없이 직접 파일을 다운로드하는 두 가지 방법이 있습니다.

* **방법 1: Git을 사용하여 리포지토리 클론 (권장)**
    1.  터미널(Windows: 명령 프롬프트 또는 PowerShell, macOS/Linux: 터미널)을 엽니다.
    2.  프로젝트를 저장하고 싶은 폴더로 이동합니다. (예: `cd Documents/GitHub_Projects`)
    3.  다음 명령어를 실행하여 깃허브 리포지토리를 클론(복제)합니다:
        ```bash
        git clone [https://github.com/당신의_깃허브_아이디/simple-password-generator.git](https://github.com/당신의_깃허브_아이디/simple-password-generator.git)
        ```
        * **주의:** 위의 URL에서 `당신의_깃허브_아이디`는 **본인의 실제 깃허브 사용자 이름**으로 바꿔야 합니다.
    4.  클론이 완료되면 `simple-password-generator`라는 새 폴더가 생성됩니다. 이 폴더로 이동합니다:
        ```bash
        cd simple-password-generator
        ```

* **방법 2: 깃허브에서 직접 ZIP 파일 다운로드**
    1.  해당 프로젝트의 깃허브 리포지토리 페이지(예: `https://github.com/당신의_깃허브_아이디/simple-password-generator`)로 접속합니다.
    2.  리포지토리 페이지에서 초록색 **`< > Code`** 버튼을 클릭합니다.
    3.  드롭다운 메뉴에서 **`Download ZIP`**을 클릭하여 압축 파일을 다운로드합니다.
    4.  다운로드된 압축 파일을 원하는 위치에 압축 해제합니다. 압축을 해제하면 `simple-password-generator-main` (또는 비슷한 이름) 폴더가 생성됩니다.

### 3. 실행 명령 (가장 중요!)

소스 코드 준비가 완료되었다면, 다음 명령어로 암호 생성기를 실행할 수 있습니다.

* **터미널/명령 프롬프트에서 실행:**
    1.  `simple-password-generator` (또는 `simple-password-generator-main`) 폴더로 이동합니다. (만약 위 2단계에서 이미 이 폴더에 있다면 생략)
        ```bash
        cd simple-password-generator
        ```
    2.  다음 명령어를 터미널에 입력하고 `Enter` 키를 누릅니다:
        ```bash
        python main.py
        # 또는 (시스템 설정에 따라)
        python3 main.py
        ```
        * `python` 또는 `python3`는 시스템에 설치된 Python 실행 파일의 이름에 따라 다를 수 있습니다. 일반적으로 `python`을 먼저 시도해보고 안 되면 `python3`를 사용합니다.

    3.  명령어를 실행하면, 작은 윈도우 형태의 "간단한 암호 생성기" 애플리케이션이 화면에 나타날 것입니다.

### 4. 추가 환경 설정

* 이 프로젝트는 Python의 기본 내장 라이브러리인 `Tkinter`, `random`, `string`만 사용하므로, **별도의 추가 설치 파일이나 환경 설정이 필요하지 않습니다.** Python만 설치되어 있다면 바로 실행 가능합니다.

## 프로젝트 구조
simple-password-generator/
├── main.py    (암호 생성기 로직 및 GUI 구현 코드)
└── README.md  (프로젝트 설명 문서)