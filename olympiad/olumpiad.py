from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd 
from twocaptcha import TwoCaptcha
import urllib.request


opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

solver = TwoCaptcha('483b7730b66592a812ca46d5ddd4ef3c')

section_list=['A', 'B', 'C', 'D', 'E', 'F', 'G']
#exam_list=["SOF IMO 2023-24", "SOF NSO 2023-24", "SOF IEO 2023-24", "SOF IGKO 2023-24"]
exam_list=["SOF IEO 2023-24", "SOF IGKO 2023-24"]

n_start=141
n_stop=270
section_idx=4
section=section_list[section_idx]
print(section)
# using chrome driver
driver=webdriver.Chrome()

total_count_captcha=0
good_count_captcha=0
bad_count_captcha=0
consc_fails=0
next_exam=0
list_dict=[]

#for i in range(1,34):
for exam in exam_list:
    print("Exam: ", exam)
    for i in range(n_start,n_stop+1):
        print("Roll: ", i)
        print("Section", section)
        # web page url
        driver.get("https://results.sofworld.org/results")
        
        # find id of option
        x = driver.find_element("name", 'olympiad_selected')
        drop=Select(x)
        
        # select by visible text
        drop.select_by_visible_text(exam)
        #time.sleep(4)
        #driver.close()

        driver.find_element("name", 'rollid1').send_keys("KA0060")
        driver.find_element("name", 'rollid2').send_keys("03")
        driver.find_element("name", 'rollid3').send_keys(section)
        driver.find_element("name", 'rollid4').send_keys(str(i).zfill(3))

        try_captcha_again=1
        wrong_section=0
        while(try_captcha_again or wrong_section):
            if wrong_section:
                driver.implicitly_wait(10)
                driver.get("https://results.sofworld.org/results")
                
                # find id of option
                x = driver.find_element("name", 'olympiad_selected')
                drop=Select(x)
                
                # select by visible text
                drop.select_by_visible_text(exam)
                #time.sleep(4)
                #driver.close()

                driver.find_element("name", 'rollid1').send_keys("KA0060")
                driver.find_element("name", 'rollid2').send_keys("03")
                driver.find_element("name", 'rollid3').send_keys(section)
                driver.find_element("name", 'rollid4').send_keys(str(i).zfill(3))
                wrong_section=0
            img = driver.find_element(By.XPATH, '//div[@class="fieldset-wrapper"]/img')
            src = img.get_attribute('src')
            src_old=src
            #print(src)

            try:

                #captcha = input("Enter Captcha: ") 
                #captcha = solver.normal(src, param1=..., ...)
                urllib.request.urlretrieve(src, "captcha.jfif")
                total_count_captcha=total_count_captcha+1
                captcha = solver.normal("captcha.jfif")
                #print(captcha)
                print("Decoded Captcha: ", captcha['code'])
                driver.find_element("name", 'captcha_response').send_keys(captcha['code'])

                driver.find_element("name", 'op').click()

                #texto=driver.find_elements(By.CLASS_NAME, 'result-cards-no-border').text
                texto = [my_elem.text for my_elem in driver.find_elements(By.CLASS_NAME, "result-cards-no-border")]
                texto[0].splitlines()
                try_captcha_again=0
            except:
                if "wrong" in driver.find_element(By.XPATH, '//div[@id="edit-description"]/h2').text:
                    consc_fails=consc_fails+1
                    if section_idx < len(section_list)-1:
                        print("Section", section)
                        section_idx=section_idx+1
                        section=section_list[section_idx]
                        print("*** IMP NOTE *** : Now Moving to Section", section)
                        wrong_section=1
                    else:
                        print("***IMP NOTE***: Finished all sections. Move to next Exam")
                        next_exam=1
                        break
                    if consc_fails >= 2:
                        raise Exception("***ERROR***: Wrong Roll Number")
                else:
                    print("ERROR: Wrong Captcha?")
                    try_captcha_again=1
                    bad_count_captcha=bad_count_captcha+1
                    print("Total Captcha: ", total_count_captcha, ".   Good: ", good_count_captcha, ".   Bad: ", bad_count_captcha)
            else:
                consc_fails=0
                try_captcha_again=0
                good_count_captcha=good_count_captcha+1
                print("Total Captcha: ", total_count_captcha, ".   Good: ", good_count_captcha, ".   Bad: ", bad_count_captcha)
        
        if next_exam:
            next_exam=0
            n_start=1
            section_idx=0
            section=section_list[section_idx]
            break
        else:
            dict1=dict()
            for elem in texto[0].splitlines():
                #print(elem)
                if re.search(':\s*$', elem):
                    key=elem
                else:
                    elem=re.sub(r'/40\s*$',"",elem)
                    dict1[key]=elem
            print(dict1)
            list_dict.append(dict1)
            df = pd.DataFrame(list_dict) 
            df.to_csv("olympiad.csv")

    n_start=1

















































#df

        # get the image source
        #img = driver.find_element()
        #src = img.get_attribute('src')

        # download the image
        #urllib.urlretrieve(src, "captcha.png")

        # get the image source
        #img = driver.find_element(By.X_PATH, '//div[@class="fieldset-wrapper"]/img')
        #src = img.get_attribute('src')

        # download the image
        #urllib.urlretrieve(src, "captcha.png")

        #.get_attribute("src")
        #print(driver.find_element_by_xpath("//div[@class='c-label']/img[@class='c-label__image']").get_attribute("title"))

        #captcha = input("Enter Captcha: ") 
        #captcha = solver.normal('path/to/captcha.jpg', param1=..., ...)
        #driver.find_element("name", 'captcha_response').send_keys(captcha)

        #driver.find_element("name", 'op').click()

        #texto=driver.find_elements(By.CLASS_NAME, 'result-cards-no-border').text 
        #texto = [my_elem.text for my_elem in driver.find_elements(By.CLASS_NAME, "result-cards-no-border")]

        #print(texto[0].splitlines())
        #print(texto[0])


                # test=driver.find_element("name", 'captcha_response').get_attribute("border-bottom-color")
                # print("Border: ", test)
                # img = driver.find_element(By.XPATH, '//div[@class="fieldset-wrapper"]/img')
                # src = img.get_attribute('src')
# _attribute('src')
