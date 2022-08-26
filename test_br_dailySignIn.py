import logging
import re
from playwright.sync_api import Page, expect

url = "https://www.blackrock.vip/#/login"
password = "!Abhilash98"
ashal_airtel = "919995146005"
ashal_jio = "917012486572"
reliance_jio = "917012403113"
mummy = "919539914580"


def test_ashal_airtel(page: Page):
    br_signin_bonus(page, ashal_airtel)


def test_ashal_jio(page: Page):
    br_signin_bonus(page, ashal_jio)


def test_mummy(page: Page):
    br_signin_bonus(page, mummy)


def test_reliance_jio(page: Page):
    br_signin_bonus(page, reliance_jio)


def br_signin_bonus(page, username):
    page.goto(url, timeout=1200000)
    expect(page).to_have_title(re.compile("BlackRock"))
    page.locator("//div[contains(@class,'checked')]/i").click()
    # Go to https://www.blackrock.vip/#/login
    # page.goto("https://www.blackrock.vip/#/login")

    # Click [placeholder="Phone number"]
    page.locator("[placeholder=\"Phone number\"]").click()

    # Fill [placeholder="Phone number"]
    page.locator("[placeholder=\"Phone number\"]").fill(username)

    # Click [placeholder="Password"]
    page.locator("[placeholder=\"Password\"]").click()

    # Fill [placeholder="Password"]
    page.locator("[placeholder=\"Password\"]").fill("!Abhilash98")

    # Click text=Log In >> nth=1
    page.locator("text=Log In").nth(1).click()
    page.wait_for_url("https://www.blackrock.vip/#/index")

    # Click button:has-text("Confirm")
    #page.locator("button:has-text(\"Confirm\")").click()

    # Click .item_img > img >> nth=0
    page.locator(".item_img > img").first.click()
    page.wait_for_url("https://www.blackrock.vip/#/sign")

    page.locator("//span[text()='You have signed in for ']").is_visible(timeout=120000)
    text_value = page.locator("//div[contains(@class,'sign_btn')]//span[text()='Sign in' or text()='Succeeded']").text_content()
    print("\ntext_value == "+text_value)

    if text_value == "Sign in":
        page.locator("div:has-text(\"Sign in\")").nth(3).click()
        expect(page.locator("//*[@id='app']/div[1]/div[5]/div/div[2]/span")).to_have_text("Succeeded")
        print("Sign In completed successfully...")
    elif text_value == "Succeeded":
        print("already sign in completed for the day...")
    else :
        print("error in program.. please check code...")
        print(text_value)




    # page.locator("//*[@id='app']/div[1]/div[1]/div[1]").click()


    page.goto("https://www.blackrock.vip/#/index",timeout=12000)
    page.wait_for_url("https://www.blackrock.vip/#/index")

    # Click button:has-text("Confirm")
    #page.locator("button:has-text(\"Confirm\")").click()

    # Click text=Account
    page.locator("text=Account").click()
    page.wait_for_url("https://www.blackrock.vip/#/user")

    # Click div[role="button"]:has-text("Account Settings")
    page.locator("div[role=\"button\"]:has-text(\"Account Settings\")").click()
    page.wait_for_url("https://www.blackrock.vip/#/safe")

    # Click text=Sign Out
    page.locator("text=Sign Out").click()
    page.wait_for_url("https://www.blackrock.vip/#/index")

    # Click button:has-text("Confirm")
    #page.locator("button:has-text(\"Confirm\")").click()

    # Click text=Account
    page.locator("text=Account").click()
    page.wait_for_url("https://www.blackrock.vip/#/login")

    # Click text=Please log in first
    expect(page.locator("text=Please log in first")).to_have_text("Please log in first")

    print("process is completed...")
