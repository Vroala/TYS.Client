import webbrowser, time, os

search = input('검색어: ')
new = 2

opUrl = 'http://search.naver.com/search.naver?where=nexearch&query=' + search
webbrowser.open(opUrl)

time.sleep(1)

serUrl = 'chrome://settings/clearBrowserData'
webbrowser.open(serUrl)

#time.sleep(2)
#browserExe = "chrome.exe"
#os.system("taskkill /f /im "+browserExe)