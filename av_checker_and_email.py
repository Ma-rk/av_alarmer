import time
import logging

import smtplib
from email.mime.text import MIMEText

from selenium import webdriver

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def send_mail(opened: bool):
    # 세션 생성
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # TLS 보안 시작
    s.starttls()

    # 로그인 인증
    s.login('', '')

    # 보낼 메시지 설정
    if opened:
        msg = MIMEText('어벤져스 오픈 했다 ㅎㅎㅎㅎㅎㅎ')
    else:
        msg = MIMEText('어벤져스 아직 오픈 안했다 ㅋ')
    msg['Subject'] = '어벤져스 오픈했니?'

    # 메일 보내기
    s.sendmail("", "", msg.as_string())

    # 세션 종료
    s.quit()


capabilities = webdriver.DesiredCapabilities.CHROME

url = 'http://ticket.cgv.co.kr/Reservation/Reservation.aspx?MOVIE_CD=&amp;MOVIE_CD_GROUP=&amp;PLAY_YMD=&amp;THEATER_CD=&amp;PLAY_NUM=&amp;PLAY_START_TM=&amp;AREA_CD=&amp;SCREEN_CD=&amp;THIRD_ITEM='

options = webdriver.ChromeOptions()
options.add_argument('headless')

while True:
    driver = webdriver.Chrome('/Volumes/Drive_D/temp_code/crawl/selenium/chromedriver',
                              desired_capabilities=capabilities,
                              chrome_options=options)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.get(url)

    time.sleep(3)
    if '어벤저스' in driver.page_source:
        send_mail(True)
        break
    else:
        logger.info('not yet haha')
        send_mail(False)

    driver.quit()

