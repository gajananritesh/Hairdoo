"use strict";

$("[data-checkboxes]").each(function() {
  var me = $(this),
    group = me.data('checkboxes'),
    role = me.data('checkbox-role');

  me.change(function() {
    var all = $('[data-checkboxes="' + group + '"]:not([data-checkbox-role="group_data_check"])'),
      checked = $('[data-checkboxes="' + group + '"]:not([data-checkbox-role="group_data_check"]):checked'),
      group_data_check = $('[data-checkboxes="' + group + '"][data-checkbox-role="group_data_check"]'),
      total = all.length,
      checked_length = checked.length;

    if(role == 'group_data_check') {
      if(me.is(':checked')) {
        all.prop('checked', true);
      }else{
        all.prop('checked', false);
      }
    }else{
      if(checked_length >= total) {
        group_data_check.prop('checked', true);
      }else{
        group_data_check.prop('checked', false);
      }
    }
  });
});

$("#table-1").dataTable({
  "columnDefs": [
    { "sortable": false, "targets": [2,3] }
  ]
});
$("#table-2").dataTable({
  "columnDefs": [
    { "sortable": false, "targets": [0,2,3] }
  ]
});
