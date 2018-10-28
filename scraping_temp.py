import urllib.request
import urllib.error
import re

url = "https://www.kuaidaili.com/free/inha/"
Regex = r"<td data-title=\"IP\">(.+?)</td>"

try:
	for count in range(5):
		temp_url = url + str(count)
		res = urllib.request.urlopen(temp_url).read().decode('utf-8')
		IP_res = re.findall(Regex, res)
		for i in IP_res:
			print("IP: " + str(i))
except urllib.error.HTTPError as e:
	if hasattr(e, 'code'):
		print("HTTP_ErrorCode:" + str(e.code))
except urllib.error.URLError as e:
	if hasattr(e, 'reason'):
		print("URL_ErrorReason:" + str(e.reason))
else:
	print("Success!")