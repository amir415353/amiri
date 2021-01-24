import json
import requests
import re
import random

def hc_solver(filePath, count):
	proxy1 = ['104.28.5.81:80',
	'104.28.8.77:80',
	'104.28.5.144:80',
	'1.0.0.67:80',
	'104.28.4.190:80',
	'104.28.1.77:80',
	'162.159.246.194:80',
	'172.67.181.156:80',
	'104.28.27.169:80',
	'104.28.6.98:80',
	'1.1.1.190:80',
	'172.67.181.76:80',
	'104.28.16.196:80',
	'1.0.0.116:80',
	'104.28.4.121:80',
	'104.19.125.221:80',
	'1.0.0.114:80',
	'104.28.7.48:80',
	'104.28.6.115:80',
	'104.27.142.28:80',
	'104.28.2.136:80',
	'1.1.1.12:80',
	'167.71.40.51:3128',
	'104.28.4.249:80',
	'185.114.137.14:12457',
	'104.28.5.202:80',
	'104.28.0.99:80',
	'104.28.10.86:80',
	'176.9.85.13:3128'
	'191.101.39.174:80',
	'104.28.30.21:80',
	'104.28.16.54:80',
	'104.28.4.20:80',
	'162.159.242.53:80',
	'104.28.16.29:80',
	'104.28.5.252:80',
	'104.28.31.88:80',
	'1.1.1.54:80',
	'104.28.17.182:80',
	'1.1.1.78:80',
	'104.28.7.232:80',
	'104.28.10.82:80',
	'104.28.12.71:80',
	'104.28.17.180:80',
	'104.28.7.46:80',
	'104.28.17.114:80',
	'1.0.0.69:80',
	'173.245.49.182:80',
	'80.241.251.54:8080',
	'104.28.3.58:80']
	proxy = random.choice(proxy1)
	searchUrl = 'https://yandex.ru/images/search'
	proxies = {"http":"http://" + proxy}
	files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
	params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
	try:
		response = requests.post(searchUrl, params=params, files=files, proxies=proxies)
		query_string = json.loads(response.content)['blocks'][0]['params']['url']
		img_search_url= searchUrl + '?' + query_string
		a = requests.get(img_search_url)
		b = a.text
		t1 = re.findall(r'train', b)
		t2 = re.findall(r'Train', b)
		t22 = re.findall(r'TRAIN', b)
		t23 = re.findall(r'поезд', b)
		t24 = re.findall(r'трамва', b)
		t3 = len(t1) + len(t2) + len(t22) + len(t23) + len(t24)
		b1 = re.findall(r'bus', b)
		b2 = re.findall(r'Bus', b)
		b22 = re.findall(r'BUS', b)
		b111 = re.findall(r'motorbus', b)
		b112 = re.findall(r'Motorbus', b)
		b113 = re.findall(r'MOTORBUS', b)
		b3 = len(b1) + len(b2) + len(b22) + len(b111) + len(b112) + len(b113)
		b4 = re.findall(r'abuse', b)
		b5 = re.findall(r'aria-busy', b)
		b222 = re.findall(r'business', b)
		b223 = re.findall(r'Business', b)
		b224 = re.findall(r'BUSINESS', b)
		b225 = re.findall(r'airbus', b)
		b226 = re.findall(r'Airbus', b)
		b227 = re.findall(r'AIRBUS', b)
		b228 = re.findall(r'Busdriver', b)
		b229 = re.findall(r'Bus driver', b)
		b230 = re.findall(r'Bus Driver', b)
		b55 = len(b4) + len(b5) + len(b222) + len(b223) + len(b224) + len(b225) + len(b226) + len(b227) + len(b228) + len(b229) + len(b230)
		b6 = int(b3) - int(b55)
		tr1 = re.findall(r'truck', b)
		tr2 = re.findall(r'Truck', b)
		tr3 = re.findall(r'TRUCK', b)
		tr31 = re.findall(r'грузовик', b)
		tr4 = len(tr1) + len(tr2) + len(tr3) + len(tr31)
		by1 = re.findall(r'bicycle', b)
		by2 = re.findall(r'Bicycle', b)
		by3 = re.findall(r'BICYCLE', b)
		by4 = len(by1) + len(by2) + len(by3)
		a1 = re.findall(r'airplane', b)
		a2 = re.findall(r'Airplane', b)
		a3 = re.findall(r'AIRPLANE', b)
		a4 = re.findall(r'airbus', b)
		a5 = re.findall(r'Airbus', b)
		a6 = re.findall(r'AIRBUS', b)
		a7 = len(a1) + len(a2) + len(a3) + len(a4) + len(a5) + len(a6)
		bo1 = re.findall(r'boat', b)
		bo2 = re.findall(r'Boat', b)
		bo3 = re.findall(r'BOAT', b)
		bo31 = re.findall(r'ship', b)
		bo32 = re.findall(r'Ship', b)
		bo33 = re.findall(r'SHIP', b)
		bo4 = len(bo1) + len(bo2) + len(bo3) + len(bo31) + len(bo32) + len(bo33)
		mo1 = re.findall(r'motorcycle', b)
		mo2 = re.findall(r'Motorcycle', b)
		mo3 = re.findall(r'MOTORCYCLE', b)
		mo31 = re.findall(r'motor', b)
		mo32 = re.findall(r'Motor', b)
		mo33 = re.findall(r'MOTOR', b)
		mo4 = len(mo1) + len(mo2) + len(mo3) + len(mo31) + len(mo32) + len(mo33)
		c1 = re.findall(r'car', b)
		c2 = re.findall(r'Car', b)
		c3 = re.findall(r'CAR', b)
		c31 = re.findall(r'автомобиль', b)
		c4 = len(c1) + len(c2) + len(c3) + len(c31)
		if (t3 > b6) and (t3 > tr4) and (t3 > by4) and (t3 > a7) and (t3 > bo4) and (t3 > mo4) and (t3 > c4):
		    print(str(count) + ' This is definitely a train')
		if (b6 > t3) and (b6 > tr4) and (b6 > by4) and (b6 > a7) and (b6 > bo4) and (b6 > mo4) and (b6 > c4):
		    print(str(count) + ' This is definitely a bus')
		if (tr4 > b6) and (tr4 > t3) and (tr4 > by4) and (tr4 > a7) and (tr4 > bo4) and (tr4 > mo4) and (tr4 > c4):
		    print(str(count) + ' This is definitely a truck')
		if (by4 > b6) and (by4 > tr4) and (by4 > t3) and (by4 > a7) and (by4 > bo4) and (by4 > mo4) and (by4 > c4):
		    print(str(count) + ' This is definitely a bicycle')
		if (a7 > b6) and (a7 > tr4) and (a7 > by4) and (a7 > t3) and (a7 > bo4) and (a7 > mo4) and (a7 > c4):
		    print(str(count) + ' This is definitely a airplane')
		if (bo4 > t3) and (bo4 > b6) and (bo4 > tr4) and (bo4 > by4) and (bo4 > a7) and (bo4 > mo4) and (bo4 > c4):
		    print(str(count) + ' This is definitely a boat')
		if (mo4 > t3) and (mo4 > b6) and (mo4 > tr4) and (mo4 > by4) and (mo4 > a7) and (mo4 > bo4) and (mo4 > c4):
		    print(str(count) + ' This is definitely a motorcycle')
		if (c4 > t3) and (c4 > b6) and (c4 > tr4) and (c4 > by4) and (c4 > a7) and (c4 > bo4) and (c4 > mo4):
		    print(str(count) + ' This is definitely a car')
	except (KeyError, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
		hc_solver(filePath, count)
headers = {'Cookie': '__cfduid=d5c7d41b01b423d28af5d265e2b0466fb1611514195; INGRESSCOOKIE=1611514196.272.1171.361267; __cflb=02DiuHLwzyAZNoSCVjn6AYT9Lry6fSzgs3c22MJKBQXYG; hmt_id=aad64ad1-853e-4a4c-bf98-7afe9071ae7e'}
lines2 = []
count = 0
Input_text = input('Please enter your text:\n')
s = Input_text.replace('\t','')
s = s.replace('\n','')
s = s.replace(',}','}')
s = s.replace(',]',']')
data = json.loads(s)
dd = data["tasklist"]
count1 = range(0, len(dd))
for x in count1:
	dd = data["tasklist"]
	d = dd[x]
	d2 = d['datapoint_uri']
	lines2.append(d2)
for a in lines2:
	response = requests.get(a, headers=headers)
	u1 = a.replace('https://imgs.hcaptcha.com/','')
	u1 = u1.replace('/','')
	u1 = u1.replace('//','')
	u1 = u1.replace('\\','')
	u1 = u1.replace('\\\\','')
	file = open(r'E:\adm\nd_newdawn\\' + u1 + '.jpg', "wb")
	file.write(response.content)
file.close()
for a in lines2:
	u1 = a.replace('https://imgs.hcaptcha.com/','')
	u1 = u1.replace('/','')
	filePath1 = u1.replace('\\','')
	filePath1 = filePath1.replace('//','')
	filePath1 = filePath1.replace('\\\\','')
	filePath = filePath1 + '.jpg'
	hc_solver(filePath, count)
	count+=1
