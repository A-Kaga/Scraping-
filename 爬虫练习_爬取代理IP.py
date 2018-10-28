import urllib.request
import urllib.error
import urllib.parse
import time
import re

# 1 for 
signle_web_flag = 0
proxy_flag = 1

headers = {'Accept': 'text/html,application/xhtml+xml,\
        application/xml;q=0.9,image/webp,image/apng,\
        */*;q=0.8',
       'Accept-Language': 'zh-CN,zh;q=0.9',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.3;\
                      Win64;\
                      x64) AppleWebKit/537.36 (KHTML, \
                      like Gecko)Chrome/48.0.2564.48 \
                      Safari/537.36'
       }
proxy = {'http': '49.81.125.62:9000'}
url = "https://www.kuaidaili.com/free/inha/"
Regex = r"<td data-title=\"IP\">(.+?)</td>"


proxy_handler = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(proxy_handler)


try:
	if signle_web_flag == 1:
		res = urllib.request.urlopen(url).read().decode('utf-8')
		IP_res = re.findall(Regex, res)
		for i in IP_res:
			print("IP: " + str(i))
	else:
		for count in range(1, 6):
			print('----------' + 'Page ' + str(count) + '----------')
			temp_url = url + str(count) + '/'
			response = urllib.request.Request(temp_url, headers = headers)
			if proxy_flag == 1:
				res = opener.open(response).read().decode('utf-8')
				IP_res = re.findall(Regex, res)

				for i in IP_res:
					print("IP: " + str(i))
			else:
				res = urllib.request.urlopen(temp_url).read().decode('utf-8')
				IP_res = re.findall(Regex, res)
				for i in IP_res:
					print("IP: " + str(i))
			time.sleep(1)

except urllib.error.HTTPError as e:
	if hasattr(e, 'code'):
		print("HTTP_ErrorCode:" + str(e.code))

except urllib.error.URLError as e:
	if hasattr(e, 'reason'):
		print("URL_ErrorReason:" + str(e.reason))

else:
	print("Success!")