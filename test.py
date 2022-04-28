import urllib.request, urllib.parse 


def sss(url):
    try:
        protocol = "http://"
        mod_url = protocol+url
        print(mod_url)
        with urllib.request.urlopen(mod_url) as response:
            print(response.code)
            if response.code==200:
                return True
                    
    except Exception as e:
         print('Request failed:', e.reason)



with open('ss.txt') as file:
    for line in file:
        if sss(line.strip()):
            result_file=open("Result.txt",'a+')
            result_file.write('http://'+line.strip()+'\n')
            result_file.close()
            
            











     #def sss(url):
#    try:
#        print(url)
#        mod_url=url[:len(url)-1]
#        print(mod_url)
#        http = urllib3.PoolManager()
#        uri = "http://"
#        #to connect
#        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
##            s.connect(uri + mod_url, 443)##

#        response=http.request('GET', uri + mod_url)
#        print(response.status)
#    except urllib3.exceptions.HTTPError as e:
#        print('Request failed:', e.reason)



#with open('ss.txt') as file:
#    ss = file.readline()
#    print(sss(ss))



# import requests
# def sss(arg):
#     url = 'https://'
#     response = requests.get(url + arg)
#     if response.status_code == 200:
#         print('Web site exists')
#     else:
#         print('Web site does not exist') 
#         return False


# with open('ss.txt') as file:
#     ss = file.readline()
#     print(sss(ss))

#def uri_exists_get(uri: str) -> bool:
#     url = 'https://'
    
    
#     a = url + uri
#     ipAddress = socket.gethostbyname(a)
#     print("IP-адрес имени хоста {}: {}".format(a, ipAddress))



#     print(a)
#     try:
#         response = requests.get(a)
#         try:
#             response.raise_for_status()
#             return True
#         except requests.exceptions.HTTPError:
#             print('HTTPError')
#             return False
#     except Exception as e:
#         print('ConnectionError' + str(e))
#         return False


    

