<!doctype html>
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
	<head>
		{% block head %}
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		<title>{% block title %}Bottled Jinn Framework{% endblock %}</title>
		<meta name="description" content="{% block meta_description %}Generic meta description{% endblock %}">
		<meta name="viewport" content="width=device-width">
		{% block styles %}
		<link href="{{paths.css}}/bootstrap.min.css" rel="stylesheet" media="screen" />
		<link href="//code.jquery.com/ui/1.9.1/themes/base/jquery-ui.css" rel="stylesheet" media="screen" />
		<link href="{{paths.css}}/style.css" rel="stylesheet" media="screen" />
		{% endblock %}
		{% block scripts %}
		<script src="{{paths.js}}/libs/modernizr-2.5.3.min.js"></script>
		<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
		<script src="//code.jquery.com/ui/1.9.1/jquery-ui.js"></script>
		<script src="{{paths.js}}/libs/ckeditor/ckeditor.js"></script>
		<script>window.jQuery || document.write('<script src="{{paths.js}}/libs/jquery-1.7.1.min.js"><\/script>')</script>
		<script src="{{paths.js}}/plugins.js"></script>
		<script src="{{paths.js}}/bootstrap.min.js"></script>
		<script src="{{paths.js}}/script.js"></script>
		{% endblock %}
		{% endblock %}
	</head>
	<body class="{% block body_classes %}admin index{% endblock %}">
	<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->
		{% block content %}{% endblock %}
	</body>
</html>