# django docker starter

Quickly set up a Django project with a MySql database in Docker with a debugger attached <br>

<h2>Steps to run on your local machine</h2>
<p>1. Conditions </p>
<ul>
  <li>Docker installed</li>
</ul>
<p>2. Run docker-compose up -d --build</p>
<p>3. Go to http://localhost:7000/ to view your Django application <br/> (https is not supported we expect you to use a proxyserver with a loadbalancer in production anyway)</p>
<p>3.1 this api supports swagger & redoc (http://localhost:7000/api/redoc/)</p>
<p>4. Start developing</p>


<h2>Package Manager</h2>
<p>This project uses pipenv (pip install pipenv) for managing dependencies
<p>To install a dependency run "pipenv install <package>"
<p>To update django to the latest version run "pipenv update django"</p>


