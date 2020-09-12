from LoginPage import login, logout
from MainPage import fillInputs, addElements
from Performance import Perfor,kpilist
from PimPage import optionalFrames, customFields
from Tools import exit

print("\nOrangeHRM Sınama Yazılımına Hoşgeldiniz. \n")
print("Tools dosyası içinden driver yolunuzu doğru yazdığınıza emin olunuz.")
print("Login Page dosyası içinden sistemin kurulu olduğu alan adını doğru yazdığınıza emin olunuz.\n")


secenek = -1

while(secenek!=0):
    print("\n1. Giriş sayfası")
    print("2. Anasayfa")
    print("3. Performance")
    print("4. PIM")
    print("\n0. Çıkış")

    secenek = int(input("\nSınamak istediğiniz kısmı seçiniz:"))
    print("")
    if secenek == 1:
        login("opensourcecms","opensourcecms")
        logout()
        exit()
    elif secenek == 2:
        login("opensourcecms", "opensourcecms")
        fillInputs()
        addElements()
        exit()
    elif secenek == 3:
        login("opensourcecms", "opensourcecms")
        Perfor()
        kpilist()
        exit()
    elif secenek == 4:
        login("opensourcecms", "opensourcecms")
        optionalFrames()
        exit()
        login("opensourcecms", "opensourcecms")
        customFields()
        exit()
    else:
        print("Geçersiz giriş")