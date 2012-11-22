{% extends "base.tpl" %}
{% block title %}Bottled Jinn Dashboard{% endblock %}
{% block body_classes%}{{super()}} dashboard{% endblock %}
{% block content %}

	<div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="{{url(urls.dashboard)}}">Bottled Jinn Dashboard</a>
          <div class="nav-collapse collapse">
            {#<ul class="nav">
              <li><a href="{{url(urls.models_design,model_name="demo")}}">Nuevo</a></li>
            </ul>#}
          </div><!--/.nav-collapse -->
		  <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="{{paths.base}}logout">Logout</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
	
	<div class="container-fluid" role="main">
		<div class="row-fluid">
			{%block container%}
			<div class="span3">
				{% include "admin/quicknav.tpl" %}
			</div><!--/span-->
			<div class="span9">
				{% for model in models%}
					<div class="model_definition">
						<h3>{{model.name}}</h3>
						<a href="{{url(urls.models_create,model_name=model.name)}}" title="edit {{model.name}}">{{model.name}}</a>
						<div class="repr">
							{{model.__json__()}}
						</div>
					</div>
				{% endfor %}
			</div>
			{%endblock%}
		</div>
		<hr />
		{% block footer %}
		<div id="footer">
			<div class="container">
				<p class="credit">&copy; Copyright 2012 <a href="http://markcial.github.com/BottledJinn/">Bottled Jinn</a>.</p>
			</div>
		</div>
		{% endblock %}
	</div>
{% endblock %}
