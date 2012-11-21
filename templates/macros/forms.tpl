{% macro input(name, value='', type='text', placeholder='Insert text here…', label=False, attrs={} ) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{label}}</label>{% endif %}
	<input type="{{type}}" value="{{value|e}}" name="{{name}}" placeholder="{{placeholder}}" id="{{name}}" {%for (k,v) in attrs.iteritems()%}{{k}}="{{v}}"{%endfor%} />
	</p>
{%- endmacro %}

{%- macro textarea(name, value='', placeholder='Insert text here…', rows=10, cols=40, label=False) -%}
	<p class="input-container">
	{% if label %}<label for="{{name}}">{{placeholder}}</label>{% endif %}
	<textarea name="{{name}}" id="{{name}}" rows="{{rows}}" cols="{{cols}}" placeholder="{{placeholder}}">{{ value|e }}</textarea>
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