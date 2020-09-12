from selenium import webdriver

browser = ""


def getBrowser():
    global browser
    if browser == "":
        browser = webdriver.Chrome(executable_path=r"YourDriverPath")
    return browser


def switchFrame():
    global browser
    browser.implicitly_wait(3)
    frame = getBrowser().find_element_by_xpath("/html/body/div[6]/iframe")
    browser.switch_to_frame(frame)


def exit():
    global browser
    browser.quit()
    browser = ""
