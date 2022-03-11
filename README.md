# django docker starter

Quickly set up a Django project with a MySql database in Docker with a debugger attached in Visual Studio Code.<br>

<h2>Steps to run on your local machine</h2>
<p>*Requirements </p>
<ul>
  <li>Docker installed</li>
</ul>
<p><b>1.</b> Run docker-compose up -d --build</p>
<p><b>2.</b> Go to http://localhost:7000/ to view your Django application <br/> (https is not supported we expect you to use a proxyserver with a loadbalancer in production anyway)</p>
<p><b>2.1</b> this api supports swagger & redoc (http://localhost:7000/api/redoc/)</p>
<p><b>3.</b> Start developing</p>
<p><b>3.1</b> Start Run and Debug in Visual Studio Code for setting breakpoints</p>


<h2>Package Manager</h2>
<p>This project uses pipenv (pip install pipenv) for managing dependencies</p>
<p>To install a dependency run "pipenv install <package>"</p>
<p>To update django to the latest version run "pipenv update django"</p>

<h2>Add app to project</h2>
<p>Dependecies for MySql run inside the docker container</p>
<p>To add a project you have to use the shell inside the container "docker exec -it <container-id> /bin/bash"/p>
<p>Create a folder inside src/apps/<app-name> and run "python manage.py startapp <app-name> src/apps/<app-name>"</p>
