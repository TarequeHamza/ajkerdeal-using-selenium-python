from selenium.webdriver.common.by import By


class RegistrationPageLocators(object):
    LOGIN_BTN = (By.XPATH, "//a[@id='hover-Id']")
    REGISTER_BTN = (By.LINK_TEXT, 'রেজিস্টার')
    NAME = (By.XPATH, "//input[@id='NameTextBox']")
    PHONE = (By.XPATH, "//input[@id='MobileTextBox']")
    EMAIL = (By.XPATH, "//input[@id='EmailTextBoxs']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    AGAIN = (By.XPATH, "//input[@id='againPassowrd']")
    REGISTER = (By.XPATH, "//input[@id='SignupButton']")
    MALE = (By.XPATH, "//input[@id='MaleRadioButton']")
    REGISTRATION_BTN = (By.XPATH, "//*[@id='SignupButton']")


class LoginPageLocators(object):
    LOGIN_BTN = (By.XPATH, "//a[@id='hover-Id']")
    SET_EMAIL = (By.XPATH, "//input[@id='Email']")
    SET_PASS = (By.XPATH, "//input[@id='Password']")
    CLICK_LOGIN_BTN = (By.XPATH, "//*[@id='active-hover']/ul/div[3]/input")



class SearchPageLocators(object):
    SEARCH_BAR = (By.XPATH, "//input[@id='txtName']")
    SEARCH_BTN = (By.XPATH, "//header/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/button[1]")


class CategoryPageLocators(object):
    WATCH_BTN = (By.XPATH, "/html/body/div/section[2]/div/div/div/div/div[1]/div/ul/li[8]")
    TABLE_BTN = (By.XPATH, "//*[@id='menu']/ul/li[8]/ul/li[7]/a")


class LangcngPageLocators(object):
    ENG_BTN = (By.XPATH, "/html/body/header/div[1]/div/div/div[2]/div/ul/li[5]/div/div[2]/a")


class GadgetsPageLocators(object):
    SW_BTN = (By.XPATH, "//*[@id='gagetDealTitle']/div[3]/button[1]")


class HotdealPageLocators(object):
   PANT_BTN = (By.XPATH, "//*[@id='hotDealTitle']/div[3]/button[5]")


class MfashionPageLocators(object):
    HIJAB_BTN = (By.XPATH, "//*[@id='muslim-fasion']/div/div[2]/a/img")


class VideosPageLocators(object):
   VIDEO_BTN = (By.XPATH, "//*[@id='vAd']/div[1]/a/span[1]/img")


class CcarePageLocators(object):
    CCR_BTN = (By.XPATH, "//*[@id='footerContent']/div[1]/div/div/div[1]/div[1]/h4")


class CommunicationPageLocators(object):
    CMMU_BTN = (By.XPATH, "//*[@id='footerContent']/div[1]/div/div/div[1]/div[1]/ul/li[7]/a")


class HelpcenterPageLocators(object):
    HLC_BTN = (By.XPATH, "//a[contains(text(),'হেল্প সেন্টার')]")


class HowdoorderPageLocators(object):
    HDO_BTN = (By.XPATH, "//a[contains(text(),'কিভাবে অর্ডার করবেন')]")


class TrackorderPageLocators(object):
    TRO_BTN = (By.XPATH, "//*[@id='footerContent']/div[1]/div/div/div[1]/div[1]/ul/li[3]/a")


class RetrunrefundpPageLocators(object):
    RRP_BTN = (By.XPATH, "//a[contains(text(),'রিটার্ন ও রিফান্ড পলিসি')]")



class PrivacypPageLocators(object):
    PP_BTN = (By.XPATH, "//a[contains(text(),'প্রাইভেসী পলিসি')]")


class ProductcpPageLocators(object):
    PCP_BTN = (By.XPATH, "//a[contains(text(),'প্রােডাক্ট পরিবর্তন প্রক্রিয়া')]")


class OuraddressPageLocators(object):
    OAD_BTN = (By.XPATH, "//a[contains(text(),'আমাদের ঠিকানা')]")


class AjkerdilbPageLocators(object):
    ADB_BTN = (By.XPATH, "//a[contains(text(),'আজকেরডিল ব্লগ')]")


class SitemapPageLocators(object):
    SM_BTN = (By.XPATH, "//a[contains(text(),'সাইট ম্যাপ')]")
