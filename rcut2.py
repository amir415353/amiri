import image_slicer
from colorthief import ColorThief
import time
import multiprocessing
import json
import requests
import re

def cg_y(cg, lines23, lines34, lines45):
	if cg[0] > 120:
		if cg[1] > 98:
			if cg[2] < 80:
				if str(cg[0]) in str(lines23):
					if str(cg[1]) in str(lines34):
						if str(cg[2]) in str(lines45):
							ans = 'yes'
							return ans

def cg_b(cg, lines24, lines35, lines46):
	if cg[0] > 4:
		if cg[1] > 4:
			if cg[2] > 4:
				if str(cg[0]) in str(lines24):
					if str(cg[1]) in str(lines35):
						if str(cg[2]) in str(lines46):
							ans = 'yes'
							return ans
def cg_bl3(cg, lines25, lines36, lines47):
	if cg[0] > 38:
		if cg[1] > 39:
			if cg[2] > 39:
				if str(cg[0]) in str(lines25):
					if str(cg[1]) in str(lines36):
						if str(cg[2]) in str(lines47):
							ans = 'yes'
							return ans

lines1 = []
lines2 = []
lines3 = []
lines4 = []
def rc_solver(filePath, count, lines23, lines34, lines45):
	try:
		proxies = {'http':  'socks5://127.0.0.1:9050',
							   'https': 'socks5://127.0.0.1:9050'}
		searchUrl = 'https://yandex.ru/images/search'
		files = {'upfile': ('blob', open(filePath, 'rb'), 'image/png')}
		params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
		response = requests.post(searchUrl, params=params, files=files, proxies=proxies)
		query_string = json.loads(response.content)['blocks'][0]['params']['url']
		img_search_url= searchUrl + '?' + query_string
		a = requests.get(img_search_url, proxies=proxies)
		b = a.text
		t1 = re.findall(r'train', b)
		t2 = re.findall(r'Train', b)
		t22 = re.findall(r'TRAIN', b)
		t23 = re.findall(r'поезд', b)
		t24 = re.findall(r'трамва', b)
		t25 = re.findall(r'rail', b)
		t26 = re.findall(r'Rail', b)
		t27 = re.findall(r'RAIL', b)
		t33 = len(t1) + len(t2) + len(t22) + len(t23) + len(t24) + len(t25) + len(t26) + len(t27)
		t4 = re.findall(r'Railway', b)
		t5 = re.findall(r'railroad', b)
		t6 = len(t4) + len(t5)
		t3 = int(t33) - int(t6)
		b1 = re.findall(r'bus', b)
		b2 = re.findall(r'Bus', b)
		b22 = re.findall(r'BUS', b)
		b111 = re.findall(r'motorbus', b)
		b112 = re.findall(r'Motorbus', b)
		b113 = re.findall(r'MOTORBUS', b)
		b114 = re.findall(r'автобус', b)
		b3 = len(b1) + len(b2) + len(b22) + len(b111) + len(b112) + len(b113) + len(b114)
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
		b231 = re.findall(r'Busg', b)
		b55 = len(b4) + len(b5) + len(b222) + len(b223) + len(b224) + len(b225) + len(b226) + len(b227) + len(b228) + len(b229) + len(b230) + len(b231)
		b6 = int(b3) - int(b55)
		tr1 = re.findall(r'truck', b)
		tr2 = re.findall(r'Truck', b)
		tr3 = re.findall(r'TRUCK', b)
		tr31 = re.findall(r'грузовик', b)
		tr32 = re.findall(r'пожарной', b)
		tr33 = re.findall(r'Огонь', b)
		tr44 = len(tr1) + len(tr2) + len(tr3) + len(tr31) + len(tr32) + len(tr33)
		tr5 = re.findall(r'itruck', b)
		tr6 = len(tr5)
		tr4 = int(tr44) - int(tr6)
		by1 = re.findall(r'bicycle', b)
		by2 = re.findall(r'Bicycle', b)
		by3 = re.findall(r'BICYCLE', b)
		by31 = re.findall(r'велосипед', b)
		by4 = len(by1) + len(by2) + len(by3) + len(by31)
		a1 = re.findall(r'airplane', b)
		a2 = re.findall(r'Airplane', b)
		a3 = re.findall(r'AIRPLANE', b)
		a4 = re.findall(r'airbus', b)
		a5 = re.findall(r'Airbus', b)
		a6 = re.findall(r'AIRBUS', b)
		a61 = re.findall(r'самолет', b)
		a62 = re.findall(r'аэробус', b)
		a7 = len(a1) + len(a2) + len(a3) + len(a4) + len(a5) + len(a6) + len(a61) + len(a62)
		bo1 = re.findall(r'boat', b)
		bo2 = re.findall(r'Boat', b)
		bo3 = re.findall(r'BOAT', b)
		bo31 = re.findall(r'ship', b)
		bo32 = re.findall(r'Ship', b)
		bo33 = re.findall(r'SHIP', b)
		bo34 = re.findall(r'лодка', b)
		bo4 = len(bo1) + len(bo2) + len(bo3) + len(bo31) + len(bo32) + len(bo33) + len(bo34)
		mo1 = re.findall(r'motorcycle', b)
		mo2 = re.findall(r'Motorcycle', b)
		mo3 = re.findall(r'MOTORCYCLE', b)
		mo31 = re.findall(r'motor', b)
		mo32 = re.findall(r'Motor', b)
		mo33 = re.findall(r'MOTOR', b)
		mo34 = re.findall(r'мотоцикл', b)
		mo35 = re.findall(r'мотор', b)
		mo36 = re.findall(r'Мопеды', b)
		mo4 = len(mo1) + len(mo2) + len(mo3) + len(mo31) + len(mo32) + len(mo33) + len(mo34) + len(mo35) + len(mo36)
		c1 = re.findall(r'car', b)
		c2 = re.findall(r'Car', b)
		c111 = re.findall(r'автомобиль', b)
		c112 = re.findall(r'автомашина', b)
		c112 = re.findall(r'машина', b)
		c113 = re.findall(r'Машина', b)
		c114 = re.findall(r'автомобили', b)
		c115 = re.findall(r'automobile', b)
		c116 = re.findall(r'Automobile', b)
		c117 = re.findall(r'AUTOMOBILE', b)
		c3 = len(c1) + len(c2) + len(c111) + len(c112) + len(c113) + len(c114) + len(c115) + len(c116) + len(c117)
		c41 = re.findall(r'carousel', b)
		c5 = re.findall(r'carry', b)
		c222 = re.findall(r'Carry', b)
		c223 = re.findall(r'CARRY', b)
		c224 = re.findall(r'Carousel', b)
		c225 = re.findall(r'crack', b)
		c226 = re.findall(r'Sky', b)
		c227 = re.findall(r'sky', b)
		c55 = len(c41) + len(c5) + len(c222) + len(c223) + len(c224) + len(c225) + len(c226) + len(c227)
		c6 = int(c3) - int(c55)
		tre1 = re.findall(r'tree', b)
		tre2 = re.findall(r'Tree', b)
		tre3 = re.findall(r'TREE', b)
		tre4 = re.findall(r'дерево', b)
		tre5 = re.findall(r'древо', b)
		tre55 = re.findall(r'Дерево', b)
		tre66 = len(tre1) + len(tre2) + len(tre3) + len(tre4) + len(tre5) + len(tre55)
		tre61 = re.findall(r'street', b)
		tre62 = re.findall(r'Street', b)
		tre63 = re.findall(r'STREET', b)
		tre64 = len(tre61) + len(tre62) + len(tre63)
		tre6 = int(tre66) - int(tre64)
		fi1 = re.findall(r'fire hydrant', b)
		fi2 = re.findall(r'Fire hydrant', b)
		fi3 = re.findall(r'FIRE HYDRANT', b)
		fi4 = re.findall(r'firehydrant', b)
		fi5 = re.findall(r'Firehydrant', b)
		fi6 = re.findall(r'FIREHYDRANT', b)
		fi7 = re.findall(r'пожарный гидрант', b)
		fi77 = re.findall(r'Fire Hydrant', b)
		fi78 = re.findall(r'fire-hydrant', b)
		fi8 = len(fi1) + len(fi2) + len(fi3) + len(fi4) + len(fi5) + len(fi6) + len(fi7) + len(fi77) + len(fi78)
		cr1 = re.findall(r'crosswalk', b)
		cr2 = re.findall(r'Crosswalk', b)
		cr3 = re.findall(r'CROSSWALK', b)
		cr4 = re.findall(r'cross walk', b)
		cr5 = re.findall(r'Cross walk', b)
		cr6 = re.findall(r'пешеходный переход', b)
		cr7 = re.findall(r'пешеходные переход', b)
		cr77 = re.findall(r'Переход', b)
		cr78 = re.findall(r'Пешеходный переход', b)
		cr79 = re.findall(r'Крестовая прогулка', b)
		cr80 = re.findall(r'road Crossing', b)
		cr81 = re.findall(r'Road Crossing', b)
		cr82 = re.findall(r'RoadCrossing', b)
		cr81 = re.findall(r'roadCrossing', b)
		cr82 = re.findall(r'ROADCROSSING', b)
		cr83 = re.findall(r'Cross Walk', b)
		cr84 = re.findall(r'Cross', b)
		cr85 = re.findall(r'cross-', b)
		cr86 = re.findall(r'white line', b)
		cr87 = re.findall(r'White line', b)
		cr88 = re.findall(r'White Line', b)
		cr89 = re.findall(r'white-line', b)
		cr90 = re.findall(r'white arrow', b)
		cr91 = re.findall(r'White arrow', b)
		cr92 = re.findall(r'White Arrow', b)
		cr93 = re.findall(r'white-arrow', b)
		cr94 = re.findall(r'crossing', b)
		cr95 = re.findall(r'Пересекать', b)
		cr8 = len(cr1) + len(cr2) + len(cr3) + len(cr4) + len(cr5) + len(cr6) + len(cr7) + len(cr77) + len(cr78) + len(cr78) + len(cr79) + len(cr80) + len(cr81) + len(cr82) + len(cr83) + len(cr84) + len(cr85) + len(cr86) + len(cr87) + len(cr88) + len(cr89) + len(cr90) + len(cr91) + len(cr92) + len(cr93) + len(cr94) + len(cr95)
		tra1 = re.findall(r'traffic light', b)
		tra2 = re.findall(r'Traffic light', b)
		tra3 = re.findall(r'trafficlight', b)
		tra4 = re.findall(r'Trafficlight', b)
		tra5 = re.findall(r'TRAFFICLIGHT', b)
		tra11 = re.findall(r'traffic signals', b)
		tra12 = re.findall(r'Traffic signals', b)
		tra13 = re.findall(r'trafficsignals', b)
		tra14 = re.findall(r'Trafficsignals', b)
		tra15 = re.findall(r'TRAFFICSIGNALS', b)
		tra16 = re.findall(r'светофор', b)
		tra17 = re.findall(r'трафик', b)
		tra18 = re.findall(r'Трафик', b)
		tra19 = re.findall(r'traffic-', b)
		tra20 = re.findall(r'Traffic-', b)
		tra19 = re.findall(r'traffic_', b)
		tra20 = re.findall(r'Traffic_', b)
		tra21 = re.findall(r'Traffic Signals', b)
		tra22 = re.findall(r'Traffic Light', b)
		tra23 = re.findall(r'power line', b)
		tra24 = re.findall(r'Power line', b)
		tra25 = re.findall(r'Power Line', b)
		tra26 = re.findall(r'power-line', b)
		tra27 = re.findall(r'Power-line', b)
		tra28 = re.findall(r'электропередачи', b)
		tra29 = re.findall(r'overhead line', b)
		tra30 = re.findall(r'Overhead line', b)
		tra31 = re.findall(r'Overhead Line', b)
		tra32 = re.findall(r'overhead-line', b)
		tra33 = re.findall(r'Overhead-line', b)
		tra34 = re.findall(r'Бишкеке', b)
		tra7 = len(tra1) + len(tra2) + len(tra3) + len(tra4) + len(tra5) + len(tra11) + len(tra12) + len(tra13) + len(tra14) + len(tra15) + len(tra16) + len(tra17) + len(tra18) + len(tra19) + len(tra20) + len(tra21) + len(tra22) + len(tra23) + len(tra24) + len(tra25) + len(tra26) + len(tra27) + len(tra28) + len(tra29) + len(tra30) + len(tra31) + len(tra32) + len(tra33) + len(tra34)
		color_thief = ColorThief(filePath)
		palette = color_thief.get_palette(color_count=51)
		for a in range(0, 50):
			ans = cg_y(palette[a], lines23, lines34, lines45)
			lines1.append(ans)
		if 'yes' in str(lines1):
			tra7+=40
		lines1.clear()
		br1 = re.findall(r'bridge', b)
		br2 = re.findall(r'Bridge', b)
		br3 = re.findall(r'BRIDGE', b)
		br4 = re.findall(r'мост', b)
		br5 = re.findall(r'Мост', b)
		br66 = len(br1) + len(br2) + len(br3) + len(br4) + len(br5)
		br61 = re.findall(r'моокупаемост', b)
		br62 = re.findall(r'моста', b)
		br63 = len(br61) + len(br62)
		br6 = int(br66) - int(br63)
		trac1 = re.findall(r'tractor', b)
		trac2 = re.findall(r'Tractor', b)
		trac3 = re.findall(r'TRACTOR', b)
		trac4 = re.findall(r'трактор', b)
		trac5 = re.findall(r'Трактор', b)
		trac6 = len(trac1) + len(trac2) + len(trac3) + len(trac4) + len(trac5)
		if (t3 > b6) and (t3 > tr4) and (t3 > by4) and (t3 > a7) and (t3 > bo4) and (t3 > mo4) and (t3 > c6) and (t3 > tre6) and (t3 > fi8) and (t3 > cr8) and (t3 > tra7) and (t3 > br6) and (t3 > trac6):
			print(str(count) + ' This is definitely a train')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a train')
			f.write("\n")
			f.close()
		if (b6 > t3) and (b6 > tr4) and (b6 > by4) and (b6 > a7) and (b6 > bo4) and (b6 > mo4) and (b6 > c6) and (b6 > tre6) and (b6 > fi8) and (b6 > cr8) and (b6 > tra7) and (b6 > br6) and (b6 > trac6):
			print(str(count) + ' This is definitely a bus')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a bus')
			f.write("\n")
			f.close()
		if (tr4 > b6) and (tr4 > t3) and (tr4 > by4) and (tr4 > a7) and (tr4 > bo4) and (tr4 > mo4) and (tr4 > c6) and (tr4 > tre6) and (tr4 > fi8) and (tr4 > cr8) and (tr4 > tra7) and (tr4 > br6) and (tr4 > trac6):
			print(str(count) + ' This is definitely a truck')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a truck')
			f.write("\n")
			f.close()
		if (by4 > b6) and (by4 > tr4) and (by4 > t3) and (by4 > a7) and (by4 > bo4) and (by4 > mo4) and (by4 > c6) and (by4 > tre6) and (by4 > fi8) and (by4 > cr8) and (by4 > tra7) and (by4 > br6) and (by4 > trac6):
			print(str(count) + ' This is definitely a bicycle')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a bicycle')
			f.write("\n")
			f.close()
		if (a7 > b6) and (a7 > tr4) and (a7 > by4) and (a7 > t3) and (a7 > bo4) and (a7 > mo4) and (a7 > c6) and (a7 > tre6) and (a7 > fi8) and (a7 > cr8) and (a7 > tra7) and (a7 > br6) and (a7 > trac6):
			print(str(count) + ' This is definitely a airplane')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a airplane')
			f.write("\n")
			f.close()
		if (bo4 > t3) and (bo4 > b6) and (bo4 > tr4) and (bo4 > by4) and (bo4 > a7) and (bo4 > mo4) and (bo4 > c6) and (bo4 > tre6) and (bo4 > fi8) and (bo4 > cr8) and (bo4 > tra7) and (bo4 > br6) and (bo4 > trac6):
			print(str(count) + ' This is definitely a boat')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a boat')
			f.write("\n")
			f.close()
		if (mo4 > t3) and (mo4 > b6) and (mo4 > tr4) and (mo4 > by4) and (mo4 > a7) and (mo4 > bo4) and (mo4 > c6) and (mo4 > tre6) and (mo4 > fi8) and (mo4 > cr8) and (mo4 > tra7) and (mo4 > br6) and (mo4 > trac6):
			print(str(count) + ' This is definitely a motorcycle')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a motorcycle')
			f.write("\n")
			f.close()
		if (c6 > t3) and (c6 > b6) and (c6 > tr4) and (c6 > by4) and (c6 > a7) and (c6 > bo4) and (c6 > mo4) and (c6 > tre6) and (c6 > fi8) and (c6 > cr8) and (c6 > tra7) and (c6 > br6) and (c6 > trac6):
			print(str(count) + ' This is definitely a car and a traffic light')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a car and a traffic light')
			f.write("\n")
			f.close()
		if (tre6 > t3) and (tre6 > b6) and (tre6 > tr4) and (tre6 > by4) and (tre6 > a7) and (tre6 > bo4) and (tre6 > mo4) and (tre6 > c6) and (tre6 > fi8) and (tre6 > cr8) and (tre6 > tra7) and (tre6 > br6) and (tre6 > trac6):
			print(str(count) + ' This is definitely a tree')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a tree')
			f.write("\n")
			f.close()
		if (fi8 > t3) and (fi8 > b6) and (fi8 > tr4) and (fi8 > by4) and (fi8 > a7) and (fi8 > bo4) and (fi8 > mo4) and (fi8 > c6) and (fi8 > tre6) and (fi8 > cr8) and (fi8 > tra7) and (fi8 > br6) and (fi8 > trac6):
			print(str(count) + ' This is definitely a fire hydrant')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a fire hydrant')
			f.write("\n")
			f.close()
		if (cr8 > t3) and (cr8 > b6) and (cr8 > tr4) and (cr8 > by4) and (cr8 > a7) and (cr8 > bo4) and (cr8 > mo4) and (cr8 > c6) and (cr8 > tre6) and (cr8 > fi8) and (cr8 > tra7) and (cr8 > br6) and (cr8 > trac6):
			print(str(count) + ' This is definitely a crosswalks')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a crosswalks')
			f.write("\n")
			f.close()
		if (tra7 > t3) and (tra7 > b6) and (tra7 > tr4) and (tra7 > by4) and (tra7 > a7) and (tra7 > bo4) and (tra7 > mo4) and (tra7 > c6) and (tra7 > tre6) and (tra7 > fi8) and (tra7 > cr8) and (tra7 > br6) and (tra7 > trac6):
			print(str(count) + ' This is definitely a traffic light')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a traffic light')
			f.write("\n")
			f.close()
		if (br6 > t3) and (br6 > b6) and (br6 > tr4) and (br6 > by4) and (br6 > a7) and (br6 > bo4) and (br6 > mo4) and (br6 > c6) and (br6 > tre6) and (br6 > fi8) and (br6 > cr8) and (br6 > tra7) and (br6 > trac6):
			print(str(count) + ' This is definitely a bridge')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a bridge')
			f.write("\n")
			f.close()
		if (trac6 > t3) and (trac6 > b6) and (trac6 > tr4) and (trac6 > by4) and (trac6 > a7) and (trac6 > bo4) and (trac6 > mo4) and (trac6 > c6) and (trac6 > tre6) and (trac6 > fi8) and (trac6 > cr8) and (trac6 > tra7) and (trac6 > br6):
			print(str(count) + ' This is definitely a tractor')
			f = open("rc1.txt", "a")
			f.write(str(count) + ' This is definitely a tractor')
			f.write("\n")
			f.close()
		if '<div class="captcha__play-image"></div><div class="captcha__play-text">' in b:
			rc_solver(filePath, count, lines23, lines34, lines45)
	except (KeyError, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ProxyError, json.decoder.JSONDecodeError):
		rc_solver(filePath, count, lines23, lines34, lines45)

def rc_solver2(filePath, count, lines23, lines34, lines45, lines24, lines35, lines46):
	try:
		proxies = {'http':  'socks5://127.0.0.1:9050',
							   'https': 'socks5://127.0.0.1:9050'}
		searchUrl = 'https://yandex.ru/images/search'
		files = {'upfile': ('blob', open(filePath, 'rb'), 'image/png')}
		params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
		response = requests.post(searchUrl, params=params, files=files, proxies=proxies)
		query_string = json.loads(response.content)['blocks'][0]['params']['url']
		img_search_url= searchUrl + '?' + query_string
		a = requests.get(img_search_url, proxies=proxies)
		b = a.text
		t1 = re.findall(r'train', b)
		t2 = re.findall(r'Train', b)
		t22 = re.findall(r'TRAIN', b)
		t23 = re.findall(r'поезд', b)
		t24 = re.findall(r'трамва', b)
		t25 = re.findall(r'rail', b)
		t26 = re.findall(r'Rail', b)
		t27 = re.findall(r'RAIL', b)
		t33 = len(t1) + len(t2) + len(t22) + len(t23) + len(t24) + len(t25) + len(t26) + len(t27)
		t4 = re.findall(r'Railway', b)
		t5 = re.findall(r'railroad', b)
		t6 = len(t4) + len(t5)
		t3 = int(t33) - int(t6)
		b1 = re.findall(r'bus', b)
		b2 = re.findall(r'Bus', b)
		b22 = re.findall(r'BUS', b)
		b111 = re.findall(r'motorbus', b)
		b112 = re.findall(r'Motorbus', b)
		b113 = re.findall(r'MOTORBUS', b)
		b114 = re.findall(r'автобус', b)
		b3 = len(b1) + len(b2) + len(b22) + len(b111) + len(b112) + len(b113) + len(b114)
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
		b231 = re.findall(r'Busg', b)
		b55 = len(b4) + len(b5) + len(b222) + len(b223) + len(b224) + len(b225) + len(b226) + len(b227) + len(b228) + len(b229) + len(b230) + len(b231)
		b6 = int(b3) - int(b55)
		tr1 = re.findall(r'truck', b)
		tr2 = re.findall(r'Truck', b)
		tr3 = re.findall(r'TRUCK', b)
		tr31 = re.findall(r'грузовик', b)
		tr32 = re.findall(r'пожарной', b)
		tr33 = re.findall(r'Огонь', b)
		tr44 = len(tr1) + len(tr2) + len(tr3) + len(tr31) + len(tr32) + len(tr33)
		tr5 = re.findall(r'itruck', b)
		tr6 = len(tr5)
		tr4 = int(tr44) - int(tr6)
		by1 = re.findall(r'bicycle', b)
		by2 = re.findall(r'Bicycle', b)
		by3 = re.findall(r'BICYCLE', b)
		by31 = re.findall(r'велосипед', b)
		by4 = len(by1) + len(by2) + len(by3) + len(by31)
		a1 = re.findall(r'airplane', b)
		a2 = re.findall(r'Airplane', b)
		a3 = re.findall(r'AIRPLANE', b)
		a4 = re.findall(r'airbus', b)
		a5 = re.findall(r'Airbus', b)
		a6 = re.findall(r'AIRBUS', b)
		a61 = re.findall(r'самолет', b)
		a62 = re.findall(r'аэробус', b)
		a7 = len(a1) + len(a2) + len(a3) + len(a4) + len(a5) + len(a6) + len(a61) + len(a62)
		bo1 = re.findall(r'boat', b)
		bo2 = re.findall(r'Boat', b)
		bo3 = re.findall(r'BOAT', b)
		bo31 = re.findall(r'ship', b)
		bo32 = re.findall(r'Ship', b)
		bo33 = re.findall(r'SHIP', b)
		bo34 = re.findall(r'лодка', b)
		bo4 = len(bo1) + len(bo2) + len(bo3) + len(bo31) + len(bo32) + len(bo33) + len(bo34)
		mo1 = re.findall(r'motorcycle', b)
		mo2 = re.findall(r'Motorcycle', b)
		mo3 = re.findall(r'MOTORCYCLE', b)
		mo31 = re.findall(r'motor', b)
		mo32 = re.findall(r'Motor', b)
		mo33 = re.findall(r'MOTOR', b)
		mo34 = re.findall(r'мотоцикл', b)
		mo35 = re.findall(r'мотор', b)
		mo36 = re.findall(r'Мопеды', b)
		mo4 = len(mo1) + len(mo2) + len(mo3) + len(mo31) + len(mo32) + len(mo33) + len(mo34) + len(mo35) + len(mo36)
		c1 = re.findall(r'car', b)
		c2 = re.findall(r'Car', b)
		c111 = re.findall(r'автомобиль', b)
		c112 = re.findall(r'Авто', b)
		c3 = len(c1) + len(c2) + len(c111) + len(c112)
		c41 = re.findall(r'carousel', b)
		c5 = re.findall(r'carry', b)
		c222 = re.findall(r'Carry', b)
		c223 = re.findall(r'CARRY', b)
		c224 = re.findall(r'Carousel', b)
		c225 = re.findall(r'Автошкол', b)
		c226 = re.findall(r'автовладельцев', b)
		c227 = re.findall(r'Авторы', b)
		c228 = re.findall(r'care', b)
		c229 = re.findall(r'Автопрайс', b)
		c55 = len(c41) + len(c5) + len(c222) + len(c223) + len(c224) + len(c225) + len(c226) + len(c227) + len(c228) + len(c229)
		c6 = int(c3) - int(c55)
		tre1 = re.findall(r'tree', b)
		tre2 = re.findall(r'Tree', b)
		tre3 = re.findall(r'TREE', b)
		tre4 = re.findall(r'дерево', b)
		tre5 = re.findall(r'древо', b)
		tre55 = re.findall(r'Дерево', b)
		tre66 = len(tre1) + len(tre2) + len(tre3) + len(tre4) + len(tre5) + len(tre55)
		tre61 = re.findall(r'street', b)
		tre62 = re.findall(r'Street', b)
		tre63 = re.findall(r'STREET', b)
		tre64 = len(tre61) + len(tre62) + len(tre63)
		tre6 = int(tre66) - int(tre64)
		fi1 = re.findall(r'fire hydrant', b)
		fi2 = re.findall(r'Fire hydrant', b)
		fi3 = re.findall(r'FIRE HYDRANT', b)
		fi4 = re.findall(r'firehydrant', b)
		fi5 = re.findall(r'Firehydrant', b)
		fi6 = re.findall(r'FIREHYDRANT', b)
		fi7 = re.findall(r'пожарный гидрант', b)
		fi77 = re.findall(r'Fire Hydrant', b)
		fi78 = re.findall(r'fire-hydrant', b)
		fi8 = len(fi1) + len(fi2) + len(fi3) + len(fi4) + len(fi5) + len(fi6) + len(fi7) + len(fi77) + len(fi78)
		cr1 = re.findall(r'crosswalk', b)
		cr2 = re.findall(r'Crosswalk', b)
		cr3 = re.findall(r'CROSSWALK', b)
		cr4 = re.findall(r'cross walk', b)
		cr5 = re.findall(r'Cross walk', b)
		cr6 = re.findall(r'пешеходный переход', b)
		cr7 = re.findall(r'пешеходные переход', b)
		cr77 = re.findall(r'Переход', b)
		cr78 = re.findall(r'Пешеходный переход', b)
		cr79 = re.findall(r'Крестовая прогулка', b)
		cr80 = re.findall(r'road Crossing', b)
		cr81 = re.findall(r'Road Crossing', b)
		cr82 = re.findall(r'RoadCrossing', b)
		cr81 = re.findall(r'roadCrossing', b)
		cr82 = re.findall(r'ROADCROSSING', b)
		cr83 = re.findall(r'Cross Walk', b)
		cr84 = re.findall(r'Cross', b)
		cr85 = re.findall(r'cross-', b)
		cr86 = re.findall(r'white line', b)
		cr87 = re.findall(r'White line', b)
		cr88 = re.findall(r'White Line', b)
		cr89 = re.findall(r'white-line', b)
		cr90 = re.findall(r'white arrow', b)
		cr91 = re.findall(r'White arrow', b)
		cr92 = re.findall(r'White Arrow', b)
		cr93 = re.findall(r'white-arrow', b)
		cr94 = re.findall(r'crossing', b)
		cr95 = re.findall(r'Пересекать', b)
		cr8 = len(cr1) + len(cr2) + len(cr3) + len(cr4) + len(cr5) + len(cr6) + len(cr7) + len(cr77) + len(cr78) + len(cr78) + len(cr79) + len(cr80) + len(cr81) + len(cr82) + len(cr83) + len(cr84) + len(cr85) + len(cr86) + len(cr87) + len(cr88) + len(cr89) + len(cr90) + len(cr91) + len(cr92) + len(cr93) + len(cr94) + len(cr95)
		tra1 = re.findall(r'traffic light', b)
		tra2 = re.findall(r'Traffic light', b)
		tra3 = re.findall(r'trafficlight', b)
		tra4 = re.findall(r'Trafficlight', b)
		tra5 = re.findall(r'TRAFFICLIGHT', b)
		tra11 = re.findall(r'traffic signals', b)
		tra12 = re.findall(r'Traffic signals', b)
		tra13 = re.findall(r'trafficsignals', b)
		tra14 = re.findall(r'Trafficsignals', b)
		tra15 = re.findall(r'TRAFFICSIGNALS', b)
		tra16 = re.findall(r'светофор', b)
		tra17 = re.findall(r'трафик', b)
		tra18 = re.findall(r'Трафик', b)
		tra19 = re.findall(r'traffic-', b)
		tra20 = re.findall(r'Traffic-', b)
		tra19 = re.findall(r'traffic_', b)
		tra20 = re.findall(r'Traffic_', b)
		tra21 = re.findall(r'Traffic Signals', b)
		tra22 = re.findall(r'Traffic Light', b)
		tra23 = re.findall(r'power line', b)
		tra24 = re.findall(r'Power line', b)
		tra25 = re.findall(r'Power Line', b)
		tra26 = re.findall(r'power-line', b)
		tra27 = re.findall(r'Power-line', b)
		tra28 = re.findall(r'электропередачи', b)
		tra29 = re.findall(r'overhead line', b)
		tra30 = re.findall(r'Overhead line', b)
		tra31 = re.findall(r'Overhead Line', b)
		tra32 = re.findall(r'overhead-line', b)
		tra33 = re.findall(r'Overhead-line', b)
		tra34 = re.findall(r'Бишкеке', b)
		tra7 = len(tra1) + len(tra2) + len(tra3) + len(tra4) + len(tra5) + len(tra11) + len(tra12) + len(tra13) + len(tra14) + len(tra15) + len(tra16) + len(tra17) + len(tra18) + len(tra19) + len(tra20) + len(tra21) + len(tra22) + len(tra23) + len(tra24) + len(tra25) + len(tra26) + len(tra27) + len(tra28) + len(tra29) + len(tra30) + len(tra31) + len(tra32) + len(tra33) + len(tra34)
		color_thief = ColorThief(filePath)
		palette = color_thief.get_palette(color_count=24)
		for a in range(0, 23):
			ans2 = cg_y(palette[a], lines23, lines34, lines45)
			ans3 = cg_b(palette[a], lines24, lines35, lines46)
			lines2.append(ans2)
			lines3.append(ans3)
		if 'yes' in str(lines2):
			tra7+=30
		if 'yes' in str(lines3):
			tra7+=30
		palette = color_thief.get_palette(color_count=34)
		for a in range(0, 33):
			ans4 = cg_bl3(palette[a], lines25, lines36, lines47)
			lines4.append(ans4)
		if 'yes' in str(lines4):
			tra7+=30
		lines2.clear()
		lines3.clear()
		lines4.clear()
		br1 = re.findall(r'bridge', b)
		br2 = re.findall(r'Bridge', b)
		br3 = re.findall(r'BRIDGE', b)
		br4 = re.findall(r'мост', b)
		br5 = re.findall(r'Мост', b)
		br66 = len(br1) + len(br2) + len(br3) + len(br4) + len(br5)
		br61 = re.findall(r'моокупаемост', b)
		br62 = re.findall(r'моста', b)
		br63 = len(br61) + len(br62)
		br6 = int(br66) - int(br63)
		trac1 = re.findall(r'tractor', b)
		trac2 = re.findall(r'Tractor', b)
		trac3 = re.findall(r'TRACTOR', b)
		trac4 = re.findall(r'трактор', b)
		trac5 = re.findall(r'Трактор', b)
		trac6 = len(trac1) + len(trac2) + len(trac3) + len(trac4) + len(trac5)
		if (t3 > b6) and (t3 > tr4) and (t3 > by4) and (t3 > a7) and (t3 > bo4) and (t3 > mo4) and (t3 > c6) and (t3 > tre6) and (t3 > fi8) and (t3 > cr8) and (t3 > tra7) and (t3 > br6) and (t3 > trac6):
			print(str(count) + ' This is definitely a train')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a train')
			f.write("\n")
			f.close()
		if (b6 > t3) and (b6 > tr4) and (b6 > by4) and (b6 > a7) and (b6 > bo4) and (b6 > mo4) and (b6 > c6) and (b6 > tre6) and (b6 > fi8) and (b6 > cr8) and (b6 > tra7) and (b6 > br6) and (b6 > trac6):
			print(str(count) + ' This is definitely a bus')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a bus')
			f.write("\n")
			f.close()
		if (tr4 > b6) and (tr4 > t3) and (tr4 > by4) and (tr4 > a7) and (tr4 > bo4) and (tr4 > mo4) and (tr4 > c6) and (tr4 > tre6) and (tr4 > fi8) and (tr4 > cr8) and (tr4 > tra7) and (tr4 > br6) and (tr4 > trac6):
			print(str(count) + ' This is definitely a truck')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a truck')
			f.write("\n")
			f.close()
		if (by4 > b6) and (by4 > tr4) and (by4 > t3) and (by4 > a7) and (by4 > bo4) and (by4 > mo4) and (by4 > c6) and (by4 > tre6) and (by4 > fi8) and (by4 > cr8) and (by4 > tra7) and (by4 > br6) and (by4 > trac6):
			print(str(count) + ' This is definitely a bicycle')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a bicycle')
			f.write("\n")
			f.close()
		if (a7 > b6) and (a7 > tr4) and (a7 > by4) and (a7 > t3) and (a7 > bo4) and (a7 > mo4) and (a7 > c6) and (a7 > tre6) and (a7 > fi8) and (a7 > cr8) and (a7 > tra7) and (a7 > br6) and (a7 > trac6):
			print(str(count) + ' This is definitely a airplane')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a airplane')
			f.write("\n")
			f.close()
		if (bo4 > t3) and (bo4 > b6) and (bo4 > tr4) and (bo4 > by4) and (bo4 > a7) and (bo4 > mo4) and (bo4 > c6) and (bo4 > tre6) and (bo4 > fi8) and (bo4 > cr8) and (bo4 > tra7) and (bo4 > br6) and (bo4 > trac6):
			print(str(count) + ' This is definitely a boat')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a boat')
			f.write("\n")
			f.close()
		if (mo4 > t3) and (mo4 > b6) and (mo4 > tr4) and (mo4 > by4) and (mo4 > a7) and (mo4 > bo4) and (mo4 > c6) and (mo4 > tre6) and (mo4 > fi8) and (mo4 > cr8) and (mo4 > tra7) and (mo4 > br6) and (mo4 > trac6):
			print(str(count) + ' This is definitely a motorcycle')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a motorcycle')
			f.write("\n")
			f.close()
		if (c6 > t3) and (c6 > b6) and (c6 > tr4) and (c6 > by4) and (c6 > a7) and (c6 > bo4) and (c6 > mo4) and (c6 > tre6) and (c6 > fi8) and (c6 > cr8) and (c6 > tra7) and (c6 > br6) and (c6 > trac6):
			print(str(count) + ' This is definitely a car')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a car')
			f.write("\n")
			f.close()
		if (tre6 > t3) and (tre6 > b6) and (tre6 > tr4) and (tre6 > by4) and (tre6 > a7) and (tre6 > bo4) and (tre6 > mo4) and (tre6 > c6) and (tre6 > fi8) and (tre6 > cr8) and (tre6 > tra7) and (tre6 > br6) and (tre6 > trac6):
			print(str(count) + ' This is definitely a tree')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a tree')
			f.write("\n")
			f.close()
		if (fi8 > t3) and (fi8 > b6) and (fi8 > tr4) and (fi8 > by4) and (fi8 > a7) and (fi8 > bo4) and (fi8 > mo4) and (fi8 > c6) and (fi8 > tre6) and (fi8 > cr8) and (fi8 > tra7) and (fi8 > br6) and (fi8 > trac6):
			print(str(count) + ' This is definitely a fire hydrant')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a fire hydrant')
			f.write("\n")
			f.close()
		if (cr8 > t3) and (cr8 > b6) and (cr8 > tr4) and (cr8 > by4) and (cr8 > a7) and (cr8 > bo4) and (cr8 > mo4) and (cr8 > c6) and (cr8 > tre6) and (cr8 > fi8) and (cr8 > tra7) and (cr8 > br6) and (cr8 > trac6):
			print(str(count) + ' This is definitely a crosswalks')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a crosswalks')
			f.write("\n")
			f.close()
		if (tra7 > t3) and (tra7 > b6) and (tra7 > tr4) and (tra7 > by4) and (tra7 > a7) and (tra7 > bo4) and (tra7 > mo4) and (tra7 > c6) and (tra7 > tre6) and (tra7 > fi8) and (tra7 > cr8) and (tra7 > br6) and (tra7 > trac6):
			print(str(count) + ' This is definitely a traffic light')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a traffic light')
			f.write("\n")
			f.close()
		if (br6 > t3) and (br6 > b6) and (br6 > tr4) and (br6 > by4) and (br6 > a7) and (br6 > bo4) and (br6 > mo4) and (br6 > c6) and (br6 > tre6) and (br6 > fi8) and (br6 > cr8) and (br6 > tra7) and (br6 > trac6):
			print(str(count) + ' This is definitely a bridge')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a bridge')
			f.write("\n")
			f.close()
		if (trac6 > t3) and (trac6 > b6) and (trac6 > tr4) and (trac6 > by4) and (trac6 > a7) and (trac6 > bo4) and (trac6 > mo4) and (trac6 > c6) and (trac6 > tre6) and (trac6 > fi8) and (trac6 > cr8) and (trac6 > tra7) and (trac6 > br6):
			print(str(count) + ' This is definitely a tractor')
			f = open("rcp1.txt", "a")
			f.write(str(count) + ' This is definitely a tractor')
			f.write("\n")
			f.close()
		if '<div class="captcha__play-image"></div><div class="captcha__play-text">' in b:
			rc_solver2(filePath, count, lines23, lines34, lines45, lines24, lines35, lines46)
	except (KeyError, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ProxyError, json.decoder.JSONDecodeError):
		rc_solver2(filePath, count, lines23, lines34, lines45, lines24, lines35, lines46)
infile = 'payload54.jpg'

lines23 = []
lines34 = []
lines45 = []
lines24 = []
lines35 = []
lines46 = []
lines25 = []
lines36 = []
lines47 = []

c4 = range(140, 180)
c5 = range(99 , 110)
c6 = range(15, 80)

for a in c4:
	lines23.append(a)
for a in c5:
	lines34.append(a)
for a in c6:
	lines45.append(a)

c7 = range(13, 20)
c8 = range(5 , 20)
c9 = range(5, 30)

for a in c7:
	lines24.append(a)
for a in c8:
	lines35.append(a)
for a in c9:
	lines46.append(a)

c10 = range(39, 54)
c11 = range(40 , 54)
c12 = range(53, 62)

for a in c10:
    lines25.append(a)
for a in c11:
    lines36.append(a)
for a in c12:
    lines47.append(a)

image_slicer.slice(infile, 4)

infile1 = infile.replace('.jpg', '')
filePath = infile1 + '_01_01.png'
rc_solver(filePath, 0, lines23, lines34, lines45)
filePath = infile1 + '_01_02.png'
rc_solver(filePath, 1, lines23, lines34, lines45)
filePath = infile1 + '_02_01.png'
rc_solver(filePath, 2, lines23, lines34, lines45)
filePath = infile1 + '_02_02.png'
rc_solver(filePath, 3, lines23, lines34, lines45)
input_text = 'traffic'

f = open("rc1.txt", "r")
a2 = f.read()

with open('rc1.txt') as f1:
	a1 = f1.readlines()
	if input_text in a2:
		image_slicer.slice(infile, 16)
		for a in a1:
			if input_text and '0' in a:
				if input_text in a:
					infile1 = infile.replace('.jpg', '')
					filePath = infile1 + '_01_01.png'
					rc_solver2(filePath, 0, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_01_02.png'
					rc_solver2(filePath, 1, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_02_01.png'
					rc_solver2(filePath, 4, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_02_02.png'
					rc_solver2(filePath, 5, lines23, lines34, lines45, lines24, lines35, lines46)
			if input_text and '1' in a:
				if input_text in a:
					infile1 = infile.replace('.jpg', '')
					filePath = infile1 + '_01_03.png'
					rc_solver2(filePath, 2, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_01_04.png'
					rc_solver2(filePath, 3, lines23, lines34, lines45, lines24, lines35, lines46)
					infile1 = infile.replace('.jpg', '')
					filePath = infile1 + '_02_03.png'
					rc_solver2(filePath, 6, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_02_04.png'
					rc_solver2(filePath, 7, lines23, lines34, lines45, lines24, lines35, lines46)
			if input_text and '2' in a:
				if input_text in a:
					infile1 = infile.replace('.jpg', '')
					filePath = infile1 + '_03_01.png'
					rc_solver2(filePath, 8, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_03_02.png'
					rc_solver2(filePath, 9, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_04_01.png'
					rc_solver2(filePath, 12, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_04_02.png'
					rc_solver2(filePath, 13, lines23, lines34, lines45, lines24, lines35, lines46)
			if input_text and '3' in a:
				if input_text in a:
					infile1 = infile.replace('.jpg', '')
					filePath = infile1 + '_03_03.png'
					rc_solver2(filePath, 10, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_03_04.png'
					rc_solver2(filePath, 11, lines23, lines34, lines45, lines24, lines35, lines46)
					infile1 = infile.replace('.jpg', '')
					filePath = infile1 + '_04_03.png'
					rc_solver2(filePath, 14, lines23, lines34, lines45, lines24, lines35, lines46)
					filePath = infile1 + '_04_04.png'
					rc_solver2(filePath, 15, lines23, lines34, lines45, lines24, lines35, lines46)
	elif input_text not in a2:
		image_slicer.slice(infile, 2)
		infile1 = infile.replace('.jpg', '')
		filePath = infile1 + '_01_01.png'
		rc_solver2(filePath, 0, lines23, lines34, lines45, lines24, lines35, lines46)
		filePath = infile1 + '_01_02.png'
		rc_solver2(filePath, 1, lines23, lines34, lines45, lines24, lines35, lines46)
