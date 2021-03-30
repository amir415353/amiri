import image_slicer
from colorthief import ColorThief
import time
import multiprocessing
import json
import requests
import re

test_list = []
lines_s = []
lines_s2 = []
lines_s4 = []
lines_s_h = []
lines_s_h2 = []
lines_ss = []
count11 = 0

lines4 = []
lines5 = []
lines6 = []
lines7 = []
lines8 = []
lines9 = []
lines10 = []
lines11 = []

def cg_b(cg, lines1, lines2, lines3):
	if cg[0] > 100:
		if cg[1] > 89:
			if str(cg[0]) in str(lines1):
				if str(cg[1]) in str(lines2):
					if str(cg[2]) in str(lines3):
						ans = 'yes'
						return ans
def cg_o(cg, lines22, lines33, lines44):
	if cg[0] > 100:
		if cg[1] > 69:
			if cg[2] < 70:
				if str(cg[0]) in str(lines22):
					if str(cg[1]) in str(lines33):
						if str(cg[2]) in str(lines44):
							ans = 'yes'
							return ans

def cg_b2(cg, lines25, lines36, lines47):
	if cg[0] > 37:
		if cg[1] > 39:
			if cg[2] > 47:
				if str(cg[0]) in str(lines25):
					if str(cg[1]) in str(lines36):
						if str(cg[2]) in str(lines47):
							ans = 'yes'
							return ans

def rc_solver(filePath, count):
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
		color_thief = ColorThief(filePath)
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
		b111 = re.findall(r'motorbus', b)
		b112 = re.findall(r'Motorbus', b)
		b113 = re.findall(r'MOTORBUS', b)
		b114 = re.findall(r'автобус', b)
		b3 = len(b1) + len(b2) + len(b111) + len(b112) + len(b113) + len(b114)
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
		b232 = re.findall(r'abus', b)
		b55 = len(b4) + len(b5) + len(b222) + len(b223) + len(b224) + len(b225) + len(b226) + len(b227) + len(b228) + len(b229) + len(b230) + len(b231) + len(b232)
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
		bo35 = re.findall(r'Лодка', b)
		bo4 = len(bo1) + len(bo2) + len(bo3) + len(bo31) + len(bo32) + len(bo33) + len(bo34) + len(bo35)
		mo1 = re.findall(r'motorcycle', b)
		mo2 = re.findall(r'Motorcycle', b)
		mo3 = re.findall(r'MOTORCYCLE', b)
		mo31 = re.findall(r'motor', b)
		mo32 = re.findall(r'Motor', b)
		mo33 = re.findall(r'MOTOR', b)
		mo34 = re.findall(r'мотоцикл', b)
		mo35 = re.findall(r'мотор', b)
		mo36 = re.findall(r'Мопеды', b)
		mo44 = len(mo1) + len(mo2) + len(mo3) + len(mo31) + len(mo32) + len(mo33) + len(mo34) + len(mo35) + len(mo36)
		mo41 = re.findall(r'lomotor', b)
		mo5 = len(mo41)
		mo4 = int(mo44) - int(mo5)
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
		c5 = re.findall(r'carr', b)
		c222 = re.findall(r'Carry', b)
		c223 = re.findall(r'CARRY', b)
		c224 = re.findall(r'Carousel', b)
		c225 = re.findall(r'card', b)
		c55 = len(c41) + len(c5) + len(c222) + len(c223) + len(c224) + len(c225)
		c6 = int(c3) - int(c55)
		palette = color_thief.get_palette(color_count=14)
		for a in range(0, 13):
			ans5 = cg_b2(palette[a], lines25, lines36, lines47)
			lines9.append(ans5)
		if 'yes' in str(lines9):
			c6+=30
		lines9.clear()
		tre1 = re.findall(r'tree', b)
		tre2 = re.findall(r'Tree', b)
		tre3 = re.findall(r'TREE', b)
		tre4 = re.findall(r'дерево', b)
		tre5 = re.findall(r'древо', b)
		tre55 = re.findall(r'Дерево', b)
		tre56 = re.findall(r'Кедр', b)
		tre57 = re.findall(r'plant', b)
		tre58 = re.findall(r'Plant', b)
		tre59 = re.findall(r'природ', b)
		tre60 = re.findall(r'Природ', b)
		tre61 = re.findall(r'paddy field', b)
		tre62 = re.findall(r'Paddy field', b)
		tre63 = re.findall(r'Paddy Field', b)
		tre64 = re.findall(r'paddy-field', b)
		tre65 = re.findall(r'Paddy-field', b)
		tre661 = re.findall(r'рисовое поле', b)
		tre662 = re.findall(r'рисовые поля', b)
		tre663 = re.findall(r'linden', b)
		tre664 = re.findall(r'Linden', b)
		tre665 = re.findall(r'липа', b)
		tre666 = re.findall(r'липы', b)
		tre667 = re.findall(r'Липа', b)
		tre668 = re.findall(r'Липовые деревья', b)
		tre66 = len(tre1) + len(tre2) + len(tre3) + len(tre4) + len(tre5) + len(tre55) + len(tre55) + len(tre56) + len(tre57) + len(tre58) + len(tre59) + len(tre60) + len(tre61) + len(tre62) + len(tre63) + len(tre64) + len(tre65) + len(tre661) + len(tre662) + len(tre663) + len(tre664) + len(tre665) + len(tre666) + len(tre667) + len(tre668)
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
		fi77 = re.findall(r'dog', b)
		fi78 = re.findall(r'Dog', b)
		fi79 = re.findall(r'собака', b)
		fi80 = re.findall(r'Собака', b)
		fi81 = re.findall(r'собачка', b)
		fi82 = re.findall(r'Собачка', b)
		fi83 = re.findall(r'firefight', b)
		fi84 = re.findall(r'Firefight', b)
		fi85 = re.findall(r'FIREFIGHT', b)
		fi86 = re.findall(r'fire-fight', b)
		fi87 = re.findall(r'Fire-fight', b)
		fi88 = re.findall(r'FIRE-FIGHT', b)
		fi89 = re.findall(r'fire_fight', b)
		fi90 = re.findall(r'Fire_fight', b)
		fi91 = re.findall(r'FIRE_FIGHT', b)
		fi8881 = len(fi1) + len(fi2) + len(fi3) + len(fi4) + len(fi5) + len(fi6) + len(fi7) + len(fi77) + len(fi78) + len(fi79) + len(fi80) + len(fi81) + len(fi82) + len(fi83) + len(fi84) + len(fi85) + len(fi86) + len(fi87) + len(fi88) + len(fi89) + len(fi90) + len(fi91)
		fi881 = re.findall(r'fired', b)
		fi891 = len(fi881)
		fi8 = int(fi8881) - int(fi891)
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
		cr80 = re.findall(r'crossing', b)
		cr81 = re.findall(r'Crossing', b)
		cr82 = re.findall(r'CROSSING', b)
		cr83 = re.findall(r'Cross Walk', b)
		cr84 = re.findall(r'cross-', b)
		cr85 = re.findall(r'white line', b)
		cr86 = re.findall(r'White line', b)
		cr87 = re.findall(r'White Line', b)
		cr88 = re.findall(r'white-line', b)
		cr89 = re.findall(r'white arrow', b)
		cr90 = re.findall(r'White arrow', b)
		cr91 = re.findall(r'White Arrow', b)
		cr92 = re.findall(r'white-arrow', b)
		cr93 = re.findall(r'Пересекать', b)
		cr94 = re.findall(r'разметка на дороге', b)
		cr95 = re.findall(r'road clown', b)
		cr96 = re.findall(r'Road clown', b)
		cr97 = re.findall(r'Road Clown', b)
		cr98 = re.findall(r'ROAD CLOWN', b)
		cr99 = re.findall(r'road-clown', b)
		cr100 = re.findall(r'Road-clown', b)
		cr101 = re.findall(r'Road-Clown', b)
		cr102 = re.findall(r'ROAD-CLOWN', b)
		cr103 = re.findall(r'road_clown', b)
		cr104 = re.findall(r'Road_clown', b)
		cr105 = re.findall(r'Road Clown', b)
		cr106 = re.findall(r'ROAD_CLOWN', b)
		cr107 = re.findall(r'roadclown', b)
		cr108 = re.findall(r'Roadclown', b)
		cr109 = re.findall(r'RoadClown', b)
		cr110 = re.findall(r'ROADCLOWN', b)
		cr111 = re.findall(r'road race', b)
		cr112 = re.findall(r'Road race', b)
		cr113 = re.findall(r'Road Race', b)
		cr114 = re.findall(r'ROAD RACE', b)
		cr115 = re.findall(r'road-race', b)
		cr116 = re.findall(r'Road-race', b)
		cr117 = re.findall(r'Road-Race', b)
		cr118 = re.findall(r'ROAD-RACE', b)
		cr119 = re.findall(r'road_race', b)
		cr120 = re.findall(r'Road_race', b)
		cr121 = re.findall(r'Road Race', b)
		cr122 = re.findall(r'ROAD_RACE', b)
		cr123 = re.findall(r'roadrace', b)
		cr124 = re.findall(r'Roadrace', b)
		cr125 = re.findall(r'RoadRace', b)
		cr126 = re.findall(r'ROADRACE', b)
		cr8 = len(cr1) + len(cr2) + len(cr3) + len(cr4) + len(cr5) + len(cr6) + len(cr7) + len(cr77) + len(cr78) + len(cr78) + len(cr79) + len(cr80) + len(cr81) + len(cr82) + len(cr83) + len(cr84) + len(cr85) + len(cr86) + len(cr87) + len(cr88) + len(cr89) + len(cr90) + len(cr91) + len(cr92) + len(cr93) + len(cr94) + len(cr95) + len(cr96) + len(cr97) + len(cr98) + len(cr99) + len(cr100) + len(cr101) + len(cr102) + len(cr103) + len(cr104) + len(cr105) + len(cr106) + len(cr107) + len(cr108) + len(cr109) + len(cr110) + len(cr111) + len(cr112) + len(cr113) + len(cr114) + len(cr115) + len(cr116) + len(cr117) + len(cr118) + len(cr119) + len(cr120) + len(cr121) + len(cr122) + len(cr123) + len(cr124) + len(cr125) + len(cr126)
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
		tra7 = len(tra1) + len(tra2) + len(tra3) + len(tra4) + len(tra5) + len(tra11) + len(tra12) + len(tra13) + len(tra14) + len(tra15) + len(tra16) + len(tra17) + len(tra18) + len(tra19) + len(tra20) + len(tra21) + len(tra22)
		br1 = re.findall(r'bridge', b)
		br2 = re.findall(r'Bridge', b)
		br3 = re.findall(r'BRIDGE', b)
		br4 = re.findall(r'мост', b)
		br5 = re.findall(r'Мост', b)
		br66 = len(br1) + len(br2) + len(br3) + len(br4) + len(br5)
		br61 = re.findall(r'моокупаемост', b)
		br62 = re.findall(r'моста', b)
		br621 = re.findall(r'недвижимост', b)
		br63 = len(br61) + len(br62) + len(br621)
		br6 = int(br66) - int(br63)
		trac1 = re.findall(r'tractor', b)
		trac2 = re.findall(r'Tractor', b)
		trac3 = re.findall(r'TRACTOR', b)
		trac4 = re.findall(r'трактор', b)
		trac5 = re.findall(r'Трактор', b)
		trac6 = len(trac1) + len(trac2) + len(trac3) + len(trac4) + len(trac5)
		ta1 = re.findall(r'taxis', b)
		ta2 = re.findall(r'Taxis', b)
		ta22 = re.findall(r'TAXIS', b)
		ta23 = re.findall(r'такси', b)
		ta24 = re.findall(r'Таксис', b)
		ta25 = re.findall(r'nissan nv200', b)
		ta26 = re.findall(r'Nissan nv200', b)
		ta27 = re.findall(r'Nissan NV200', b)
		ta28 = re.findall(r'car', b)
		ta29 = re.findall(r'Car', b)
		ta333 = len(ta1) + len(ta2) + len(ta22) + len(ta23) + len(ta24) + len(ta25) + len(ta26) + len(ta27) + len(ta28) + len(ta29)
		ta441 = re.findall(r'carousel', b)
		ta442 = re.findall(r'carry', b)
		ta443 = re.findall(r'Carry', b)
		ta444 = re.findall(r'CARRY', b)
		ta445 = re.findall(r'Carousel', b)
		ta446 = re.findall(r'card', b)
		ta447 = re.findall(r'carret', b)
		ta4444 = len(ta441) + len(ta442) + len(ta443) + len(ta444) + len(ta445) + len(ta446) + len(ta447)
		ta3 = int(ta333) - int(ta4444)
		st1 = re.findall(r'stair', b)
		st2 = re.findall(r'Stair', b)
		st22 = re.findall(r'STAIR', b)
		st23 = re.findall(r'лестница', b)
		st24 = re.findall(r'Лестница', b)
		st25 = re.findall(r'лестница', b)
		st26 = re.findall(r'deck', b)
		st27 = re.findall(r'Deck', b)
		st28 = re.findall(r'DECK', b)
		st29 = re.findall(r'палуба', b)
		st30 = re.findall(r'Палуба', b)
		st31 = re.findall(r'недвижимость', b)
		st32 = re.findall(r'Недвижимость', b)
		st3 = len(st1) + len(st2) + len(st22) + len(st23) + len(st24) + len(st25) + len(st26) + len(st27) + len(st28) + len(st29) + len(st30) + len(st31) + len(st32)
		ch1 = re.findall(r'chimney', b)
		ch2 = re.findall(r'Chimney', b)
		ch22 = re.findall(r'CHIMNEY', b)
		ch23 = re.findall(r'дымовая труба', b)
		ch24 = re.findall(r'Дымовая труба', b)
		ch25 = re.findall(r'дымоходы', b)
		ch26 = re.findall(r'Дымоходы', b)
		ch27 = re.findall(r'roof', b)
		ch28 = re.findall(r'Roof', b)
		ch29 = re.findall(r'крыша', b)
		ch30 = re.findall(r'Крыша', b)
		ch31 = re.findall(r'недвижимость', b)
		ch32 = re.findall(r'Недвижимость', b)
		ch33 = re.findall(r'дома', b)
		ch34 = re.findall(r'Дома', b)
		ch3 = len(ch1) + len(ch2) + len(ch22) + len(ch23) + len(ch24) + len(ch25) + len(ch26) + len(ch27) + len(ch28) + len(ch29) + len(ch30) + len(ch31) + len(ch32) + len(ch33) + len(ch34)
		hi3 = 0
		pa1 = re.findall(r'parking meter', b)
		pa2 = re.findall(r'Parking meter', b)
		pa22 = re.findall(r'Parking Meter', b)
		pa23 = re.findall(r'PARKING METER', b)
		pa24 = re.findall(r'parkingmeter', b)
		pa25 = re.findall(r'Parkingmeter', b)
		pa26 = re.findall(r'PARKINGMETER', b)
		pa27 = re.findall(r'parking-meter', b)
		pa28 = re.findall(r'parking_meter', b)
		pa29 = re.findall(r'Parking-meter', b)
		pa30 = re.findall(r'Parking_meter', b)
		pa31 = re.findall(r'Parking-Meter', b)
		pa32 = re.findall(r'Parking_Meter', b)
		pa33 = re.findall(r'PARKING-METER', b)
		pa34 = re.findall(r'PARKING_METER', b)
		pa35 = re.findall(r'счетчик на стоянке', b)
		pa36 = re.findall(r'Счетчик на стоянке', b)
		pa37 = re.findall(r'паркоматы', b)
		pa38 = re.findall(r'Паркоматы', b)
		pa39 = re.findall(r'Парковочные счетчики', b)
		pa3 = len(pa1) + len(pa2) + len(pa22) + len(pa23) + len(pa24) + len(pa25) + len(pa26) + len(pa27) + len(pa28) + len(pa29) + len(pa30) + len(pa31) + len(pa32) + len(pa33) + len(pa34) + len(pa35) + len(pa36) + len(pa37) + len(pa38) + len(pa39)
		if (t3 > b6) and (t3 > tr4) and (t3 > by4) and (t3 > a7) and (t3 > bo4) and (t3 > mo4) and (t3 > c6) and (t3 > tre6) and (t3 > fi8) and (t3 > cr8) and (t3 > tra7) and (t3 > br6) and (t3 > trac6) and (t3 > ta3) and (t3 > st3) and (t3 > ch3) and (t3 > hi3) and (t3 > pa3):
			print(str(count) + ' This is definitely a train')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a train')
			f.write("\n")
			f.close()
		if (b6 > t3) and (b6 > tr4) and (b6 > by4) and (b6 > a7) and (b6 > bo4) and (b6 > mo4) and (b6 > c6) and (b6 > tre6) and (b6 > fi8) and (b6 > cr8) and (b6 > tra7) and (b6 > br6) and (b6 > trac6) and (b6 > ta3) and (b6 > st3) and (b6 > ch3) and (b6 > hi3) and (b6 > pa3):
			palette = color_thief.get_palette(color_count=34)
			for a in range(0, 33):
				ans = cg_b(palette[a], lines1, lines2, lines3)
				lines5.append(ans)
			if 'yes' in str(lines5):
				print(str(count) + ' This is definitely a taxis')
				f = open("r1.txt", "a")
				f.write(str(count) + ' This is definitely a taxis')
				f.write("\n")
				f.close()
			elif 'yes' not in str(lines5):
				print(str(count) + ' This is definitely a bus')
				f = open("r1.txt", "a")
				f.write(str(count) + ' This is definitely a bus')
				f.write("\n")
				f.close()
			lines5.clear()
		if (tr4 > b6) and (tr4 > t3) and (tr4 > by4) and (tr4 > a7) and (tr4 > bo4) and (tr4 > mo4) and (tr4 > c6) and (tr4 > tre6) and (tr4 > fi8) and (tr4 > cr8) and (tr4 > tra7) and (tr4 > br6) and (tr4 > trac6) and (tr4 > ta3) and (tr4 > st3) and (tr4 > ch3) and (tr4 > hi3) and (tr4 > pa3):
			print(str(count) + ' This is definitely a truck')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a truck')
			f.write("\n")
			f.close()
		if (by4 > b6) and (by4 > tr4) and (by4 > t3) and (by4 > a7) and (by4 > bo4) and (by4 > mo4) and (by4 > c6) and (by4 > tre6) and (by4 > fi8) and (by4 > cr8) and (by4 > tra7) and (by4 > br6) and (by4 > trac6) and (by4 > ta3) and (by4 > st3) and (by4 > ch3) and (by4 > hi3) and (by4 > pa3):
			print(str(count) + ' This is definitely a bicycles')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a bicycles')
			f.write("\n")
			f.close()
		if (a7 > b6) and (a7 > tr4) and (a7 > by4) and (a7 > t3) and (a7 > bo4) and (a7 > mo4) and (a7 > c6) and (a7 > tre6) and (a7 > fi8) and (a7 > cr8) and (a7 > tra7) and (a7 > br6) and (a7 > trac6) and (a7 > ta3) and (a7 > st3) and (a7 > ch3) and (a7 > hi3) and (a7 > pa3):
			print(str(count) + ' This is definitely a airplane')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a airplane')
			f.write("\n")
			f.close()
		if (bo4 > t3) and (bo4 > b6) and (bo4 > tr4) and (bo4 > by4) and (bo4 > a7) and (bo4 > mo4) and (bo4 > c6) and (bo4 > tre6) and (bo4 > fi8) and (bo4 > cr8) and (bo4 > tra7) and (bo4 > br6) and (bo4 > trac6) and (bo4 > ta3) and (bo4 > st3) and (bo4 > ch3) and (bo4 > hi3) and (bo4 > pa3):
			print(str(count) + ' This is definitely a boat')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a boat')
			f.write("\n")
			f.close()
		if (mo4 > t3) and (mo4 > b6) and (mo4 > tr4) and (mo4 > by4) and (mo4 > a7) and (mo4 > bo4) and (mo4 > c6) and (mo4 > tre6) and (mo4 > fi8) and (mo4 > cr8) and (mo4 > tra7) and (mo4 > br6) and (mo4 > trac6) and (mo4 > ta3) and (mo4 > st3) and (mo4 > ch3) and (mo4 > hi3) and (mo4 > pa3):
			print(str(count) + ' This is definitely a motorcycle')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a motorcycle')
			f.write("\n")
			f.close()
		if (c6 > t3) and (c6 > b6) and (c6 > tr4) and (c6 > by4) and (c6 > a7) and (c6 > bo4) and (c6 > mo4) and (c6 > tre6) and (c6 > fi8) and (c6 > cr8) and (c6 > tra7) and (c6 > br6) and (c6 > trac6) and (c6 > ta3) and (c6 > st3) and (c6 > ch3) and (c6 > hi3) and (c6 > pa3):
			palette = color_thief.get_palette(color_count=34)
			for a in range(0, 33):
				ans2 = cg_o(palette[a], lines22, lines33, lines44)
				lines6.append(ans2)
			if 'yes' in str(lines6):
				print(str(count) + ' This is definitely a bus')
				f = open("r1.txt", "a")
				f.write(str(count) + ' This is definitely a bus')
				f.write("\n")
				f.close()
			elif 'yes' not in str(lines6):
				print(str(count) + ' This is definitely a car')
				f = open("r1.txt", "a")
				f.write(str(count) + ' This is definitely a car')
				f.write("\n")
				f.close()
			lines6.clear()
		if (tre6 > t3) and (tre6 > b6) and (tre6 > tr4) and (tre6 > by4) and (tre6 > a7) and (tre6 > bo4) and (tre6 > mo4) and (tre6 > c6) and (tre6 > fi8) and (tre6 > cr8) and (tre6 > tra7) and (tre6 > br6) and (tre6 > trac6) and (tre6 > ta3) and (tre6 > st3) and (tre6 > ch3) and (tre6 > hi3) and (tre6 > pa3):
			print(str(count) + ' This is definitely a tree')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a tree')
			f.write("\n")
			f.close()
		if (fi8 > t3) and (fi8 > b6) and (fi8 > tr4) and (fi8 > by4) and (fi8 > a7) and (fi8 > bo4) and (fi8 > mo4) and (fi8 > c6) and (fi8 > tre6) and (fi8 > cr8) and (fi8 > tra7) and (fi8 > br6) and (fi8 > trac6) and (fi8 > ta3) and (fi8 > st3) and (fi8 > ch3) and (fi8 > hi3) and (fi8 > pa3):
			print(str(count) + ' This is definitely a fire hydrant')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a fire hydrant')
			f.write("\n")
			f.close()
		if (cr8 > t3) and (cr8 > b6) and (cr8 > tr4) and (cr8 > by4) and (cr8 > a7) and (cr8 > bo4) and (cr8 > mo4) and (cr8 > c6) and (cr8 > tre6) and (cr8 > fi8) and (cr8 > tra7) and (cr8 > br6) and (cr8 > trac6) and (cr8 > ta3) and (cr8 > st3) and (cr8 > ch3) and (cr8 > hi3) and (cr8 > pa3):
			print(str(count) + ' This is definitely a crosswalks')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a crosswalks')
			f.write("\n")
			f.close()
		if (tra7 > t3) and (tra7 > b6) and (tra7 > tr4) and (tra7 > by4) and (tra7 > a7) and (tra7 > bo4) and (tra7 > mo4) and (tra7 > c6) and (tra7 > tre6) and (tra7 > fi8) and (tra7 > cr8) and (tra7 > br6) and (tra7 > trac6) and (tra7 > ta3) and (tra7 > st3) and (tra7 > ch3) and (tra7 > hi3 and (tra7 > pa3)):
			print(str(count) + ' This is definitely a traffic light')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a traffic light')
			f.write("\n")
			f.close()
		if (br6 > t3) and (br6 > b6) and (br6 > tr4) and (br6 > by4) and (br6 > a7) and (br6 > bo4) and (br6 > mo4) and (br6 > c6) and (br6 > tre6) and (br6 > fi8) and (br6 > cr8) and (br6 > tra7) and (br6 > trac6) and (br6 > ta3) and (br6 > st3) and (br6 > ch3) and (br6 > hi3) and (br6 > pa3):
			print(str(count) + ' This is definitely a bridges')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a bridges')
			f.write("\n")
			f.close()
		if (trac6 > t3) and (trac6 > b6) and (trac6 > tr4) and (trac6 > by4) and (trac6 > a7) and (trac6 > bo4) and (trac6 > mo4) and (trac6 > c6) and (trac6 > tre6) and (trac6 > fi8) and (trac6 > cr8) and (trac6 > tra7) and (trac6 > br6) and (trac6 > ta3) and (trac6 > st3) and (trac6 > ch3) and (trac6 > hi3) and (trac6 > pa3):
			print(str(count) + ' This is definitely a tractors')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a tractors')
			f.write("\n")
			f.close()
		if (ta3 > t3) and (ta3 > b6) and (ta3 > tr4) and (ta3 > by4) and (ta3 > a7) and (ta3 > bo4) and (ta3 > mo4) and (ta3 > c6) and (ta3 > tre6) and (ta3 > fi8) and (ta3 > cr8) and (ta3 > tra7) and (ta3 > br6) and (ta3 > trac6) and (ta3 > st3) and (ta3 > ch3) and (ta3 > hi3) and (ta3 > pa3):
			palette = color_thief.get_palette(color_count=34)
			for a in range(0, 33):
				ans = cg_b(palette[a], lines1, lines2, lines3)
				ans2 = cg_o(palette[a], lines22, lines33, lines44)
				lines4.append(ans)
				lines6.append(ans2)
			if 'yes' in str(lines4):
				print(str(count) + ' This is definitely a taxis')
				f = open("r1.txt", "a")
				f.write(str(count) + ' This is definitely a taxis')
				f.write("\n")
				f.close()
			elif 'yes' not in str(lines4):
				if 'yes' in str(lines6):
					print(str(count) + ' This is definitely a bus')
					f = open("r1.txt", "a")
					f.write(str(count) + ' This is definitely a bus')
					f.write("\n")
					f.close()
				if 'yes' not in str(lines6):
					print(str(count) + ' This is definitely a car')
					f = open("r1.txt", "a")
					f.write(str(count) + ' This is definitely a car')
					f.write("\n")
					f.close()
			lines4.clear()
			lines6.clear()
		if (st3 > t3) and (st3 > b6) and (st3 > tr4) and (st3 > by4) and (st3 > a7) and (st3 > bo4) and (st3 > mo4) and (st3 > c6) and (st3 > tre6) and (st3 > fi8) and (st3 > cr8) and (st3 > tra7) and (st3 > br6) and (st3 > trac6) and (st3 > ta3) and (st3 > ch3) and (st3 > hi3) and (st3 > pa3):
			print(str(count) + ' This is definitely a stairs')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a stairs')
			f.write("\n")
			f.close()
		if (ch3 > t3) and (ch3 > b6) and (ch3 > tr4) and (ch3 > by4) and (ch3 > a7) and (ch3 > bo4) and (ch3 > mo4) and (ch3 > c6) and (ch3 > tre6) and (ch3 > fi8) and (ch3 > cr8) and (ch3 > tra7) and (ch3 > br6) and (ch3 > trac6) and (ch3 > ta3) and (ch3 > st3) and (ch3 > hi3) and (ch3 > pa3):
			print(str(count) + ' This is definitely a chimney')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a chimney')
			f.write("\n")
			f.close()
		if (hi3 > t3) and (hi3 > b6) and (hi3 > tr4) and (hi3 > by4) and (hi3 > a7) and (hi3 > bo4) and (hi3 > mo4) and (hi3 > c6) and (hi3 > tre6) and (hi3 > fi8) and (hi3 > cr8) and (hi3 > tra7) and (hi3 > br6) and (hi3 > trac6) and (hi3 > ta3) and (hi3 > st3) and (hi3 > ch3) and (hi3 > pa3):
			print(str(count) + ' This is definitely a mountains or hills')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a mountains or hills')
			f.write("\n")
			f.close()
		if (pa3 > t3) and (pa3 > b6) and (pa3 > tr4) and (pa3 > by4) and (pa3 > a7) and (pa3 > bo4) and (pa3 > mo4) and (pa3 > c6) and (pa3 > tre6) and (pa3 > fi8) and (pa3 > cr8) and (pa3 > tra7) and (pa3 > br6) and (pa3 > trac6) and (pa3 > ta3) and (pa3 > st3) and (pa3 > ch3) and (pa3 > hi3):
			print(str(count) + ' This is definitely a parking meters')
			f = open("r1.txt", "a")
			f.write(str(count) + ' This is definitely a parking meters')
			f.write("\n")
			f.close()
		if '<div class="captcha__play-image"></div><div class="captcha__play-text">' in b:
			rc_solver(filePath, count)
		test_list.append((count, t3, b6, tr4, by4, a7, bo4, mo4, c6, tre6, fi8, cr8, tra7, br6, trac6, ta3, st3, ch3, hi3, pa3))
	except (KeyError, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ProxyError, json.decoder.JSONDecodeError):
		rc_solver(filePath, count)


lines1 = []
lines2 = []
lines3 = []

lines22 = []
lines33 = []
lines44 = []

lines25 = []
lines36 = []
lines47 = []

c1 = range(142, 192)
c2 = range(90 , 148)
c3 = range(0, 70)

for a in c1:
	lines1.append(a)
for a in c2:
	lines2.append(a)
for a in c3:
	lines3.append(a)

c4 = range(145, 231)
c5 = range(70 , 102)
c6 = range(0, 70)

for a in c4:
	lines22.append(a)
for a in c5:
	lines33.append(a)
for a in c6:
	lines44.append(a)

c10 = range(45, 61)
c11 = range(42 , 55)
c12 = range(51, 78)

for a in c10:
    lines25.append(a)
for a in c11:
    lines36.append(a)
for a in c12:
    lines47.append(a)
infile = 'payload113_bicycles.jpg'
image_slicer.slice(infile, 9)


infile1 = infile.replace('.jpg', '')
filePath = infile1 + '_01_01.png'
rc_solver(filePath, 0)
filePath = infile1 + '_01_02.png'
rc_solver(filePath, 1)
filePath = infile1 + '_01_03.png'
rc_solver(filePath, 2)
filePath = infile1 + '_02_01.png'
rc_solver(filePath, 3)
filePath = infile1 + '_02_02.png'
rc_solver(filePath, 4)
filePath = infile1 + '_02_03.png'
rc_solver(filePath, 5)
filePath = infile1 + '_03_01.png'
rc_solver(filePath, 6)
filePath = infile1 + '_03_02.png'
rc_solver(filePath, 7)
filePath = infile1 + '_03_03.png'
rc_solver(filePath, 8)

for val in test_list:
	if val != None:
		lines_s2.append(val)
input_text = r'bicycles'
input_text2 = 'bicycles'
if 'trai' in input_text2:
	input_text3 = 1
elif 'bus' in input_text2:
	input_text3 = 2
elif 'truc' in input_text2:
	input_text3 = 3
elif 'bicy' in input_text2:
	input_text3 = 4
elif 'airp' in input_text2:
	input_text3 = 5
elif 'boa' in input_text2:
	input_text3 = 6
elif 'motorc' in input_text2:
	input_text3 = 7
elif 'car' in input_text2:
	input_text3 = 8
elif 'tree' in input_text2:
	input_text3 = 9
elif 'fire' in input_text2:
	input_text3 = 10
elif 'crossw' in input_text2:
	input_text3 = 11
elif 'traffic li' in input_text2:
	input_text3 = 12
elif 'bridge' in input_text2:
	input_text3 = 13
elif 'tract' in input_text2:
	input_text3 = 14
elif 'taxi' in input_text2:
	input_text3 = 15
elif 'stair' in input_text2:
	input_text3 = 16
elif 'chim' in input_text2:
	input_text3 = 17
elif 'mountain' in input_text2:
	input_text3 = 18
elif 'parking' in input_text2:
	input_text3 = 19
with open('r1.txt') as f1:
	a1 = f1.readlines()
a2 = re.findall(input_text, str(a1))
if len(a2) == 3:
	pass
elif len(a2) > 3:
	pass
elif len(a2) == 2:
	for b in a1:
		ati = b.translate({ord(i): None for i in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz. '})
		if input_text2 in b:
			lines_s_h.append(ati)
	for b1 in lines_s2:
		if int(lines_s_h[0]) != int(b1[0]):
			lines_s.append(b1)
	for b1 in lines_s:
		if int(lines_s_h[1]) != int(b1[0]):
			lines_ss.append(b1)
	lines_ss = list(dict.fromkeys(lines_ss))
	lines_ss.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_ss.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_ss.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s3 = lines_ss
	try:
		if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]) and (lines_s3[0][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]) and (lines_s3[1][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]) and (lines_s3[2][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]) and (lines_s3[3][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]) and (lines_s3[4][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]) and (lines_s3[5][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[6][input_text3] > lines_s3[0][input_text3]) and (lines_s3[6][input_text3] > lines_s3[1][input_text3]) and (lines_s3[6][input_text3] > lines_s3[2][input_text3]) and (lines_s3[6][input_text3] > lines_s3[3][input_text3]) and (lines_s3[6][input_text3] > lines_s3[4][input_text3]) and (lines_s3[6][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
	except IndexError:
		if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]):
			print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
elif len(a2) == 1:
	for b in a1:
		ati = b.translate({ord(i): None for i in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz. '})
		if input_text2 in b:
			lines_s_h.append(ati)
	for b1 in lines_s2:
		if int(lines_s_h[0]) != int(b1[0]):
			lines_s.append(b1)
	lines_s.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s3 = lines_s
	if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]) and (lines_s3[0][input_text3] > lines_s3[6][input_text3]) and (lines_s3[0][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[0][0])
	if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]) and (lines_s3[1][input_text3] > lines_s3[6][input_text3]) and (lines_s3[1][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[1][0])
	if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]) and (lines_s3[2][input_text3] > lines_s3[6][input_text3]) and (lines_s3[2][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[2][0])
	if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]) and (lines_s3[3][input_text3] > lines_s3[6][input_text3]) and (lines_s3[3][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[3][0])
	if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]) and (lines_s3[4][input_text3] > lines_s3[6][input_text3]) and (lines_s3[4][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[4][0])
	if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]) and (lines_s3[5][input_text3] > lines_s3[6][input_text3]) and (lines_s3[5][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[5][0])
	if (lines_s3[6][input_text3] > lines_s3[0][input_text3]) and (lines_s3[6][input_text3] > lines_s3[1][input_text3]) and (lines_s3[6][input_text3] > lines_s3[2][input_text3]) and (lines_s3[6][input_text3] > lines_s3[3][input_text3]) and (lines_s3[6][input_text3] > lines_s3[4][input_text3]) and (lines_s3[6][input_text3] > lines_s3[5][input_text3]) and (lines_s3[6][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[6][0])
	if (lines_s3[7][input_text3] > lines_s3[0][input_text3]) and (lines_s3[7][input_text3] > lines_s3[1][input_text3]) and (lines_s3[7][input_text3] > lines_s3[2][input_text3]) and (lines_s3[7][input_text3] > lines_s3[3][input_text3]) and (lines_s3[7][input_text3] > lines_s3[4][input_text3]) and (lines_s3[7][input_text3] > lines_s3[5][input_text3]) and (lines_s3[7][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[7][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[7][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[7][0])
	for b1 in lines_s3:
		if int(lines_s_h2[0]) != int(b1[0]):
			lines_s4.append(b1)
	lines_s3 = lines_s4
	if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]) and (lines_s3[0][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]) and (lines_s3[1][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]) and (lines_s3[2][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]) and (lines_s3[3][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]) and (lines_s3[4][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]) and (lines_s3[5][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[6][input_text3] > lines_s3[0][input_text3]) and (lines_s3[6][input_text3] > lines_s3[1][input_text3]) and (lines_s3[6][input_text3] > lines_s3[2][input_text3]) and (lines_s3[6][input_text3] > lines_s3[3][input_text3]) and (lines_s3[6][input_text3] > lines_s3[4][input_text3]) and (lines_s3[6][input_text3] > lines_s3[5][input_text3]):
		print(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
