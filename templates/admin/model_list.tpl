{% extends "admin/dashboard.tpl" %}
{% import 'macros/forms.tpl' as forms %}
{% block title %}Bottled Jinn Dashboard{% endblock %}
{% block body_classes%}{{super()}} model_edit{% endblock %}
{% block container %}
	<div class="span3">
		{% include "admin/quicknav.tpl" %}
	</div><!--/span-->
	<div class="span9">
		<table class="table table-bordered table-striped">
			<caption>Hola</caption>
			<thead>
				<tr>
					{% for field in model.fields %}
					<th>{{field.name}}</th>
					{% endfor %}
				</tr>
			</thead>
			<tbody>
				{% for item in items %}
				<tr>
					{% for field in item.fields %}
					<td>{{field.value}}</td>
					{% endfor %}
				</tr>
				{% endfor %}
			</tbody>
		</table>
		{#
		<fieldset>
			<legend>Edit form</legend>
			<form id="editable_form" class="editable well" action="{{post_action}}" method="POST">
				<div id="form_content">
				{% for field in model.fields %}
				{{forms.field(field.name, type=field.type, label=field.label )}}
				{% endfor %}
				</div>
				<hr />
				<button type="submit" class="btn btn-primary">Save changes</button>
				<button type="button" class="btn">Cancel</button>
			</form>
		</fieldset>
		#}
	</div>
{% endblock %}
