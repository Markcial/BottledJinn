/**
 * Copyright (c) 2003-2012, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	config.language = 'es';
	config.skin = 'moono-light';
	// config.uiColor = '#AADC6E';
	config.toolbar_Basic = [
	{ name: 'basicstyles', items : [ 'Bold','Italic' ] },
	{ name: 'paragraph', items : [ 'NumberedList','BulletedList' ] },
	{ name: 'tools', items : [ 'Maximize','-','About' ] }
	];
};

