{% extends "admin/dashboard.tpl" %}
{% block title %}Bottled Jinn Dashboard{% endblock %}
{% block body_classes%}{{super()}} model_design{% endblock %}
{% block container %}
	<div class="span3">
		{% include "admin/fields.tpl" %}
	</div><!--/span-->
	<div class="span9">
		<fieldset>
			<legend>Design {{model_name}} Object</legend>
			<form id="editable_form" class="editable well" action="{{post_action}}" method="POST">
				<p>
					<label for="model_name">Model name</label>
					<input type="text" name="model_name" id="model_name" placeholder="Model name" required />
				</p>
				<div id="form_content">
				
				</div>
				<hr />
				<button type="submit" class="btn btn-primary">Save changes</button>
				<button type="button" class="btn">Cancel</button>
			</form>
			<script type="text/javascript">
			Form.bind( document.getElementById( 'form_content' ) );
			</script>
		</fieldset>
	</div>
{% endblock %}
