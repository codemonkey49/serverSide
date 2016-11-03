from django.shortcuts import render, redirect
from api import *
from data.models import watchedData,itemData,commandsDB, stockData,transactionData
from commands import generateCommands
from datetime import date


def index(request):
    templateName="botEnd/index.html"
    return render(request,templateName)
def valueRetrieve(request):
    watched=watchedData.objects.all().filter(userWatched = True) | watchedData.objects.all().filter(machineWatched = True)
    #print watched,len(watched)
    
    for i in watched:
        price=fetchPrice(i.itemID)
        today=date.today()
        if (itemData.objects.all().filter(itemID=i.itemID).filter(date=today).count() == 0):
            b=itemData(itemID=i.itemID,price=price)
            b.save()
    return redirect('botEnd:index')
    
def commandsIndex(request):
    print "index"
    template_name="botEnd/commandsIndex.html"
    commands=commandsDB.objects.all()
    PIDs=[]
    for i in commands:
        if i.PID not in PIDs:
            PIDs.append(i.PID)
            
    context={"PIDs":PIDs}
    return render (request,template_name,context)
    
    
def commandsDetail(request,PID):
    print "detail"
    template_name="botEnd/commandsDetail.html"
    print generateCommands(PID)
    commands=commandsDB.objects.all().filter(PID=PID)
    context={"commands":commands}
    return render(request,template_name,context)
    
def submitTransaction(request,PID,bs,itemID,amt,price,currentLiquid):
    tr=transactionData.objects.create(
        PID=PID,
        bs=bs,
        itemID=itemID,
        amt=amt,
        price=price,
        currentLiquid=currentLiquid
        )
    tr.save()
    print "done bois"
    return redirect('botEnd:index')