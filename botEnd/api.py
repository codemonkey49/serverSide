import urllib2

def fetchData(itemID):
        url='http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='
        full=url[:73] + str(itemID) 
        response = urllib2.urlopen(full)
        html = response.read()
        return html
        
def fetchPrice(itemID):     
        html=fetchData(itemID)
        if html=='':
                return "0"
        index=html.find("price")
        price= html[index+7:index+17].split("}")[0]
        
        if ("'" in price or '"' in price):
                price=price.replace("'","")
                price=price.replace('"',"")
        if ("," in price):
                price=price.replace(",","")
                
        if ("k" in price):
                price=price.replace("k","")
                price=price.replace('"','')
                price=int(float(price)*1000)
        return int(price)
                
#print fetchPrice(440)
def fetchUrl(itemID):
        html=fetchData(itemID)
        html=html.split(",")
        url=html[1].split(":")
        url= url[2][2:]
        print url
        url="http://"+url.split('"')[0]
        return url
        
#print fetchUrl(440)

def fetchName(itemID):
        html=fetchData(itemID)
        html=html.split(",")
        name= html[5].split(":")[1]
        return name.split('"')[1]
#fetchName(440)