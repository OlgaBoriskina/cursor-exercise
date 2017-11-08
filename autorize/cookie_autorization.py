import pickle

def autirize (driver):
    with open("cookies.pkl", "rb") as read:
        cookies = pickle.load(read)
    for cookie in cookies:
        driver.add_cookie(cookie)