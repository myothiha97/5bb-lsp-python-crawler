from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
from info import user_info
from datetime import date
import os
import json
import csv
chrome_option = Options()
chrome_option.add_experimental_option("prefs",{"download.default_directory":"C:\5bb_lsp_csv"})
driver = webdriver.Chrome(executable_path=r"C:\Users\Myo Thiha Kyaw\Desktop\chrome\chromedriver.exe",chrome_options=chrome_option)
driver.get("http://172.30.0.14:8081/pos")
user_name = driver.find_element(By.ID,"username")
pass_word = driver.find_element(By.ID,"password")

user_name.send_keys(user_info["username"])
pass_word.send_keys(user_info["password"])
pass_word.send_keys(Keys.ENTER)
# driver.find_element(By.XPATH,'//*[@id="wrapper"]/app-root/nav/div/button').click
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="bs-navbar"]/ul/li[2]/a')))
opportunity_tab = driver.find_element(By.XPATH,'//*[@id="bs-navbar"]/ul/li[2]/a').click()
print("clicked")
wait = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="bs-navbar"]/ul/li[2]/ul/li[3]')))
select_element = driver.find_element(By.XPATH,'//*[@id="bs-navbar"]/ul/li[2]/ul/li[3]').click()

date_format = date.today()
current_date = date_format.strftime("%d")
current_day = str(int(current_date) - 1)
print(current_day)
# if current_days > 0 and current_days <=8:
#     current_day = str(current_days)
# elif current_days > 8 and current_days <= 15:
#     current_day = str(20 - current_days)
# elif current_days > 15 and current_days <=22:
#     current_day=str(30)
    
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="page-wrapper"]/div/div/app-i-order-search/div/div[2]/form/div/div[8]/div/input')))

fetch_date = driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div/div/app-i-order-search/div/div[2]/form/div/div[8]/div/input').click()
time.sleep(3)

select_date = driver.find_element(By.XPATH,"//*[contains(@id,'{}')]/button".format(current_day)).click()
time.sleep(3)
chose_date=driver.find_element(By.XPATH,'//*[@id="page-wrapper"]/div/div/app-i-order-search/div/div[2]/form/button').click()


time.sleep(3)
try:
    download_button=driver.find_element(By.XPATH,'/html/body/div[1]/app-root/div/div/div/app-i-order-search/search-component/div[2]/div/div[1]/div/a').click()
except:
    print("There is no file to download or invalid xpath")
else:
    print("Donwload completed")
finally:
    time.sleep(2)
    driver.close()


def read_csv_file(file_name):
    file = r"C:\Users\Myo Thiha Kyaw\Downloads\{}.csv".format(file_name)

    csv_file = []
    with open(file) as csvDataFile:
        csv_data = csv.reader(csvDataFile)
        for row in csv_data:
        #    print(row)
            csv_file.append(row)
    return csv_file
csv_data = read_csv_file("export")
dict_data = [i for i in csv_data[0]]
datas=[]
for i in range(len(csv_data)-1):
    # lis1 = [i for i in csv_datas[i+1]]
    change_dict = dict(zip(dict_data,csv_data[i+1]))
    # datas.append(dict(zip(dict_data,[y for y in csv_data[i+1]])))
    datas.append(change_dict)
# print(datas)
json_data = json.dumps(datas,indent=4)
print(json_data)
if os.path.exists(r"C:\Users\Myo Thiha Kyaw\Downloads\export.csv"):
      os.remove(r"C:\Users\Myo Thiha Kyaw\Downloads\export.csv")
      print("File deleted")
else:
  print("The file does not exist")
  
  
  
