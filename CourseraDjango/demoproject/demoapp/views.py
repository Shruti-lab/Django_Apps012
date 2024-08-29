#https://www.programiz.com/html/form-action
from email.headerregistry import Address
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    content = f'''
      Status code: {HttpResponse.status_code},
      Content: {HttpResponse.content} ,
      Date & Time:{now}

    '''
    return HttpResponse(f"<h1>{content}</h2>")
    # return HttpResponse("hfyujn")

def home(request):
    return HttpResponse("<html><h1>Hello World!</h1></html>")

def pra1(request):
    path = request.path
    method = request.method
    content='''<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : "{}"</p> 
<p>Request Method :{}</p>
<h1>Status Code: {}</h1>
<p>Cookies: {}</p>
<p>User: {}</p>
<p>Files: {}</p>
<p>request.GET: {}</p>
<p>request.POST: {}</p>
<h3>You can add and vary the meta tags. to see it create some error in this file and scroll down on website</h3>
Username: {}<br>
{}</center>'''.format(path,method,HttpResponse.status_code,request.COOKIES,request.user,request.FILES,request.GET,request.POST,request.META['USERNAME'],request.META['HTTP_ACCEPT'])
    return HttpResponse(content)

# An important thing to understand here is the parameters added inside the path() function in the urls.py file must match the arguments added inside the pathview() view function associated with it in the views.py file.
def pathview(request,name,id,marks):  #getuser
    print(id,name)  #here id and name are string BUT MARKS IS INTEGER
    html = f'''<table><thead><tr>
    <th>ID</th>
    <th>NAME</th>
    <th>MARKS</th>
    </tr></thead>
    <tbody>
    <tr>
    <td>{id+'fghb'}</td>
    <td>{name}</td>
    <td>{marks+4*2}</td>
    </tr>
    </tbody>
    </table>'''
    response = HttpResponse(html)
    return response

def queryview(request):
    name = request.GET['name'] 
    id = request.GET['id'] 
    address = request.GET['address']  #Q) the variable 'address' and value inside GET['address'] must be same. why?
    return HttpResponse("Name:{}   UserID:{}   Address:{}".format(name, id,address)) 
# http://127.0.0.1:8000/demo/getdata/?name=Ashrita&id=1 Entire URL for above queryview

def showform(request):
    return render(request,"forms.html")

def getform(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name:{} UserID:{}".format(name, id))

def drinks(request,drink_name):
    return HttpResponse(drink_name)

def error(request):
    return HttpResponseBadRequest("404: Page not found")

# def error2(request):
#     return HttpResponse('404: pagee not found', status_code='404')

"""Query parameter
The client URL may contain a query string linked to the endpoint, for example, 
http://localhost:8000/getuser/?name=John&id=1

A query string is a sequence of one or more key=value pairs concatenated by the & symbol. Each key is the query parameter. The query string ends with the ? symbol after the URL endpoint.
Query strings are an alternative approach to URL parameters for adding URL configurations.

The URL dispatcher doesn’t parse these parameters. They are fetched by the view from the request object it receives. The request object’s GET property is a dictionary object. """

'''
The URL pattern treats the identifiers in angular brackets (<..>) as the path parameters. By default, it parses the received value to the string type. Other path converters available are:

str - Matches any non-empty string and excludes the path separator, '/'. This is the default if a converter isn’t included in the expression.

int - Matches zero or any positive integer and returns an int. For example:/customer/<int:id>

slug - Matches any slug string consisting of ASCII letters or numbers, including the hyphen and underscore characters.

uuid - Matches a formatted UUID.  For example: 075194d3-6885-417e-a8a8-6c931e272f00 and returns a UUID instance.

path - Matches any non-empty string and includes the path separator, '/'. '''



'''
from django.http import HttpResponse 
from django.template import loader 
def index(request): 
    template = loader.get_template('demoapp/index.html') 
    context={}  
    return HttpResponse(template.render(context, request))'''

'''
def drinks(request,drink_name):
    drink={
        'mocha':'type of coffee',
        'tea':'type of beverage',
        'lemonade':'type of refreshment',
        'mojito':'I love it'
    }
    choice_of_drink  = drink[drink_name]
    return HttpResponse( f"<h2> {drink_name} </h2>"+choice_of_drink)'''

'''from django.http import Http404, HttpResponse 
from .models import Product 

def detail(request, id): 
    try: 
        p = Product.objects.get(pk=id) 
    except Product.DoesNotExist: 
        raise Http404("Product does not exist") 
    return HttpResponse("Product Found") 
    
from django.http import HttpResponse 
def my_view(request): 
    # ... 
    if condition==True: 
        return HttpResponse('<h1>Page not found</h1>', status_code='404') 
    else: 
        return HttpResponse('<h1>Page was found</h1>')     '''

# Usually, the Django development server is in DEBUG mode, which shows the error's traceback instead of the exception.
# To render the custom exception message, the DEBUG variable in the project’s settings should be set to False. and ALLOWED_HOSTS = ['*']