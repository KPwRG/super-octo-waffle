from django.shortcuts import render, redirect

def index(request):
    return render(request,"index.html")

# def create_user(request):
#     print("Got Post Info....................................")
#     print(request.POST)
#     return render(request, "index.html")

def create_user(request):
    # print("Got Post info>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    request.session['age'] = request.POST['age']
    request.session['gender'] = request.POST['gender']
    # name_from_form = request.POST['name']
    # email_from_form = request.POST['email']
    # age_from_form = request.POST['age']
    # gender_from_form = request.POST['gender']
    # print(name_from_form)
    # print(email_from_form)
    # context = {
    #     "name_on_template" : name_from_form,
    #     "email_on_template" : email_from_form,
    #     "age_on_template" : age_from_form,
    #     "gender_on_template" : gender_from_form
    # }
    return redirect("/success")

def success(request):
    return render(request, "success.html")

