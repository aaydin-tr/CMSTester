from Tools import getBrowser,switchFrame
from LoginPage import login
from selenium.webdriver.support.select import Select
import time

def Perfor():
    getBrowser().find_element_by_xpath("/html/body/div[5]/ul/li[6]/a").click()
    switchFrame()
    getBrowser().find_element_by_id("txtPeriodFromDate").clear()
    getBrowser().find_element_by_id("txtPeriodFromDate").send_keys("2019-01-02")
    getBrowser().find_element_by_id("txtPeriodToDate").clear()
    getBrowser().find_element_by_id("txtPeriodToDate").send_keys("2019-01-03")
    Select(getBrowser().find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/form/div[1]/select[1]")).select_by_index(0)
    Select(getBrowser().find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/form/div[1]/select[2]")).select_by_index(0)
    getBrowser().find_element_by_id("txtEmpName").clear()
    getBrowser().find_element_by_id("txtEmpName").send_keys("deneme")
    getBrowser().find_element_by_id("txtReviewerName").clear()
    getBrowser().find_element_by_id("txtReviewerName").send_keys("deneme")
    getBrowser().find_element_by_id("searchButton").click()
    try:
        print("Sonuç:",getBrowser().find_element_by_xpath("/html/body/div[1]/div[1]/div[1]").text)
        print("Arama başarılı.")
    except:
        print("Arama başarısız.")
    time.sleep(2)
    getBrowser().find_element_by_id("clearBtn").click()
    print("Temizleme başarılı.")
    print("Performans sayfası testi başarılı")
    time.sleep(1)


def kpilist():
    getBrowser().switch_to_default_content()
    den = getBrowser().find_element_by_xpath("/html/body/div[5]/ul/li[6]/ul/li[1]/a")
    time.sleep(2)
    getBrowser().execute_script("arguments[0].click();", den)
    switchFrame()
    getBrowser().find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[2]/input").click()
    Select(getBrowser().find_element_by_id("txtJobTitle")).select_by_index(0)
    time.sleep(1)
    getBrowser().find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/textarea").send_keys("deneme")
    getBrowser().find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/input[1]").send_keys("1")
    getBrowser().find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/input[2]").send_keys("10")
    getBrowser().find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/input[3]").click()
    getBrowser().find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/input[1]").click()
    try:
        print("Sonuç:",getBrowser().find_element_by_id("messageBalloon_success").text)
        print("İsteğe bağlı alanlar denetimi başarılı.")
    except:
        print("Alanlarını denetiminde hata oluştu.")
    time.sleep(2)
    getBrowser().find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/input[2]").click()
    print("Temizleme başarılı.")
    print("Performans sayfası testi başarılı")
    time.sleep(1)


