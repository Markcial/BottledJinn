{% extends "base.tpl" %}
{% import "macros/forms.tpl" as forms %}
{% block body_classes %}{{super()}} login{% endblock %}
{% block content %}
<div class="container">

	<form class="form-signin" action="{{login_url}}" method="POST">
		<h2 class="form-signin-heading">Please sign in</h2>
		{{ forms.input('user', placeholder='Username…',attrs={'class':'input-block-level'}) }}
		{{ forms.input('password', type='password', placeholder='Password…',attrs={'class':'input-block-level'}) }}
		<p>
			<button class="btn btn-large btn-primary" type="submit">Login</button>
		</p>
	</form>

</div>
{% endblock %}
