print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

import time

inform = """PC giving an estimate number then 
if PC estimated higher then you enter (-),
but if PC estimated lower then you are entering (+),
if it is correct number then enter (E)."""

check = ""
high = 101
low = 1
count = 1							#kacinci deneme uyarisi
estimate = int((high - low)/2)		#tahmini 50 olarak aliyoruz asagi yukari neyse ona gore hareket ediyoruz

try:								#hatali giris uyarisi
	hold = input("Keep you mind a number between 0 and 100. If you are ready, enter yes (E) if you are not (H): ")
	if hold == "H" or hold == "H".lower():				#baslayip baslamama sorgusu yaptik
		print("Well let's wait a little time...")
		time.sleep(5.0)									#zaman ayari verildi
	elif hold == "E" or hold == "E".lower():			#eger kucuk harf girsede kabul ediyor
		while check != "E" and check != "E".lower():	#kontrol mekanizmasi eger bilirse sayiyi e gorunce cikacak donguden
			print(inform, "PC estimate is ", estimate)		#bilgilendirme ve tahmini sayi surekli olacak
			check = input("Estimate situation: ")			#kullanici degerlendirme inputu
			if check == "+":								#artmasi gerekiyorsa tahmin en dusuk 50 ustu olmali
				low = estimate
			elif check == "-":
				high = estimate								#azalmasi gerekiyorsa en yuksek tahmin 50 alti olmali
			else:
				print("Your chosen number is {} and Congratulations on your {}. try!!".format(estimate, count))
			estimate = int((high + low)/2)					#yarilanma metoduyla bulmaya calisiliyor
			count += 1										#kacincida bulma sayaci

except ValueError:
	print("There is something wrong... :(")
