import urllib2
#https://hprog99.wordpress.com/2014/08/14/how-to-setup-django-cron-jobs/comment-page-1/
def job():
    urllib2.urlopen("https://runescapev5-basedtoaster.c9users.io/auto/retrieve")
    
    
