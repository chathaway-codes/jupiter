from jupiter.models import Reading, User, PhysicalActivity
from random import randint

user = User.objects.all()[0]

for r in Reading.objects.all():
    r.delete()

for r in PhysicalActivity.objects.all():
    r.delete()


for i in range(1, 12):
    p = PhysicalActivity(user=user, intensity=5, duration=20*(1.125-randint(1, 25)/100.0), type='RUN')
    p.save()
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    
    p = Reading(user=user, reading=(280-((i-1)*10))*(1.05-randint(1, 10)/100.0), type='WGHT')
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    
    p = Reading(user=user, reading=70, type='HEHT')
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    
    p = Reading(user=user, reading=100*(1.125-randint(1, 25)/100.0), type='BLSG')
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    
    p = Reading(user=user, reading=(110-((i-1)*5))*(1.05-randint(1, 10)/100.0), type='PLSE')
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    
    p = Reading(user=user, reading=(150-((i-1)*2.5))*(1.05-randint(1, 10)/100.0), type='BPRS')
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
    p.when = '2012-' + repr(i) + '-01 01:01'
    p.save()
