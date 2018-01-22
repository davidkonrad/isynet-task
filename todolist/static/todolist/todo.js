"use strict;"

var Todo = {
	loadTasks: function() {
		$.ajax({
			url: 'http://localhost:8000/tasks'
		}).done(function(renderedHtml) {
			$('#task-container').html(renderedHtml)
		})
	},
	create: function() {
		$('#modal-save').text('Save');
		$('#modal-title').text('Create new task');	
		$('#todo-title').val('');
		$('#todo-description').val('');
		Todo.showModal()
	},
	edit: function(id) {
		$.ajax({
			url: 'http://localhost:8000/item/'+id
		}).done(function(data) {
			$('#modal-save').text('Save changes');
			$('#modal-title').text('Edit task');	
			$('#todo-id').val(data[0].pk);
			$('#todo-title').val(data[0].fields.title);
			$('#todo-description').val(data[0].fields.description);
			Todo.showModal()
		})
	},
	solve: function(id) {
		$.ajax({
			url: 'http://localhost:8000/solve/'+id
		}).done(function() {
			Todo.loadTasks();
		})
	},
	remove: function(id) {
		if (confirm('Remove task?')) {
			$.ajax({
				url: 'http://localhost:8000/remove/'+id
			}).done(function() {
				$('#todo-task-'+id).fadeOut(500, function() {
					$(this).remove()
				})
			})
		}
	},
	save: function() {
		var data = $('#todo-form').serialize();
		$.ajax({
			url: 'http://localhost:8000/save/',
			data: data,
			dataType: 'json'
		}).done(function() {
			Todo.loadTasks()
		}).always(function() {
			Todo.closeModal();
		})
	},
	showModal: function() {
		$('#todo-modal').modal('show');
	},
	closeModal: function(message) {
		$('#todo-modal').modal('hide');
	}
};

Todo.loadTasks();

$('body').on('shown.bs.modal', '#todo-modal', function() {
  $('#todo-title').trigger('focus')
})

$(document).ajaxError(function() {
	console.error(arguments)
})


