from django.http import HttpResponse

def personalNavigator(request):
    return HttpResponse('''
<h1>My Personal Navigator</h1>
<a href="https://www.google.com/">Google.com</a>                        
<a href="https://stackoverflow.com/">Stackoverflow</a>                        
<a href="https://www.quora.com/">quora</a>                        
<a href="https://www.wikipedia.org/">Wiki Pedia</a>                        

''')