{% extends "admin/dashboard.tpl" %}
{% import 'macros/forms.tpl' as forms %}
{% block title %}Bottled Jinn Dashboard{% endblock %}
{% block body_classes%}{{super()}} model_edit{% endblock %}
{% block container %}
	<div class="span3">
		{% include "admin/fields.tpl" %}
	</div><!--/span-->
	<div class="span9">
		<fieldset>
			<legend>Edit form</legend>
			<form id="editable_form" class="editable well" action="{{post_action}}" method="POST">
				<div id="form_content">
				{% for field in model.fields %}
				{{forms.field(field.name, type=field.type, label=field.label, value=field.value )}}
				{% endfor %}
				</div>
				<hr />
				<button type="submit" class="btn btn-primary">Save changes</button>
				<button type="button" class="btn">Cancel</button>
			</form>
		</fieldset>
	</div>
{% endblock %}
