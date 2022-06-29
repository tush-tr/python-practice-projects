Create a first app
<pre>python3 manage.py startapp first_app</pre>
In settings.py
<pre>

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_app'  --- note this 
]

</pre>
we update the list of installed apps in the settings.py file, we added our first app that we have created.<br>
Then we will edit the views.py file 
Update what you want to show on the page.
<br>
Then open <a href="first_project/urls.py">url file</a> <br> 
import url 
<pre>from django.conf.urls import url</pre>
import your views file
<pre>from first_app import views</pre>
Then add your function from views file you want to show.
<pre>
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
]
</pre>
