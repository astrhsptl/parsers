from selenium import webdriver
import time
from multiprocessing import Pool

def get_parse(urla: str):
    try:
        result = {}
        options = webdriver.FirefoxOptions()

        options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Firefox/84.0")


        driver = webdriver.Firefox(
            executable_path="/home/nia/Desktop/mans/Guides-and-manuals/selen/g_drive/geckodriver",
            options=options
        )
        driver.get(urla)
        someone = driver.find_element_by_class_name("_25d45facb5--close--C4TsU").click()
        driver.find_element_by_class_name("_25d45facb5--button--Cp1dl").click()
        pages = driver.find_elements_by_class_name("_93444fe79c--card--ibP42")
        for i in range(0, len(pages)):
            pages[i].click()
            driver.implicitly_wait(10)
            driver.switch_to.window(driver.window_handles[1])
            key = driver.find_elements_by_class_name("a10a3f92e9--title--UEAG3")[0].text
            value = driver.find_element_by_tag_name("span").find_element_by_xpath('//*[@itemprop="price"]')

            try:
                result[f'{key}, {i}'] = value.text
            except:
                result[key] = None
            driver.close()
            driver.implicitly_wait(10)
            driver.switch_to.window(driver.window_handles[0])
            
        driver.find_element_by_class_name("_93444fe79c--list-itemLink--BU9w6").click()
        time.sleep(100)
    except Exception as ex: 
        print('mm')
    finally:
        print(result)
        driver.close()
        driver.quit()
        return result

if __name__ == '__main__':
    cascade = 'https://spb.cian.ru'

    urls = [
        '/cat.php?currency=2&deal_type=rent&district%5B0%5D=150&engine_version=2&maxprice=65000&offer_type=flat&room2=1&type=4',
        '/cat.php?currency=2&deal_type=rent&district%5B0%5D=150&engine_version=2&maxprice=65000&offer_type=flat&p=2&room2=1&type=4',
        '/cat.php?currency=2&deal_type=rent&district%5B0%5D=150&engine_version=2&maxprice=65000&offer_type=flat&room2=1&type=4&p=3',
        '/cat.php?currency=2&deal_type=rent&district%5B0%5D=150&engine_version=2&maxprice=65000&offer_type=flat&room2=1&type=4&p=4',
    ]

    curr_urls = [cascade+i for i in urls]
    print(curr_urls)
    p = Pool(processes=4)
    p.map(get_parse, curr_urls)