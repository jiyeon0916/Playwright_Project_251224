import pytest
from playwright.sync_api import sync_playwright, expect
from src.browser import launch_browser


BASE_URL = "https://www.3o3.co.kr"


@pytest.fixture(scope="function")
def page():
    """
    테스트 단위마다 브라우저를 새로 띄워
    테스트 간 상태 영향을 방지한다.
    """
    with sync_playwright() as playwright:
        browser = launch_browser(playwright)
        context = browser.new_context()
        page = context.new_page()
        yield page

        # 테스트 종료 후 정리
        context.close()
        browser.close()

@pytest.fixture
def go_to_login_page(page):
    page.goto(BASE_URL)

    refund_cta = page.locator(
        "a#lp-pom-button-1353 span",
        has_text="내 환급금 조회하기"
    )

    expect(refund_cta).to_be_visible()
    refund_cta.click()

    page.wait_for_url("**/login")
    return page

def test_landing_page_has_refund_inquiry_cta(page):
    """
    [TC-01]
    랜딩 페이지 진입 시
    '내 환급금 조회하기' CTA가 노출되는지 확인한다.
    """

    page.goto(BASE_URL)

    refund_cta = page.locator(
        "a#lp-pom-button-1353 span",
        has_text="내 환급금 조회하기"
    )

    expect(refund_cta).to_be_visible()


def test_click_refund_inquiry_cta_shows_kakao_login_button(go_to_login_page):
    """
    [TC-02]
    '내 환급금 조회하기' CTA 클릭 시
    '카카오 계정으로 계속하기' 버튼이 노출되는지 확인한다.
    """
    kakao_login_button = go_to_login_page.get_by_role(
        "button",
        name="카카오 계정으로 계속하기"
    )
    expect(kakao_login_button).to_be_visible()


def test_click_kakao_login_button_redirects_to_kakao_login_page(page):
    """
    [TC-03]
    '카카오 계정으로 계속하기' 버튼 클릭 시
    카카오 로그인 페이지(accounts.kakao.com/login)로
    정상 이동하는지 확인한다.
    """

    page.goto(BASE_URL) 
    refund_cta = page.locator( 
	"a#lp-pom-button-1353 span", 
	has_text="내 환급금 조회하기" 
    ) 
    refund_cta.click() 

    page.wait_for_url("**/login")
	
    kakao_login_button = page.locator( 
	"button span", 
	has_text="카카오 계정으로 계속하기" 
    ) 
    expect(kakao_login_button).to_be_visible() 
    kakao_login_button.click()

    page.wait_for_url("**accounts.kakao.com/login/**")

    assert "accounts.kakao.com/login" in page.url, (
        f"카카오 로그인 페이지로 이동하지 않음: {page.url}"
    )


