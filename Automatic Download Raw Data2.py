import pickle
import os
import time
from msedge.selenium_tools import Edge, EdgeOptions
edge_options = EdgeOptions()
edge_driver_path= 'C:/xxx/xxx/msedgedriver.exe' #location of msedgedriver
download_path='C:/xxx/xxx/xxx' #customized download files' location
# change default download location to download directory
prefs = {'download.default_directory':download_path}
edge_options.add_experimental_option('prefs', prefs)
fileLinks_all=pickle.load(open( "fileLinks_all", "rb" ))
def latest_download_file():
      path = download_path
      os.chdir(path)
      files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
      time.sleep(5)
      newest = files[-1]
      return newest
#print(len(fileLinks_all))
for file in fileLinks_all:
    driver = Edge(executable_path=edge_driver_path, options=edge_options)
    driver.get(file)
    start=True
    seconds=0
    newest_file='start'
    while newest_file.endswith('crdownload') or start:
        time.sleep(1)
        start=False
        newest_file = latest_download_file()
        seconds+=1
        if seconds%60 == 0:
            print(f'download {seconds} seconds for {file}')
    driver.close()
    print(file)



