from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    if 'totalGold' not in request.session:
        request.session['totalGold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,"ninjaGold.html")

def process(request):
    print(request.POST['location'])
    timeEarned = datetime.datetime.now()
    timeEarned.strftime("%Y-%m-%d %I:%M:%S")
    if request.POST['location'] == 'farm':
        gold_earned = random.randint(10,20)
        request.session['totalGold'] += gold_earned
        activitystring = f"Earned {gold_earned} golds in farm ({timeEarned})."
        request.session['activities'].append(activitystring)
    elif request.POST['location']  == 'cave':
        gold_earned = random.randint(5,10)
        request.session['totalGold'] += gold_earned
        activitystring = f"Earned {gold_earned} golds in cave ({timeEarned})."
        request.session['activities'].append(activitystring)
    elif request.POST['location']  == 'house':
        gold_earned = random.randint(2,5)
        request.session['totalGold'] += gold_earned
        activitystring = f"Earned {gold_earned} golds in house ({timeEarned})."
        request.session['activities'].append(activitystring)
    elif request.POST['location']  == 'casino':
        gold_earned = random.randint(-50,50)
        request.session['totalGold'] += gold_earned
        if gold_earned >= 0:
            activitystring = f"Earned {gold_earned} golds in casino ({timeEarned})."
        else:
            activitystring = f"Entered a casino & lost {gold_earned} gold... Ouch...({timeEarned})"
        request.session['activities'].append(activitystring)
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")