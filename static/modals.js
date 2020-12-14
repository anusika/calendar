$(document).ready(function() {
  
  $('#deleteModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var name = button.data('name') // Extract info from data-* attributes
  var id = button.data('id')
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.assignmentName').text(name)
  modal.find('.assignmentId').text(id)
  document.getElementById("toDelete").value = id;
});

$('#editModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var courseCode = button.data('coursecode')
  var courseName = button.data('coursename')
  var assignmentName = button.data('assignmentname')
  var due = button.data("due")
  var points = button.data("points")
  var id = button.data("assignmentid")
  var submitted = button.data("submitted")

  if (due == "None") {
      due = new Date()
  }

  else {
    due = new Date(due)
    due = due.toString().split('GMT')
    due = new Date(due.toString().split('GMT')[0]+' UTC').toISOString().split('.')[0]
  }


  var modal = $(this)
  modal.find('#points').val(points);
  modal.find("#courseCode").val(courseCode).change();
  modal.find("#assignmentName").val(assignmentName).change();
  modal.find("#dueDate").val(due).change();
  modal.find("#submitStatus").val(submitted).change();
  document.getElementById("assignmentId").value = id;
})


$('.tasks-btn').bind("click", function() {
    var id = $(this).attr('data-id') 
    $.getJSON($SCRIPT_ROOT + '/_findtasks', {
      assignmentId: id
    }, function(data) {
      $("#tasks").empty();
      for (var i = 0; i < data.tasks.length; i++)
      {
        if(i == 0)
        {
          $("#tasks").append("<tr> <th> task </th> <th> status </th> <tr>")
        }
        $("#tasks").append("<tr><td>" + (data.tasks)[i][0] + "</td><td>" + (data.tasks)[i][1] + "</td></tr>")
      }
    });
    return false;
  });

  
});