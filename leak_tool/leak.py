

Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # Whit


import requests , os

try :
    from search_engines import Google
except:
    print(f'    |[-] {Red} TO Run The Tool , You Must Put The search_engines Folder {White} ')
    print(f'    |[-] {Red} And The Tool Must Be Outside The Folder {White}')
    exit()
#       - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  

os.system('cls' if os.name == 'nt' else 'clear')

import datetime





class leak :
    
    def __init__(self) :
        url='https://leakbase.org//session/csrf'
        headers={
            'Host': 'leakbase.org',
        'Cookie': 'destination_url=https%3A%2F%2Fleakbase.org%2F',
        'Discourse-Track-View': 'true',
        'Sec-Ch-Ua': '',
        'Discourse-Present': 'true',
        'X-Csrf-Token': 'undefined',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '""',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://leakbase.org/login',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        }


        req=requests.get(url,headers=headers).json()['csrf']
        csrf=req
        
        
        






        url='https://leakbase.org/session'
        req=requests.post(url,data={
        'login': 'Fx3',
        'password': 'Ab12345###',
        'second_factor_method': '1',
        'timezone': 'Asia/Kuwait'},headers={
        'Host': 'leakbase.org',
        'Cookie': 'destination_url=https%3A%2F%2Fleakbase.org%2F; _forum_session=hDxTuMDMKfL46b0aWXm4T3S0rfFC5r%2Fb0aRmNEhD%2FRQfc%2B2j82ixN%2F%2FPWIYtMav5jYh3WMrcMVdkF7ivlw0NuraVrxsFqhCGu4Jb270QTKE8k5%2FNg0CfmKZ3jk0%2BetANDJcEN2Tlo74BymgrdSGf0qn05MOqJYRaPJR3aHBiL6RVbRkgux1Naip9aDZ2tIi3ldzhCudNaC8PDjbrCVmnVr0Anjq1s7MTeeesYoHQ4BRGQEvFfw7IdHI4shcPY%2BA608Gt11C1qysduvRAxJgoMyAyX20LWA%3D%3D--dTz2il0ToPcKdEFa--DOR19eTB1MIrV4RuVy3QIg%3D%3D',
        'Content-Length': '102',
        'Sec-Ch-Ua': '',
        'Discourse-Present': 'true',
        'X-Csrf-Token': 'vDiOKwqW2adM2dZJwd6TkpWZex4t318yEdcaH_mk8IbLccxeT4MPHEAzEc7o5emgg9TneMF15C8sFu27XsanwA',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '""',
        'Origin': 'https://leakbase.org',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://leakbase.org/login',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
            }).cookies



        self._t=req['_t']
        self._forum_session=req['_forum_session']
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    #def REST(self,NAME_FUNC,MORE=None):
     #   if NAME_FUNC == 'ALL':
      #      self.ALL
        






    def ftp_leak_dork(self):
        try:
                search = f'inurl:ftp intitle:"index of"'
                engine = Google()
                results = engine.search(search, pages=15)
                range,c=0,0
                links=[]
                for data in results.__dict__['_results']:
                    print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {range}',end="")
                    range=range+1
                    link = data['link']      
                    
                    links.append(link)
                print('\n')
                
                for i in links:
                        d=(datetime.datetime.now())
                        date=d.time()
                        print(White+f'[{Yellow}{date}{White}] {Blue}/{White} [{c}] -{Green} YOUR LEAK : '+i+White)
                        c=c+1
                print(f'''\n                    {White}  [99]{Red} EXIT          \n''')
                choose = input(Red + f"rodconsole " + White +'> ')
                if choose == '99':
                    exit()
                else:
                    input(Red+'exit X')
                    exit()
        except:
            pass 
        
        if results.__dict__['_results'] == []:
                    
                        print(f'\n\n    {White}| [-]{Red} Check Your Wifi {White} ')
                        print(f'    {White}| [-]{Red} If You Are Already Connected To The WiFi , It Is Possible That You Have Been Blocked Due To Too Many Attempts , Try Later Or Turn The VPN  {White} ')
                        print(f'    {White}| [-]{Yellow} Or We Did Not Find Information For The Site Yiu Entered  {White} ')
                        
                        exit()
        exit()









      
        
    

    def cam_leak_dork(self,MORE=False):
        try:
                if MORE == False:
                    search = f'intitle:"webcamxp 5" inurl:":"'
                else:
                    search = f'intitle:"yawcam" inurl:8081'
                    
                engine = Google()
                results = engine.search(search, pages=15)
                range,c=0,0
                links=[]
                for data in results.__dict__['_results']:
                    print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {range}',end="")
                    range=range+1
                    link = data['link']      
                    
                    links.append(link)
                print('\n')

                for i in links:
                        d=(datetime.datetime.now())
                        date=d.time()
                        print(White+f'[{Yellow}{date}{White}] {Blue}/{White} [{c}] -{Green} YOUR LEAK : '+i+White)
                        c=c+1
                if MORE == True :
                    print(f'''\n                      {White}  [99]{Red} EXIT          \n''')
                    input(Red + f"rodconsole " + White +'> ')
                    exit()
                    
                
                    
                print(f'''\n                    {White}  [99]{Red} EXIT          {White} [M] {Yellow} MORE        \n''')
                choose = input(Red + f"rodconsole " + White +'> ')
                if choose == 99 :
                    exit()
                
                elif choose.upper() == 'M':
                    self.cam_leak_dork(MORE=True)
        except:
            pass 
        
        if results.__dict__['_results'] == []:
                    
                        print(f'\n\n    {White}| [-]{Red} Check Your Wifi {White} ')
                        print(f'    {White}| [-]{Red} If You Are Already Connected To The WiFi , It Is Possible That You Have Been Blocked Due To Too Many Attempts , Try Later Or Turn The VPN  {White} ')
                        print(f'    {White}| [-]{Yellow} Or We Did Not Find Information For The Site Yiu Entered  {White} ')
                        input(Red+'exit X')
                        
                        exit()
        input(Red+'exit X')
        exit()




    
    
    
    
    
    def all_leak_dork(self):
        try:
                search = f'allintext:username filetype:log'
                engine = Google()
                results = engine.search(search, pages=15)
                range,c=0,0
                links=[]
                for data in results.__dict__['_results']:
                    print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {range}',end="")
                    range=range+1
                    link = data['link']      
                    
                    links.append(link)
                print('\n')
                for i in links:
                        d=(datetime.datetime.now())
                        date=d.time()
                        print(White+f'[{Yellow}{date}{White}] {Blue}/{White} [{c}] -{Green} YOUR LEAK : '+i+White)
                        c=c+1
                print(f'''\n                    {White}  [99]{Red} EXIT          \n''')
                choose = input(Red + f"rodconsole " + White +'> ')
                if choose == '99':
                    exit()
                
                
                    
                
                        
        except:
            pass 
        
        if results.__dict__['_results'] == []:
                    
                        print(f'\n\n    {White}| [-]{Red} Check Your Wifi {White} ')
                        print(f'    {White}| [-]{Red} If You Are Already Connected To The WiFi , It Is Possible That You Have Been Blocked Due To Too Many Attempts , Try Later Or Turn The VPN  {White} ')
                        print(f'    {White}| [-]{Yellow} Or We Did Not Find Information For The Site Yiu Entered  {White} ')
                        input(Red+'exit X')
                        
                        exit()
        input(Red+'exit X')
        exit()
    
    
    def search(self,search):
        _t=self._t 
        _forum_session = self._forum_session
        headers={
        'Host': 'leakbase.org',
        'Cookie':
        '_t='+_t+'; _forum_session='+_forum_session,
        'Sec-Ch-Ua': '',
        'Discourse-Present': 'true',
        'X-Csrf-Token': '0VDyLPP6Q0ZKbNbxbtYVZBCGoJXNb-JlSm90rAiNPETg06SFDQddqKk1nvaMJuya2-lCXpKK0HEl720h9OMQAA',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36',
        'Discourse-Logged-In': 'true',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '""',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://leakbase.org/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',

        }
        leak=[]
        DAta=[]
        C,range=0,0
        
        try:
            req=requests.get('https://leakbase.org/search/query?term='+search,headers=headers).json()
            for i in req['topics']:
                DATA=str(i['last_posted_at'])
                DAta.append(DATA.split('T')[0])
                
                response=requests.get('https://leakbase.org/t/'+i['slug']+'/'+str(i['id']),headers=headers).text
                print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {C}',end="")
                C=C+1
                
                if 'anonfiles' in response :
                        code_anonfiles=response.split('"https://anonfiles.com/')[1]
                        
                        code_anonfiles=code_anonfiles.split('"')[0]
                        leak.append(i['slug']+'::https://anonfiles.com/'+code_anonfiles)
        except:
            print(f'{Red}[-] - {search} ont found ')
            exit()
            
        if leak == []:
            print(f'{Red}[-] - {search} ont found ')
            exit()
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Red+'''
            ████████╗██╗████████╗██╗     ███████╗    
            ╚══██╔══╝██║╚══██╔══╝██║     ██╔════╝    
               ██║   ██║   ██║   ██║     █████╗      
               ██║   ██║   ██║   ██║     ██╔══╝        
               ██║   ██║   ██║   ███████╗███████╗    
               ╚═╝   ╚═╝   ╚═╝   ╚══════╝╚══════╝

                  ''')            
        for i in leak:
            d=(datetime.datetime.now())
            date=d.time()
            print(White+f'        [{date}{White}] {Blue}/{White}  ['+str(range)+'] '+Green+i.split('::')[0]+'       '+Red+DAta[range])
            range=range+1
        
        print(f'''\n           {White} [+] {Yellow} CHOOSE         {White}  [99]{Red} EXIT          \n''')
            
        while True:        
            choose = input(Red + f"rodconsole " + White +'> ')
            
            if choose == '99' :
                exit()
            
            
            try:
                choose=int(choose)
                l=leak[choose]
                link=(White+f'[+] -{Green} YOUR LEAK : {Yellow}'+l.split('::')[1])
                print(link)
            except:
                input(Red+'exit X')
                exit()
            
        
    
    
    
    
    
    
    
    
    
    
    def TOP(self,MORE=False):

        if MORE == True:
            url1='https://leakbase.org/c/leaks/11/l/top.json?ascending=false&page=4'
            url2='https://leakbase.org/c/leaks/11/l/top.json?ascending=false&page=5'
            url3='https://leakbase.org/c/leaks/11/l/top.json?ascending=false&page=6'
            DAta=[]
            leak=[]
            
        else:
            url1='https://leakbase.org/c/leaks/11/l/top.json?ascending=false'
            url2='https://leakbase.org/c/leaks/11/l/top.json?ascending=false&page=2'
            url3='https://leakbase.org/c/leaks/11/l/top.json?ascending=false&page=3' 
        _t=self._t 
        _forum_session = self._forum_session


        
        headers={
        'Host': 'leakbase.org',
        'Cookie':
        '_t='+_t+'; _forum_session='+_forum_session,
        'Sec-Ch-Ua': '',
        'Discourse-Present': 'true',
        'X-Csrf-Token': '0VDyLPP6Q0ZKbNbxbtYVZBCGoJXNb-JlSm90rAiNPETg06SFDQddqKk1nvaMJuya2-lCXpKK0HEl720h9OMQAA',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36',
        'Discourse-Logged-In': 'true',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '""',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://leakbase.org/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',

        }
        range=0
        leak=[]
        
        DAta=[]
        URLS=[url1,url2,url3]
        PASS=[]
        C=0
        print('\n')
        try:
            for i in URLS:
                req=requests.get(i,headers=headers).json()['topic_list']
                for i in req['topics']:
                    DATA=str(i['last_posted_at'])
                    DAta.append(DATA.split('T')[0])
                    
                    response=requests.get('https://leakbase.org/t/'+i['slug']+'/'+str(i['id']),headers=headers).text
                    print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {C}',end="")
                    C=C+1
                    
                    
                    
                    if 'anonfiles' in response :
                        code_anonfiles=response.split('"https://anonfiles.com/')[1]
                        
                        code_anonfiles=code_anonfiles.split('"')[0]
                        leak.append(i['slug']+'::https://anonfiles.com/'+code_anonfiles)
            
            if MORE == True:
                pass
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            pass

        print(Red+'''
            ████████╗██╗████████╗██╗     ███████╗    
            ╚══██╔══╝██║╚══██╔══╝██║     ██╔════╝    
               ██║   ██║   ██║   ██║     █████╗      
               ██║   ██║   ██║   ██║     ██╔══╝        
               ██║   ██║   ██║   ███████╗███████╗    
               ╚═╝   ╚═╝   ╚═╝   ╚══════╝╚══════╝

                  ''')            
        for i in leak:
            d=(datetime.datetime.now())
            date=d.time()
            print(White+f'        [{date}{White}] {Blue}/{White}  ['+str(range)+'] '+Green+i.split('::')[0]+'       '+Red+DAta[range])
            
            range=range+1
        
        print(f'''\n           {White} [+] {Yellow} CHOOSE         {White}  [99]{Red} EXIT      {White} [M] {Yellow} MORE  \n''')
            
        while True:        
            choose = input(Red + f"rodconsole " + White +'> ')
            if choose == '99' :
                exit()
                
            elif choose.upper() == 'M':
                self.TOP(MORE=True)
            
            try:
                choose=int(choose)
                l=leak[choose]
                link=(White+f'[+] -{Green} YOUR LEAK : {Yellow}'+l.split('::')[1])
                print(link)
            except:
                input(Red+'exit X')
                exit()
            
            try:
                link=('PASS: '+PASS[choose])
            except:
                pass
        exit()    
    
    







    def NEW(self,url):
        
        
        _t=self._t 
        _forum_session = self._forum_session
        headers={
        'Host': 'leakbase.org',
        'Cookie':
        '_t='+_t+'; _forum_session='+_forum_session,
        'Sec-Ch-Ua': '',
        'Discourse-Present': 'true',
        'X-Csrf-Token': '0VDyLPP6Q0ZKbNbxbtYVZBCGoJXNb-JlSm90rAiNPETg06SFDQddqKk1nvaMJuya2-lCXpKK0HEl720h9OMQAA',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36',
        'Discourse-Logged-In': 'true',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '""',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://leakbase.org/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',

        }
        range=0
        leak=[]
        
        DAta=[]
        PASS=[]
        C=0
        print('\n')
        
        
        req=requests.get(url,headers=headers).json()['topic_list']
        for i in req['topics']:
            DATA=str(i['last_posted_at'])
            DAta.append(DATA.split('T')[0])
            
            response=requests.get('https://leakbase.org/t/'+i['slug']+'/'+str(i['id']),headers=headers).text
            print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {C}',end="")
            C=C+1
            
            
            
            if 'anonfiles' in response :
                code_anonfiles=response.split('"https://anonfiles.com/')[1]
                
                code_anonfiles=code_anonfiles.split('"')[0]
                leak.append(i['slug']+'::https://anonfiles.com/'+code_anonfiles)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Red+'''
            ████████╗██╗████████╗██╗     ███████╗    
            ╚══██╔══╝██║╚══██╔══╝██║     ██╔════╝    
               ██║   ██║   ██║   ██║     █████╗      
               ██║   ██║   ██║   ██║     ██╔══╝        
               ██║   ██║   ██║   ███████╗███████╗    
               ╚═╝   ╚═╝   ╚═╝   ╚══════╝╚══════╝

                  ''')            
        for i in leak:
            d=(datetime.datetime.now())
            date=d.time()
            print(White+f'        [{date}{White}] {Blue}/{White}  ['+str(range)+'] '+Green+i.split('::')[0]+'       '+Red+DAta[range])
            range=range+1
        
        print(f'''\n           {White} [+] {Yellow} CHOOSE         {White}  [99]{Red} EXIT    \n''') 
            
        while True:        
            choose = input(Red + f"rodconsole " + White +'> ')
            if choose == '99' :
                exit()
            
           
            
            try:
                choose=int(choose)
                l=leak[choose]
                link=(White+f'[+] -{Green} YOUR LEAK : {Yellow}'+l.split('::')[1])
                print(link)
            except:
                input(Red+'exit X')
                exit()
                
            
            try:
                link=('PASS: '+PASS[choose])
            except:
                pass
        exit()















    
    def ALL(self,MORE=None):
        
        
        _t=self._t 
        _forum_session = self._forum_session
        if MORE == True:
            url1='https://leakbase.org/c/leaks/11/l/latest.json?ascending=false&page=4'
            url2='https://leakbase.org/c/leaks/11/l/latest.json?ascending=false&page=5'
            url3='https://leakbase.org/c/leaks/11/l/latest.json?ascending=false&page=6'
        else:    
            url1='https://leakbase.org/c/leaks/11/l/latest.json?ascending=false'
            url2='https://leakbase.org/c/leaks/11/l/latest.json?ascending=false&page=2'
            url3='https://leakbase.org/c/leaks/11/l/latest.json?ascending=false&page=3'
        headers={
        'Host': 'leakbase.org',
        'Cookie':
        '_t='+_t+'; _forum_session='+_forum_session,
        'Sec-Ch-Ua': '',
        'Discourse-Present': 'true',
        'X-Csrf-Token': '0VDyLPP6Q0ZKbNbxbtYVZBCGoJXNb-JlSm90rAiNPETg06SFDQddqKk1nvaMJuya2-lCXpKK0HEl720h9OMQAA',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36',
        'Discourse-Logged-In': 'true',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '""',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://leakbase.org/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',

        }
        range=0
        leak=[]
        
        DAta=[]
        URLS=[url1,url2,url3]
        PASS=[]
        C=0
        print('\n')
        try:
            for i in URLS:
                req=requests.get(i,headers=headers).json()['topic_list']
                for i in req['topics']:
                    DATA=str(i['last_posted_at'])
                    DAta.append(DATA.split('T')[0])
                    
                    response=requests.get('https://leakbase.org/t/'+i['slug']+'/'+str(i['id']),headers=headers).text
                    print(f'\r {White}[+] - {Yellow} CHECKING :{Red} {C}',end="")
                    C=C+1
                    
                    
                    
                    if 'anonfiles' in response :
                        code_anonfiles=response.split('"https://anonfiles.com/')[1]
                        
                        code_anonfiles=code_anonfiles.split('"')[0]
                        leak.append(i['slug']+'::https://anonfiles.com/'+code_anonfiles)
            if MORE == True:
                pass
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except:
            pass

        print(Red+'''
            ████████╗██╗████████╗██╗     ███████╗    
            ╚══██╔══╝██║╚══██╔══╝██║     ██╔════╝    
               ██║   ██║   ██║   ██║     █████╗      
               ██║   ██║   ██║   ██║     ██╔══╝        
               ██║   ██║   ██║   ███████╗███████╗    
               ╚═╝   ╚═╝   ╚═╝   ╚══════╝╚══════╝

                  ''')            
        for i in leak:
            
            d=(datetime.datetime.now())
            date=d.time()
            print(White+f'        [{date}{White}] {Blue}/{White}  ['+str(range)+'] '+Green+i.split('::')[0]+'       '+Red+DAta[range])
            range=range+1
        
        print(f'''\n           {White} [+] {Yellow} CHOOSE         {White}  [99]{Red} EXIT      {White} [M] {Yellow} MORE  \n''')
            
        while True:        
            choose = input(Red + f"rodconsole " + White +'> ')
            if choose == '99' :
                exit()
            
            elif choose.upper() == 'M':
                self.ALL(MORE=True)
            
            try:
                choose=int(choose)
                l=leak[choose]
                link=(White+f'[+] -{Green} YOUR LEAK : {Yellow}'+l.split('::')[1])
                print(link)
            except:
                input(Red+'exit X')
                exit()
                
            
            try:
                link=('PASS: '+PASS[choose])
            except:
                pass
        exit()






while True :
        
    print(Red+f'''
    ⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢀⣿⣿⣿⡿⠟⠛⢛⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣾⣿⠟⠁⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣸⡿⠁⠀⠀⠀⠀⣼⣿⣿⣿⣿⡟⠀⠈⠻⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢀⡟⠁⠀⠀⠀⠀⢰⣿⣿⣿⣿⡟⠀⠀⠀⠀⠈⠛⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀{White} BY T.ME/FX_PY⠀⠀{Red}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠘⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢰⣿⠀⢘⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣷⣄⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠻⣿⣿⡇⠀⠈⠂
    ⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠟⣹⡿⢿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠋⠀⠀⢿⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣭⣵⣾⠟⠁⠀⠙⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⢸⡇⢀⡾⠀⠀⢀⣾⣿⣿⣣⠀⠀⠀⣾⣿⠃⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠀⠉⠛⠛⠋⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⣆⠀⠀⠀⠀⣿⣿⣿⡇⢀⣴⡿⢿⣿⣿⡿⠀⠀⣴⣿⡟⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣷⣤⣤⣼⣿⣿⣿⣷⣾⠟⠁⠀⠉⠉⣀⣴⣾⠿⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣤⣀⣀⣀⣙⢿⣿⣿⣿⣿⣿⠛⣿⣿⣯⣤⠶⠶⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⡟⠁⠀⠈⠻⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⣀⣴⣿⠟⠉⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⠾⠛⠉⠀⠀⠀⠀⠀{Green}  v 2.0 {Red}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                                                                                   
                                
                
                    {White}[1] {Yellow} SEARCH LEAK        
                    {White}[2] {Yellow} ALL LEAK       
                    {White}[3] {Yellow} TOP LEAK 
                    {White}[4] {Yellow} NEW LEAK 
                    
                    {White}[5] {Yellow} SEARCH LEAK WITH DORKS
                    {White}[6] {Yellow} SEARCH CAM WITH DORKS
                    {White}[7] {Yellow} SEARCH FTP FILES WITH DORKS
                    
                    {Green}[+] N : NEXT PAGE             (Page : 1/2)
                    {Red}[-] E : EXIT  {White}    
        ''')

    prompt = input(Red + f"rodconsole " + White +'> ')
    
    
    
    if prompt == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''              {Red}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠐⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠻⠃⠀⣼⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠛⠀⠀⠀⠀⠀⠘⠛⠀⣴⣾⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⠆⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⠟⢀⣤⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⣠⣴⣤⣉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⡿⠟⢋⣄⡀⠀⠀⢸⡿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣷⣦⣈⠛⢿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣿⣿⣶⡄⢤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⣄⠘⣿⣿⣿⣿⣿⣿⡇⣽⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡀⠙⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣄⠘⢿⣿⠟⠘⠻⣿⣿⣿⣿⠿⠃⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣠⣶⣿⣿⣿⣶⣤⠀⣴⣾⣦⠀⠻⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠙⠿⠋⠀⠀⠀⠀⠀⠀⠀⠉⠋⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⠀⠻⢿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠿⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣷⣦⣍⠛⠿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠉⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣿⣿⣿⣿⣿⡃⠀⠈⠙⠛⣉⣴⣾⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣻⣿⣿⣿⣿⣿⠃⠀⠀⠀⠈⣭⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡙⠿⠟⠋⠁⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠺⠿⠛⠉⣴⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⡟⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⢠⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⢾⣿⣿⠀⣠⣄⠀⠸⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⢠⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⣶⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        {White} BY T.ME/FX_PY
        
        {White}[+] - {Yellow}New leaks are added almost every day
        {White}[+] - {Yellow}This tool was programmed by : {Green} FX
        {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
        
        {White}[+] - {Yellow} WAIT                 
              ''')
        
        
        l=leak()
        l.cam_leak_dork()
        
    
    if prompt == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
              {Red}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⣲⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠊⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠁⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⠀⠀⠀⠀⢀⣀⣀⠤⠖⠈⠀⠀⢀⡜⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠓⠲⢤⣸⠒⣊⣭⠛⠉⠀⠀⠀⠀⠀⢀⣠⢿⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⣹⠎⠀⠀⠑⡄⠀⢀⡠⠔⢊⡥⢺⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⣾⠋⠁⣠⠞⠁⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⡠⠊⡜⠁⠀⠀⠀⢀⡊⠁⠁⠀⢊⡀⠀⠀⠀⣀⣉⣓⣦⡤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡤⠊⠁⠸⠀⠀⠀⡠⡖⡝⠀⠀⠀⠀⠀⠈⢉⡩⠭⠒⢋⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠑⠒⠛⠒⠋⠁⠀⠀⠀⠀⠀⠀⠘⠤⣀⡀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⢀⣀⠤⠄⠀⠀⠀⡰⠚⢧⠉⠒⠒⠮⠽⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠁⡠⣖⠂⠀⠀⠀⡠⠋⠉⠀⡀⠀⠀⢀⡴⠁⠀⠸⡄⠀⠀⠀⠀⡇⠙⢌⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠐⠁⣀⡠⠔⠋⣀⣀⡴⠚⠓⡶⣞⣉⣀⣀⡠⢤⠇⠀⠀⠀⢰⣃⡀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⣠⡊⠁⡀⣠⠞⠁⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⣿⠀⠈⠑⢄⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣽⢻⡏⠁⠀⠀⠀⢀⠞⠑⠦⠤⠤⠤⠄⡸⠁⠀⠀⠀⢸⠉⣆⠀⠀⠘⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠃⠀⠀⠀⢀⢏⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⢸⠀⠘⡄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠑⠦⠤⠤⠄⢲⠁⠀⠀⠀⠀⠀⠘⣆⣀⣹
   
            {White} BY T.ME/FX_PY
            
            {White}[+] - {Yellow}New leaks are added almost every day
            {White}[+] - {Yellow}This tool was programmed by : {Green} FX
            {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
            
            {White}[+] - {Yellow} WAIT                 
              ''')
        
        
        l=leak()
        l.ftp_leak_dork()
        
           
    
    
    elif prompt == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'''{Red}
        ⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣿⠀⣰⡏⠀⠀⢀⣤⠶⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢸⣿⢀⡿⣀⣠⣠⣿⣯⡴⡢⡢⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠠⣌⢟⣴⠟⣉⣴⡿⠗⣢⣾⡃⣾⡇⢠⠴⢬⠙⣶⡀⠀⠀⠀⠀⠀
    ⠀⠩⣳⡿⢡⢋⣥⣶⡺⣿⣛⣯⣣⢌⠳⢬⣁⡼⠃⣿⣿⢡⠀⠀⠀⠀
    ⠀⣸⣿⢿⣘⠘⠃⣸⣿⠈⠉⢑⠋⠁⣷⣦⣤⣴⣾⣿⡿⠘⠇⠀⠀⠀
    ⢰⣿⣿⢿⣿⣿⠿⠟⠁⢀⣀⣈⣿⣷⠉⠙⠛⠛⣩⣭⠀⠂⢵⡄⠀⠀
    ⠀⠈⠐⠛⠉⠀⠀⠀⠀⠀⠜⡟⠋⠁⠀⠀⠀⠀⣿⡟⠀⢸⡇⡷⢤⠤
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢀⣼⡿⠁⢀⣾⣧⠐⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠛⠁⣀⣴⣿⣿⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⣠⣴⣿⣿⡿⠟⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⡾⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠋⠀⠀⠀⠀⠀  
    
                {White} BY T.ME/FX_PY
                    
                {White}[+] - {Yellow}New leaks are added almost every day
                {White}[+] - {Yellow}This tool was programmed by : {Green} FX
                {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
                
                {White}[+] - {Yellow} WAIT
              ''')
        l=leak()   
        l.ALL()
    
        
    
    elif prompt == '5' :
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'''{Red}
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⡀⠀⠀⢀⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀
        ⣀⣀⣀⣤⣤⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣀⣀⣀
        ⠘⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⡿⠃
        ⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀
        ⠀⠀⠀⠀⣿⣿⡏⠉⠉⣿⣟⠛⠛⠛⠛⠛⠛⣻⣿⠉⠉⢹⣿⣿⠀⠀⠀⠀
        ⠀⠀⠀⠀⠹⣿⣷⢤⡀⠙⠉⠀⠀⠀⠀⠀⠀⠉⠋⢀⡤⣾⣿⠏⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠈⢿⣦⡁⠿⢿⠁⠀⠀⠀⠀⠈⡿⠿⢈⣴⡿⠁⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠘⢿⣿⠂⠀⣀⣠⣀⣀⣄⣀⠀⠐⣿⡿⠃⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠈⠻⠿⠿⠟⠁⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣦⣤⣀⣀⣤⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            {White} BY T.ME/FX_PY
            
            {White}[+] - {Yellow}New leaks are added almost every day
            {White}[+] - {Yellow}This tool was programmed by : {Green} FX
            {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
            
            {White}[+] - {Yellow} WAIT
              ''')
        l=leak()
        l.all_leak_dork()
    
        
    elif prompt == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'''{Red}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠄⠀⠀⠀⠀⢀⣠⣴⣶⠟⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⢛⡝⠁⠀⠀⠀⠀⠐⠿⢿⡼⠃⠀⠀⠀⠀⠀⢠⠀⠀
            ⠀⠀⠀⠀⠀⠀⣀⣉⣉⣉⠙⠀⠀⣀⣤⣶⣾⣿⣷⡄⠁⠀⠀⠀⠀⢀⣴⢿⠀⠀
            ⠀⠀⠀⢀⣴⣿⣿⣟⠯⢹⡇⢀⣾⣿⣿⣿⣿⡍⣸⡇⠀⠀⠀⠀⠐⢿⣃⡞⠀⠀
            ⠀⠀⣰⣿⣿⣿⣿⡙⢀⣾⠃⣼⣿⣿⣿⡟⠇⣰⡟⢀⣠⣾⣿⣿⣧⠈⡿⠁⠀⠀
            ⠀⠀⣿⡿⣯⠛⠆⢀⣼⠇⠀⢻⣿⣿⡇⣁⣴⢟⣵⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀
            ⠀⠀⠈⠛⠶⠾⠿⠛⠁⠀⢀⣀⣈⣙⠛⠋⠁⣾⣿⣿⣿⠻⠉⣽⠃⠀⠀⠀⠀⣠
            ⠀⣀⣴⣶⣶⣦⣤⣤⣶⣾⣿⣿⣿⣿⣿⣶⡄⣿⣿⠏⠉⢀⣾⠃⠀⠀⢀⣠⣾⡟
            ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠏⣿⡈⠛⠛⠛⢋⣡⣴⣶⣤⠹⣇⡾⠀
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⢀⣿⠀⢀⣴⣿⣿⣿⣿⣿⣿⠀⠟⠀⠀
            ⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠁⢸⡟⠀⣸⣿⣿⣿⢻⠏⣹⠏⠀⠀⠀⠀
            ⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠘⣿⡀⢹⡿⠃⠋⣀⡼⠋⠀⠀⠀⠀⠀
            ⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⡿⢦⠁⠀⣸⡇⠈⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠈⢻⣿⣿⠻⣿⡙⠛⠀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠉⠻⠷⣤⣴⣶⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

            {White} BY T.ME/FX_PY
            
            {White}[+] - {Yellow}New leaks are added almost every day
            {White}[+] - {Yellow}This tool was programmed by : {Green} FX
            {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
            
            {White}[+] - {Yellow} WAIT
              ''')
        search = input(Red + f"Enter name the leak " + White +'> ')
        l=leak()   
        l.search(search)
    
    elif prompt == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f'''{Red}

            ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⡦⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢰⣿⣛⣉⣉⣉⣩⣭⣥⣤⣤⣤⡤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⢢⠆⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠤⠤⠄⢀⣀⣀⣀⡘⡄⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠐⠁⠀⠀⠀⠀⡀⠀⠀⢴⣶⣧⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠨⣿⣿⣷⡄⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀⠀⠀⢰⠀⠀⠙⣤⣶⣿⣿⣿⣿⡄⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⡐⠁⠀⠀⠀⠀⠀⡠⣴⠾⣷⡆⠀⢿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⣴⡄⢻⣿⣿⣿⣿⣿⠀⠀⠀⠀
            ⠀⠀⠀⠀⢸⠀⠀⢠⠀⠀⠀⠀⠀⠀⠈⠉⢉⠿⢿⣆⢿⣿⣿⣿⣿⡀⠀⠀⠀
            ⠀⠀⠀⠀⠎⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠘⠋⢛⣟⠛⠃⠙⠻⠿⣿⡇⠀⠀⠀
            ⠀⠀⠀⢸⡄⠀⠀⡘⠋⠉⡀⢠⣾⡰⢶⣶⡖⠁⣤⣳⣿⣶⢶⣶⡌⠳⠤⣀⣀
            ⠀⠀⠀⢸⢠⠀⢀⣿⣿⣶⣿⣿⣿⠇⠀⠁⣷⣄⣈⣙⣛⣿⣿⣿⡲⡒⠒⠒⠊
            ⠀⠀⠀⠀⣿⣾⣿⣿⣿⣿⣿⣿⡟⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣟⣿⣶⡄⠀⠀
            ⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠐⣿⠿⣿⣿⣿⣿⡿⠋⠀⠙⣿⡇⠀⠀
            ⠀⠀⠀⣿⣿⡿⠁⠸⣿⣿⣿⣿⣿⣦⠸⠋⢸⣿⣿⣿⡿⠁⠀⠀⠀⢸⣷⡀⠀
            ⠀⠀⠀⣻⣿⡇⠀⠀⠀⣹⣿⡿⢻⣿⢠⡀⠸⣿⣿⣿⣧⠀⠀⠀⠀⠘⣿⣧⠀
            ⠀⠀⢠⠉⣿⠇⠀⠀⢰⠋⣿⣰⣁⡟⠀⠁⢼⣿⡿⠿⠏⠀⠀⠀⠀⠀⠋⠟⠀
            ⠀⠀⢰⣿⠋⠀⠀⠀⢀⣿⡏⠛⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⣾⡇⠀⠀⠀⢀⠎⢹⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠜⢹⡇⠀⠀⠀⠾⣶⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠮⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀
                 
            {White} BY T.ME/FX_PY
            
            {White}[+] - {Yellow}New leaks are added almost every day
            {White}[+] - {Yellow}This tool was programmed by : {Green} FX
            {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
            
            {White}[+] - {Yellow} WAIT
              ''')
        
        l=leak()   
        l.TOP()
    
    
    
    
    
    elif prompt == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''{Red}

        ⠀⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⡀⠀
        ⠀⢸⣿⣧⣀⣀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣀⣼⣿⡧⠀
        ⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀
        ⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠿⠿⠛⠋⠁⠀⠀⠀
        
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠀⠀⠀⠀⠀⠀⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
        
        
    
            {White} BY T.ME/FX_PY
                
            {White}[+] - {Yellow}New leaks are added almost every day
            {White}[+] - {Yellow}This tool was programmed by : {Green} FX
            {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
            
            {White}[+] - {Yellow} WAIT
              ''')

        l=leak()   
        l.NEW('https://leakbase.org/c/leaks/11/l/new')
        
    elif prompt.upper() == 'N' :
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'''{Red}
    ⡌⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢀
    ⣿⣌⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠟⣱⣿
    ⢹⣿⣧⡈⠻⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⣡⣾⣿⠇
    ⢰⡙⢿⣿⣷⣌⠛⢿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡿⢋⣡⣾⣿⡿⣫⡆
    ⠈⢿⣦⣝⠻⣿⣿⣦⣉⠻⢿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⡿⠛⣡⣴⣿⣿⠟⣩⣾⡿⠁
    ⠀⠈⠻⣿⣷⣮⡙⢿⣿⣷⣤⡉⠻⢿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⡿⠟⢉⣴⣾⣿⠿⣋⣵⣾⣿⠟⠁⠀
    ⠀⠀⠰⣌⠻⣿⣿⣷⣬⡛⢿⣿⣷⣤⡉⠻⢿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⡿⠛⣉⣤⣾⣿⡿⢛⣥⣾⣿⣿⢟⣡⠆⠀⠀
    ⠀⠀⠀⠹⣿⣮⣙⢿⣿⣿⣷⣭⡻⣿⣿⣷⣦⣉⠻⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠟⣁⣴⣾⣿⡿⣟⣽⣾⣿⣿⠿⣋⣴⣿⠏⠀⠀⠀
    ⠀⠀⠀⠀⠈⠻⣿⣷⣬⣛⢿⣿⣿⣷⣿⣿⣿⣿⡇⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡏⢸⣿⣿⣿⣿⣾⣿⣿⡿⣛⣵⣾⡿⠟⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣷⣮⣟⢿⣿⣿⣿⣿⡇⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡇⢸⣿⣿⣿⣿⡿⣻⣵⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣇⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⣼⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⠘⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢁⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⢻⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡏⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⡄⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠀⠀⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                  
            {White}[+] - {Yellow}New leaks are added almost every day
            {White}[+] - {Yellow}This tool was programmed by : {Green} FX
            {White}[+] - {Yellow}Telegram channel{Green}   T.ME/FX_PY
            {White}[+] - {Yellow}User Telegram{Green}      T.ME/TVVNU
            {White}[+] - {Yellow}Instagram account{Green}  FX_PY3
            {White}[+] - {Yellow}GitHub account{Green}     TVVNP2
            {White}[+] - {Yellow}It is not allowed to remove the rights of the programmer from the tool
            {White}[+] - {Yellow}THX   
            
            {White}[-] -     {Yellow} B : BACK PAGE                (Page : 2/2)
            {White}[-] -     {Red} E : EXIT
            ''')
        
        prompt2 = input(Red + f"rodconsole " + White +'> ')
        
        if prompt2.upper() == 'E':
            exit()
        elif prompt2.upper() == 'B' :
            os.system('cls' if os.name == 'nt' else 'clear')

            
            continue 
        else:
            exit()
    elif prompt.upper() == 'E' :
        exit()
    
    
        
        
    else:
        input(Red+'exit X')
        exit()