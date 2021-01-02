# Virtual Environment in python
<p>A virtual environment is a tool that helps to keep 
dependencies required by different projects separate by creating
isolated python virtual environments for them. This is one of the 
most important tools that most of 
the Python developers use.</p>

## How to Create Python Virtual Environments on Linux
Starting from Python 3.6, the recommended way to create a virtual environment is to use the venv module.
<pre>$ sudo apt install python3-venv
</pre>
Switch to the directory where you would like to store your Python 3 virtual environments. Within the directory run the following command to create your new virtual environment:
<pre>$ python3 -m venv my-project-env
</pre>
To start using this virtual environment, you need to activate it by running the activate script:
<pre>$ source my-project-env/bin/activate</pre>
Once you are done with your work to deactivate the environment, simply type deactivate and you will return to your normal shell.
<pre>(venv) $ deactivate</pre>
## How to use virtual environment in windows
install virtual environment
<pre>>> pip install virtualenv </pre>
create a virtual environment
<pre>>> virtualenv my-project-env</pre>
activate a virtual environment
<pre>>> .\my-project-env\Scripts\activate</pre>
Here you can get error if you are getting error you can use this command
<pre>>> set executionpolicy remotesigned</pre>

## Requirements.txt file
requirements.txt file is used to specifying what python packages are required to run the
project you are looking out.
for creating a requirements.txt file --<br>
<pre>$ pip feeze > requirements.txt</pre>
when you have a requirements.txt file and you have to install all these packages into your environment
<pre>$ pip install -r requirements.txt</pre>
<strong>
<article>
If you want to create a new virtual environment in which all the packages are installed that are installed iny our system
<pre>virtualenv --system-site-packages name</pre>
</article></strong>
<br>

<footer>
Notes credits- 
<a href="https://www.geeksforgeeks.org/python-virtual-environment/">Geeks for geeks</a>,
<a href="https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/">linuxize</a>
,<a href="https://www.linkedin.com/in/tushar-r-849510116/">also me</a>
</footer>