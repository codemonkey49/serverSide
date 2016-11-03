from django.shortcuts import render
from django.http import HttpResponse
from data.models import watchedData,itemData,transactionData,stockData

import matplotlib
matplotlib.use('Agg')    
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg



import matplotlib.pyplot as plt
import numpy as np
# Create your views here.
def index(request):
    templateName="userEnd/index.html"
    store=[]
    for item in watchedData.objects.all():
        if item.userWatched:
            store.append(item)
    context={'store':store}
    return render(request, templateName, context)

def itemDetail(request,itemID):
    templateName="userEnd/detail.html"
    transactionLog=transactionData.objects.filter(itemID=itemID)
    stockLog=stockData.objects.filter(itemID=itemID)
    
    context={"itemID":itemID,"transactionLog": transactionLog, "stockLog": stockLog}
    return render(request,templateName,context)
    
def lineGraph(request,itemID):
    f = figure(itemID, figsize=(8,8))
    dates=[]
    price=[]
    data=itemData.objects.filter(itemID=itemID)
    for i in data:
        dates.append(i.date)
        price.append(i.price)
    #dates = matplotlib.dates.date2num(dates)
    #plt.margins(x=0.1, y=0.1)
    plt.plot(dates,price, '-o')
    #plt.autoscale(enable=True, axis='y', tight=None)
    #plt.gcf().autofmt_xdate()

    #plt.axis([0, 6, 0, 20])
    plt.show()
    print "graphed: ",itemID," ",price
    
    canvas = FigureCanvasAgg(f)    
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response