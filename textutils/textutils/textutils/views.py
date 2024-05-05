# I have created this File - Rayan
from django.http import HttpResponse
from django.shortcuts import render     # For templates

# Code till Video 6

# def index(request):
#     return HttpResponse("HOME PAGE!")


# def about(request):
#     return HttpResponse("<h1> This is About me </h1>")

# def myviewfile(request):
#     try:
#         file = open("./file.txt", "r")
#         data = file.read()
#     except:
#         data = "<h2> File does not exists in current director </h2>"

#     return HttpResponse(data)

# # HomeWorkd:: Personal Navigator
# def facebook(request):
#     content = '''<h1> Facebook </h1> <a href="https://www.facebook.com/campaign/landing.php?campaign_id=1653377901&extra_1=s%7Cc%7C318307045135%7Ce%7Cfacebook%27%7C&placement=&creative=318307045135&keyword=facebook%27&partner_id=googlesem&extra_2=campaignid%3D1653377901%26adgroupid%3D65139789042%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-362360550869%26loc_physical_ms%3D1011082%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMI0tj_46rx_QIVB8jVCh1F0QodEAAYASAAEgLemvD_BwE"> go to Facebook Page </a>'''

#     return HttpResponse(content)


# def cwhDjango(request):
#     content = '''<h1> Django Course </h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> go to Django Course </a> '''

#     return HttpResponse(content)


# Code for Video 7 (Laying the pipeline)

# def index(request):
#     content = '''<h1> Home </h1> <a href="http://127.0.0.1:8000/removepunc"> Remove Punctuation </a> <br> <a href="http://127.0.0.1:8000/capitalizefirst/"> Capitalize First </a> <br> <a href="http://127.0.0.1:8000/newlineremove/"> Newline Remove </a> <br> <a href="http://127.0.0.1:8000/spaceremove/"> Space Remove </a> <br> <a href="http://127.0.0.1:8000/charcount/"> Char Count </a>'''
#     return HttpResponse(content)


# def removepunc(request):
#     return HttpResponse("<h1> Remove Punc </h1> <br> <a href='/'> Back </a>")


# def capfirst(request):
#     return HttpResponse("<h1> Capitalize First</h1> <br> <a href='/'> Back </a>")


# def newlineremove(request):
#     return HttpResponse("<h1> NewLine Remove</h1> <br> <a href='/'> Back </a>")


# def spaceremove(request):
#     return HttpResponse("<h1> Space Remove </h1> <br> <a href='/'> Back </a>")  


# def charcount(request):
#     return HttpResponse("<h1> Char Count </h1> <br> <a href='/'> Back </a>")  


# TEMPLATES
# def index(request):
#     return render(request, "index.html")  # 1st arg: request , 2nd arg: template name

# def moreRender(request):
#     params = {'name': 'Rayan', 'place': 'Gujrat'}   # Creating a dictionary

#     return render(request, "index.html", params)        # 3rd arg for render is returning the dictionary to template file

# TEST UTILS WEBSITE

# Text Utils Home Page
def index(request):
    return render(request, 'home.html')

    # return HttpResponse("Home")


# Analyze page
def analyze(request):
    # GET the analyze text
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check the Checkbox values
    remove_punc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # remove_punc = request.GET.get('removepunc', 'off')
    # fullcaps = request.GET.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # charcounter = request.GET.get('charcounter', 'off')

    purpose = ""
    # Check which Checkbox is on
    if remove_punc == 'on':
        punctuations1 = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyze_text = ""

        # Analyze the text
        for char in djtext:
            if char not in punctuations1:
                analyze_text = analyze_text + char

        purpose += "Remove Punctuations"
        djtext = analyze_text

        # arr = {'purpose': 'Remove Punctuations', 'analyze_text': analyze_text}
        # return render(request, 'analyze.html', arr)

    if fullcaps == 'on':
        analyze_text = ""

        # Analyze the text
        for char in djtext:
            analyze_text += char.upper()

        purpose += " | Changed to uppercase"
        djtext = analyze_text

        # arr = {'purpose': 'Changed to uppercase', 'analyze_text':analyze_text}
        # return render(request, 'analyze.html', arr)
    
    if newlineremover == 'on':
        analyze_text = ""

        # Analyze the text
        for char in djtext:
            if char != '\n' and char != '\r':
                analyze_text += char
            else:
                print("newLine")

        purpose += " | Removed New Lines"
        djtext = analyze_text

        # arr = {'purpose' : 'Removed New Lines', 'analyze_text': analyze_text}
        # return render(request, 'analyze.html', arr)
    
    if extraspaceremover == 'on':
        analyze_text = " "

        # Analyze the text
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyze_text += char

        purpose += " | Removed Extra Spaces"
        djtext = analyze_text

        # arr = {'purpose': 'Removed Extra Spaces', 'analyze_text' :analyze_text}
        # return render(request, 'analyze.html', arr)
    
    if charcounter == 'on':
        count = 0
        analyze_text = "\nYour string have total characters : "

        for char in djtext:
            count += 1

        analyze_text = analyze_text + str(count) + "\n"
        purpose += " | Character Counter"
        djtext += analyze_text
        analyze_text = djtext

        # arr = {'purpose': 'Character Counter', 'analyze_text' :analyze_text}
        # return render(request, 'analyze.html', arr)

    if (remove_punc != 'on' and fullcaps != 'on' and newlineremover != "on" and extraspaceremover != 'on' and charcounter != 'on'):
        return HttpResponse("ERROR:: Please select any Operation and Try Again...!")

    arr = {'purpose': purpose, 'analyze_text' :analyze_text}
    return render(request, 'analyze.html', arr)




