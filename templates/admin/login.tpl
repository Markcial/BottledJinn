{% extends "base.tpl" %}
{% import "macros/forms.tpl" as forms %}
{% block body_classes %}{{super()}} login{% endblock %}
{% block content %}
<fieldset>
	<legend>Login form</legend>
	<form action="{{login_url}}" method="POST">
		{{ forms.input('user', placeholder='Username…') }}
		{{ forms.input('password', type='password', placeholder='Password…') }}
		<p>
			<input type="submit" />
		</p>
	</form>
</fieldset>
{% endblock %}
