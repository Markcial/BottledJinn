{% macro field(name, type, label, value='') -%}
{% if type == 'text' %}
{{input(name,placeholder=label,label=label,value=value)}}
{% elif type == 'email' %}
{{email_input(name,placeholder=label,label=label,value=value)}}
{% elif type == 'url' %}
{{url_input(name,placeholder=label,label=label,value=value)}}
{% elif type == 'currency' %}
{{currency_input(name,placeholder=label,label=label,value=value)}}
{% elif type == 'textarea' %}
{{textarea(name,placeholder=label,label=label,value=value)}}
{% elif type == 'richtext' %}
{{richtext(name,placeholder=label,label=label,value=value)}}
{% endif %}
{%- endmacro %}

{% macro input(name, value='', type='text', placeholder='Insert text here…', label=False, attrs={} ) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{label}}</label>{% endif %}
	<input type="{{type}}" value="{{value|e}}" name="{{name}}" placeholder="{{placeholder}}" id="{{name}}" {%for (k,v) in attrs.iteritems()%}{{k}}="{{v}}"{%endfor%} />
	</p>
{%- endmacro %}

{% macro email_input(name, value='', placeholder='Insert text here…', label=False, attrs={} ) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{label}}</label>{% endif %}
	<div class="input-prepend">
	<span class="add-on">@</span>
	<input type="email" value="{{value|e}}" name="{{name}}" placeholder="{{placeholder}}" id="{{name}}" {%for (k,v) in attrs.iteritems()%}{{k}}="{{v}}"{%endfor%} />
	</div>
	</p>
{%- endmacro %}

{% macro url_input(name, value='', placeholder='Insert text here…', label=False, attrs={} ) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{label}}</label>{% endif %}
	<div class="input-prepend">
	<span class="add-on">http://</span>
	<input type="email" value="{{value|e}}" name="{{name}}" placeholder="{{placeholder}}" id="{{name}}" {%for (k,v) in attrs.iteritems()%}{{k}}="{{v}}"{%endfor%} />
	</div>
	</p>
{%- endmacro %}

{% macro number_input(name, value='', placeholder='Insert text here…', label=False, attrs={} ) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{label}}</label>{% endif %}
	<input type="text" role="spinner" value="{{value|e}}" name="{{name}}" placeholder="{{placeholder}}" id="{{name}}" {%for (k,v) in attrs.iteritems()%}{{k}}="{{v}}"{%endfor%} />
	<script type="text/javascript">$("#{{name}}").spinner();</script>
	</p>
{%- endmacro %}

{% macro currency_input(name, value='', placeholder='Insert text here…', label=False, attrs={} ) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{label}}</label>{% endif %}
	<div class="input-prepend">
	<span class="add-on">€</span>
	<input type="text" value="{{value|e}}" name="{{name}}" placeholder="{{placeholder}}" id="{{name}}" {%for (k,v) in attrs.iteritems()%}{{k}}="{{v}}"{%endfor%} />
	</div>
	</p>
{%- endmacro %}

{%- macro textarea(name, value='', placeholder='Insert text here…', rows=10, cols=40, label=False) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{placeholder}}</label>{% endif %}
	<textarea name="{{name}}" id="{{name}}" rows="{{rows}}" cols="{{cols}}" placeholder="{{placeholder}}">{{ value|e }}</textarea>
	</p>
{%- endmacro %}

{%- macro richtext(name, value='', placeholder='Insert text here…', rows=10, cols=40, label=False) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{placeholder}}</label>{% endif %}
	<textarea name="{{name}}" id="{{name}}" rows="{{rows}}" cols="{{cols}}" placeholder="{{placeholder}}">{{ value|e }}</textarea>
	<script type="text/javascript">CKEDITOR.replace( "{{name}}", {toolbar:"Basic"} );</script>
	</p>
{%- endmacro %}

{%- macro select(name, choices={0:"none"}, value='', placeholder="Select item..." ) -%}
	<label for="{{name}}">{{placeholder}}</label>
	<select name="{{name}}" id="{{name}}">
	{% for choice in choices %}
		<option value="{{choice}}"{%- if value == choice -%} selected="selected"{%- endif %}>{{choices[choice]}}</option>
	{% endfor %} 
	</select>
{%- endmacro %}

{%- macro choices_radio(name, choices={0:"none"}, value=0 ) -%}
	{% for choice in choices %}
	<p class="input-container">
		{{ choices[ choice ]}} :
		<input type="radio" name="{{name}}" value="{{choice}}"{%- if choice == value -%} checked="checked"{%- endif %} />
	</p>
	{% endfor %}
{%- endmacro %}

{%- macro choices_checkbox(name, choices={0:"none"}, value=[0] ) -%}
	{% for choice in choices %}
	<p class="input-container">
		{{ choices[ choice ]}} :
		<input type="checkbox" name="{{name}}" value="{{choice}}"{%- if choice in value -%} checked="checked"{%- endif %} />
	</p>
	{% endfor %}
{%- endmacro %}