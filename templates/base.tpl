<!DOCTYPE html>
<html>
	<head>
		{% block head %}
		<meta http-equiv="Content-Type" content="text/html;encoding=utf8" />
		<meta charset="utf-8" />
		{% block styles %}
		<link rel="stylesheet" href="{{paths.css}}/reset.css" />
		<link rel="stylesheet" href="{{paths.css}}/style.css" />
		{% endblock %}
		<title>{% block title %}Bottled Jinn Framework{% endblock %}</title>
		{% endblock %}
	</head>
	<body class="{% block body_classes %}admin index{% endblock %}">
		<div id="content">
		{% block content %}{% endblock %}
		</div>
		<footer>
		{% block footer %}
		&copy; Copyright 2012 <a href="http://bottled-jinn.github.com/">Bottled Jinn</a>.
		{% endblock %} 
		</footer>
	</body>
</html>