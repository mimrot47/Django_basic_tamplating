from django.shortcuts import render
import datetime



# Create your views here.
def my_view(Requst):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hellow Gust !! Very Good '
    if h<12:
        msg=msg+'Morening'
    elif h<16:
        msg=msg+'Afternoon'
    elif h<21:
        msg=msg+'Evening'
    else:
        msg=msg+'night'

    sname="RK DIGITAL KEDARKHEDA "
    my_dict={'S_name':sname,'call':msg,'date':date}
    return render(Requst,'myapp/index.html',context=my_dict)
