{% extends "base.tpl" %}
{% block title %}Bottled Jinn Dashboard{% endblock %}
{% block body_classes%}{{super()}} model_edit{% endblock %}
{% block content %}
<form action="{{post_action}}">
	
</form>
{% include "admin/fields.tpl" %}
{% endblock %}