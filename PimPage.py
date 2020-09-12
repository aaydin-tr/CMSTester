import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Tools import getBrowser, switchFrame


def optionalFrames():
    den = getBrowser().find_element_by_xpath("/html/body/div[5]/ul/li[2]/ul/li[1]/ul/li[1]/a")
    time.sleep(2)
    getBrowser().execute_script("arguments[0].click();", den)
    switchFrame()
    getBrowser().find_element_by_id("btnSave").click()
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/input[1]")
    time.sleep(2)
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/input[2]").click()
    time.sleep(2)
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/input[3]").click()
    time.sleep(2)
    getBrowser().find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/input[4]").click()
    time.sleep(2)
    getBrowser().find_element_by_id("btnSave").click()
    try:
        getBrowser().find_element_by_xpath("/html/body/div[1]")
        print("İsteğe bağlı alanlar denetimi başarılı.")
    except:
        print("Alanlarını denetiminde hata oluştu.")

def customFields():
    try:
        pim = getBrowser().find_element_by_xpath('//*[@id="pim"]/a')
        config = getBrowser().find_element_by_xpath('//*[@id="pim"]/ul/li[1]/a')
        custom = getBrowser().find_element_by_xpath('//*[@id="pim"]/ul/li[1]/ul/li[2]/a')
        action = ActionChains(getBrowser())
        action.move_to_element(pim).move_to_element(config).move_to_element(custom).click().perform()
        time.sleep(3)
        switchFrame()
        getBrowser().find_element_by_id("customField_name").send_keys("DenemeAlanı")
        Select(getBrowser().find_element_by_id("customField_screen")).select_by_index(2)
        Select(getBrowser().find_element_by_id("customField_type")).select_by_index(1)
        getBrowser().find_element_by_id("btnSave").click()
        getBrowser().implicitly_wait(10)
        getBrowser().find_element_by_id("messageBalloon_success").text
        print("İsteğe bağlı alanlar denetimi başarılı.")
    except:
        print("Sayfa gösteriminde hata oluştu..")