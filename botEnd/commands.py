from data.models import stockData,watchedData,itemData
from api import fetchPrice
from datetime import date, timedelta
def generateCommands(PID):
    #sell
    stock=stockData.objects.all().filter(PID=PID)
    sell=[]
    for i in stock:
        price=fetchPrice(i.itemID)
        if i.price<=price+(price*0.1):
            sell.append(i)
        
    
    #buy
    items=watchedData.objects.all().filter(machineWatched=True)
    buy=[]
    for i in items:
        A30=averagePrice(i,30)
        #AL30=averagePrice(i,60,30)
        A100=averagePrice(i,100)
        A3=averagePrice(i,3)
        if A30<A100 and A3>A30:
            buy.append(i)
    
    

def averagePrice(item,start,finish=0):
    startDate=date.today()-timedelta(days=start)
    endDate=date.today()-timedelta(days=finish)
    data=itemData.objects.all().filter(itemID=item.itemID).filter(date__range=[startDate,endDate])
    prices=[]
    for i in data:
        prices.append(i.price)
        if len(prices) !=0:
            return sum(prices)/float(len(prices))
        else:
            return 0
    
