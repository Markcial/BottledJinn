/* Author:

*/

var Input = function(id, type){
	this.id = id;
	this.type = type;
	this.render = function()
	{
		var html = '<p>';
		html += '<input type="text" name="label[]" value="Label..." class="discrete" />';
		html += '<input type="text" id="'+this.id+'" name="name[]" value="Name" placeholder="Label..." />';
		html += '<input type="hidden" name="type[]" value="text" />';
		html += '</p>';
		return html;
	}
}
var EmailInput = function(id){
	this.id = id;
}
EmailInput.prototype.render = function(){
		var html = '<p>';
		html += '<input type="text" name="label[]" value="Label..." class="discrete" />';
		html += '<input type="text" id="'+this.id+'" name="name[]" value="Name" placeholder="Label..." />';
		html += '<input type="hidden" name="type[]" value="email" />';
		html += '</p>';
		return html;
}
var UrlInput = function(id){
	this.id = id;
}
UrlInput.prototype.render = function(){
		var html = '<label for="'+this.id+'">' + this.label + '</label>';
		html += '<div class="input-prepend">';
		html += '<span class="add-on"><i class="icon-globe"></i></span>';
		html += '<input type="text" id="'+this.id+'" name="'+this.name+'" placeholder="'+this.label+'" />';
		html += '</div>';
		return html;
}
var NumberInput = function(id,name,label){
	this.id = id;
	this.name = name;
	this.label = label;
}
NumberInput.prototype.render = function(){
		var html = '<label for="'+this.id+'">' + this.label + '</label>';
		html += '<input type="text" id="'+this.id+'" name="'+this.name+'" placeholder="'+this.label+'" />';
		html += '<script type="text/javascript">';
		html += '$("#'+this.id+'").spinner();';
		html += '</script>';
		return html;
}
var CurrencyInput = function(id,name,label){
	this.id = id;
	this.name = name;
	this.label = label;
}
CurrencyInput.prototype.render = function(){
		var html = '<label for="'+this.id+'">' + this.label + '</label>';
		html += '<div class="input-prepend">';
		html += '<span class="add-on">€</span>';
		html += '<input type="text" id="'+this.id+'" name="'+this.name+'" placeholder="'+this.label+'" />';
		html += '</div>';
		return html;
}
var TextareaInput = function(id,name,label){
	this.id = id;
	this.name = name;
	this.label = label;
}
TextareaInput.prototype.render = function(){
		var html = '<label for="'+this.id+'">' + this.label + '</label>';
		html += '<div class="input-prepend">';
		html += '<textarea id="'+this.id+'" name="'+this.name+'" placeholder="'+this.label+'"></textarea>';
		return html;
}
var RichtextInput = function(id,name,label){
	this.id = id;
	this.name = name;
	this.label = label;
}
RichtextInput.prototype.render = function(){
		var html = '<label for="'+this.id+'">' + this.label + '</label>';
		html += '<div class="input-prepend">';
		html += '<textarea role="editor" id="'+this.id+'" name="'+this.name+'" placeholder="'+this.label+'"></textarea>';
		html += '<script type="text/javascript">CKEDITOR.replace( "'+this.id+'", {toolbar:"Basic"} );</script>';
		return html;
}

var Form = {
	form:null,
	elms:[],
	amount:0,
	bind:function(form){
		this.form = form;
	},
	make:function(which){
		
	},
	add:function(which){
		this.amount++;
		var inp = new Input("text-"+this.amount,which);
		$(this.form).append( inp.render() );
	}
}