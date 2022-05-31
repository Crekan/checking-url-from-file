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
            
