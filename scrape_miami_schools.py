from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

url=[]
url.append('http://www.dadeschools.net/schools/schoolinformation/default_printable.asp?type=1&searchterm=')
url.append('http://www.dadeschools.net/schools/schoolinformation/default.asp?type=2#list')
url.append('http://www.dadeschools.net/schools/schoolinformation/default.asp?type=3#list')
url.append('http://www.dadeschools.net/schools/schoolinformation/default.asp?type=6#list')

s_type=[]
s_type.append('e')
s_type.append('m')
s_type.append('h')
s_type.append('k')

schools = []
address= []
phone = []
principal=[]
school_type = []

# elem info
#            str_td = td_info[3]
#            addr_1 = str_td.lstrip()
#            addr_2 = td_info[5]

# middle info
#            str_td = td_info[4]
#            addr_1 = str_td.lstrip()
#            addr_2 = td_info[6]

# 4 types of schools to be webscraped - elementary, middle, K8 centers and high schools
           
def scrape_info():
    browser = init_browser()
    i = 0

    for s_url in url:
        print(i, s_url)
        browser.visit(s_url)
        html = browser.html
        soup = bs(html, 'html.parser')

        tbody = soup.find('tbody')

        all_td = tbody.find_all('td')
        

        catch_school = False
        catch_phone = False

        for each_td in all_td:
            try:
              td_a = each_td.find('a', class_='bluelink')
              strong_tag = td_a.find('strong')
              print('strong_tag ', strong_tag)  
              if (len(strong_tag.text)>1):
                school_name = strong_tag.text
                td_info = each_td.contents
                print('td_info : ', td_info)
                if (i == 0):
                    str_td = td_info[3]
                    addr_1 = str_td.lstrip()
                    addr_2 = td_info[5]
                else:    
                    str_td = td_info[4]
                    addr_1 = str_td.lstrip()
                    addr_2 = td_info[6]
                schools.append(school_name)
                address.append(addr_1 +' ' + addr_2)
                print(school_name, addr_1+' '+addr_2)
                catch_school = True
            except:
                try:
                    if (catch_school):
                       td_font = each_td.find_all('div')
                       phone_contents = each_td.contents
                       phone_info = str(phone_contents[0])
                       print('phone_info : ', phone_info)
                       words=[]
                       words = phone_info.split('</font>')
                       words_2=[]
                       words_2 = words[1].split('<br/>')
                       phone.append(words_2[0]) 
                       catch_phone = True
                
                except:
                    try:
                       if (catch_school and catch_phone):
                           td_principal = str(each_td.contents[0])
                           principal.append(td_principal)
                           school_type.append(s_type[i])
                           print('principal: ', td_principal)
                           catch_school = False
                           catch_phone = False
                    except:
                       print('error')

        i+=1
        # Close the browser after scraping
        browser.quit()


        
        
        
    df = pd.DataFrame({
         "school": schools,
         "address": address,
         "phone": phone,
         "principal" : principal,
         "type" : school_type
        })

        
    print('done')
    df.to_csv('output/miami_dade_schools.csv')
    # Return results
    return 



