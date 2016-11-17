#!/usr/bin/python2
# coding:utf-8

while True:
  try:
    bro.find_elements(By.XPATH, '//a[text()="Add"]')[0].click()
    time.sleep(3)
    bro.find_elements_by_xpath("//input[@id='groupMembersInput']")[0].click()

    time.sleep(10)

    for x in range(20):
      try:
        bro.find_elements_by_xpath("//li[@class='user']")[0].click()
      except:
        pass

    time.sleep(1)
    # bro.find_elements_by_xpath("//button[@class='_42ft _4jy0 layerConfirm uiOverlayButton _4jy3 _4jy1 selected _51sy']")[0].click()
    try:
      bro.find_elements(By.XPATH, '//button[text()="Add"]')[0].click()
    except:
      bro.find_elements(By.XPATH, '//button[text()="Add"]')[0].send_keys(Keys.ESCAPE)
      bro.find_elements(By.XPATH, '//button[text()="Add"]')[0].click()

    time.sleep(15)
    try:
      bro.find_elements(By.XPATH, '//button[text()="Done"]')[0].click()
    except:
      bro.find_elements(By.XPATH, '//button[text()="Okay"]')[0].click()
    time.sleep(5)
  except Exception, e:
    print 'ERRO:', str(e)
    bro.get('https://www.facebook.com/groups/alfenasmg/members/')
    time.sleep(6)
