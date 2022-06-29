# Getting started with Django
Django is a free and open source web framework.
### Installing Django
Using conda
<pre>conda install django</pre>
Using pip
<pre>pip install django</pre>

### Django CL tool
we can create our first project with 
<pre>django-admin startproject first_project</pre>
we will get a directory of files now
<br>
<pre>
<strong>first project</strong>
<ul>
<li>__init__.py</li>
<li>settings.py</li>
<li>urls.py</li>
<li>wsgi.py</li>
</ul>
<strong>manage.py</strong>
</pre>
we can run the server using manage.py--
<pre>python3 manage.py runserver</pre>

## <a href="first_project">Creating First App</a>
We can create a simple application with 
<pre>python3 manage.py startapp first_app</pre>
for more click here--- <a href="first project">creating a simple hello world app on django.</a>