from Tools import getBrowser


def login(username, password):
    getBrowser().maximize_window()
    getBrowser().get("https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php")
    getBrowser().find_element_by_css_selector("input[name='txtUsername']").send_keys(username)
    getBrowser().find_element_by_css_selector("input[name='txtPassword']").send_keys(password)
    getBrowser().find_element_by_id("btnLogin").click()
    try:
        getBrowser().find_element_by_id("spanMessage").is_displayed()
        print("Hatalı giriş")
    except:
        print("Giriş başarılı")

def logout():
    getBrowser().find_element_by_link_text("Logout").click()
    print("Çıkış başarılı")