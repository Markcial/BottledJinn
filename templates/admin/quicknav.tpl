<div class="well sidebar-nav">
	<ul class="nav nav-list">
		<li class="nav-header">Create</li>
		<li><a href="{{url(urls.models_design)}}">Nuevo</a></li>
		<li class="nav-header">Read</li>
		{% for model in models %}
		<li><a href="{{url(urls.models_list, model_name=model.name)}}">{{model.name}} list</a></li>
		{% endfor %}
	</ul>
</div>