import config
from datetime import datetime
from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as ExpectedCondition

load_dotenv()

driver = config.setup()
config.login(driver)

wait = WebDriverWait(driver, 30)

club_username = os.getenv("INSTAGRAM_CLUB_USERNAME")

driver.get("https://www.instagram.com/" + club_username)


def time_difference(past_date):
    date1 = datetime.now()
    date2 = datetime.strptime(past_date, "%Y-%m-%dT%H:%M:%S.%fZ")

    difference = date1 - date2

    return difference.days


try:
    wait.until(ExpectedCondition.element_to_be_clickable((By.CLASS_NAME,
                                                          "_aagw")))
    post = driver.find_element(By.CLASS_NAME, "_aagw")
    post.click()
except Exception:
    assert False, "Can't click the latest post"

info_lst = []
while True:
    try:
        wait.until(ExpectedCondition.presence_of_element_located((
                                                                By.CLASS_NAME,
                                                                "_a9zs"
                                                              )))
        post_caption = driver.find_element(By.CLASS_NAME, "_a9zs").text
    except Exception:
        assert False, "Can't get the caption of a post"

    try:
        wait.until(ExpectedCondition.presence_of_element_located((
                                                                By.CLASS_NAME,
                                                                "_a9ze._a9zf"
                                                              )))
        post_date_element = driver.find_element(By.CLASS_NAME, "_a9ze._a9zf")
        post_date = post_date_element.get_attribute("datetime")
    except Exception:
        assert False, "Can't get the date of a post"

    diff = time_difference(post_date)

    # If the date of the post was less than two months ago
    #   and the caption mentions application
    if ("application" in post_caption.lower()) and (diff < 60):
        info_lst.append(post_caption)

    if (diff < 60):
        try:
            wait.until(ExpectedCondition.element_to_be_clickable((
                                                    By.CSS_SELECTOR,
                                                    "svg[aria-label='Next']"
                                                  )))
            next_post = driver.find_element(By.CSS_SELECTOR,
                                            "svg[aria-label='Next']")
            next_post.click()
        except Exception:
            assert False, "Can't view the next post"
    else:
        break

num = 0
while num < len(info_lst):
    print(info_lst[num])
    print("\n\n\n")
    num = num + 1

driver.quit()
