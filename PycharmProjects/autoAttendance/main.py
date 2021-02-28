# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def go(input_id, input_password):
    print(input_id, end='')
    from selenium import webdriver
    import time

    print("Firefox open")
    browser = webdriver.Firefox()
    print("a-ha.io site open")
    browser.get("http://www.a-ha.io/")

    print("a-ha.io site stamp menu find")
    menus = browser.find_elements_by_css_selector('.home-container section.homeButtons div')

    pypi = None
    for m in menus:
        if m.text == "출석스탬프":
            pypi = m
            break

    pypi.click()  # 클릭
    print("a-ha.io site stamp menu click")
    time.sleep(3)

    kakao_login_button_xpath = "/html/body/div/div/div/main/div/div/div/button"
    browser.find_element_by_xpath(kakao_login_button_xpath).click()
    print("a-ha.io site kakao login click")
    time.sleep(3)


    # print("a-ha.io site popup find")
    # current_window_handle = browser.current_window_handle
    # while len(browser.window_handles) == 1:
    #     time.sleep(3)
    # print("a-ha.io site popup select")
    # browser.switch_to.window(browser.window_handles[1])
    #


    id = browser.find_element_by_id("id_email_2")
    id.clear()
    id.send_keys(input_id)
    print("a-ha.io site login id typing")
    time.sleep(1)

    password = browser.find_element_by_id("id_password_3")
    password.clear()
    password.send_keys(input_password)
    print("a-ha.io site login password typing")
    time.sleep(1)

    login_button_xpath = "/html/body/div[1]/div[2]/div/div/div/div/div[2]/div/form/fieldset/div[8]/button[1]"
    browser.find_element_by_xpath(login_button_xpath).click()
    print("a-ha.io site login button click")
    time.sleep(3)


    # browser.switch_to.window(current_window_handle)

    check_attendance_button_xpath = "/html/body/div/div/div/div/section/div[3]/div[2]/div/div/header/button"
    browser.find_element_by_xpath(check_attendance_button_xpath).click()
    print("a-ha.io site stamp button click")

    time.sleep(5)  # 5초 대기
    browser.quit()  # 브라우저 종료
    print("Done")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    try:
        print("Start")

        go("yprite@gmail.com", "")
        go("yprite@jjssm.org", "")

        print("End")
    except Exception as E:
        print(E)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
