from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import date, datetime, timedelta
# Create your views here.
import openai
from Chat.models import BotAi, Asker, Askerbody, Botbody
from django.contrib.auth import logout

# Set up the OpenAI API client
openai.api_key = "API KEY" # I had to remove the original API key for security

# Set up the model and prompt
model_engine = "text-davinci-003"


def myAi(request):
    # if 'id' in request.session:
    Qu_ = ['q', 'quitew', 'Quite', 'exit', 'Exit']
    if request.method == 'POST':
        prompt = request.POST.get('ques')
        if prompt in Qu_:
            logout(request)

        else:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )

            response = completion.choices[0].text.strip()
            # print(response)
            # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            if request.user.is_authenticated:
                user = request.user
                ask, _ = Asker.objects.get_or_create(user=user)
                Askq = Askerbody.objects.create(asker=ask, body=prompt)
                Askq.save()

                bot, _ = BotAi.objects.get_or_create(user=user)
                BotAn = Botbody.objects.create(bot=bot, BotAns=response)
                BotAn.save()

                userq = Asker.objects.get(user=user)
                userqs = Askerbody.objects.filter(
                    asker=userq, Date=date.today())
                botdata = BotAi.objects.get(user=user)
                botdatas = Botbody.objects.filter(
                    bot=botdata, Date=date.today())
                ###########################################################################
                # LastSevenday = datetime.today()-timedelta(days=7)
                userd = Askerbody.objects.filter(
                    asker=userq, Date=date.today())
                mylis = zip(userqs, botdatas)
                print(prompt)
                print(response)

                return render(request, 'Home/main2.html', {"list": mylis, "user": user, "askdata": userd})


def home(request):

    return render(request, 'Home/home.html')


def clearAsk(request):
    if request.user.is_authenticated:
        user = request.user
        userq = Asker.objects.get(user=user)
        userd = Askerbody.objects.filter(asker=userq, Date=date.today())
        botdata = BotAi.objects.get(user=user)
        botdatas = Botbody.objects.filter(bot=botdata, Date=date.today())
        if userd:

            userd.delete()
            botdatas.delete()
            return HttpResponseRedirect('/main/')


def home2(request):
    if request.user.is_authenticated:
        try:
            yesrterday = datetime.today()-timedelta(days=7)
            user = request.user
            userq = Asker.objects.get(user=user)
            userd = Askerbody.objects.filter(asker=userq, Date=yesrterday)
            userd.delete()
            botdata = BotAi.objects.get(user=user)
            botdatas = Botbody.objects.filter(bot=botdata, Date=yesrterday)
            botdatas.delete()

        except:
            print("ERROR")

        user = request.user
        userq = Asker.objects.get(user=user)
        userd = Askerbody.objects.filter(asker=userq, Date=date.today())

        return render(request, 'Home/main.html', {'user': user, "askdata": userd})

    else:
        return HttpResponseRedirect('/acc/accounts/login/')
