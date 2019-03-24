#!/user/bin/env python3

from pywinauto.keyboard import SendKeys
from pywinauto.application import Application
import time

def main():
  count = 0

  Application().Start(cmd_line=u'control intl.cpl')
  app = Application().connect(title_re="Region")
  dlg = app.Region
  dlg.SystemLink2.Click()
  time.sleep(0.4)

  app2 = Application().connect(title_re="Language")
  dlg2 = app2.Language
  dlg2.SysListView32.Click(double=True)

  while count < 2:
    SendKeys('{VK_TAB}')
    time.sleep(0.1)
    count += 1
  SendKeys('{VK_RETURN}')#add input method

  while count < 8:
    SendKeys('{VK_DOWN}')
    count += 1
    time.sleep(0.1)
  SendKeys('{VK_RETURN}')#Selects Dvorak in layout choices

  dlg2.SaveButton.click()#saves settings


  SendKeys('%{F4}')
  time.sleep(0.4)
  SendKeys('%{F4}')

if __name__ == '__main__':
    main()
