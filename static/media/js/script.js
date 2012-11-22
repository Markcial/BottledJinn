/* Author:

*/

var Input = function(id, type){
	this.id = id;
	this.type = type;
	this.render = function()
	{
		var html = '<p>';
		html += '<input type="text" name="label[]" value="" placeholder="Label.." required />';
		html += '<input type="text" name="name[]" value="" placeholder="Name..." required />';
		html += '<input type="text" name="value[]" value="" placeholder="Value..." />';
		html += '<input type="hidden" name="type[]" value="'+this.type+'" />';
		html += '<input type="hidden" name="id[]" value="'+this.id+'" />';
		html += '<input type="hidden" name="order[]" value="'+Form.amount+'" />';
		html += '</p>';
		return html;
	}
}

var Form = {
	form:null,
	elms:[],
	amount:0,
	bind:function(form){
		this.form = form;
		Input.order = 0;
	},
	add:function(which){
		this.amount++;
		var inp = new Input(which+"-"+this.amount,which);
		$(this.form).append( inp.render() );
	}
}