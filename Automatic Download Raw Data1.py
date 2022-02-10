from selenium import webdriver
import pickle
path_to_downloads = 'C:/xxx/xxx' #customized download files' location
edge_driver_path= 'C:/xxx/xxx/msedgedriver.exe'  #location of msedgedriver
driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get('https://www.census.gov/data/datasets/time-series/demo/cps/cps-basic.2021.html')
elems=driver.find_elements_by_css_selector(".pagetab ul li a")
webLinks=[elem.get_attribute('href') for elem in elems if elem.get_attribute('href')]
fileLinks_all=[]
for webLink in webLinks:
    driver.get(webLink)
    elems = driver.find_elements_by_name('DOS/Windows	')
    fileLinks = [elem.get_attribute('href') for elem in elems if 'pub' in str(elem.get_attribute('href'))]
    fileLinks_all.extend(fileLinks)
pickle.dump(fileLinks_all, open( "fileLinks_all", "wb" ) )




