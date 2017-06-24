$(document).ready(function() {
   var orderTable = $('#mytable').DataTable({
   "bServerSide": true,
   "sAjaxSource": 'way_items',
   "bProcessing": true,
   "bLengthChange": true,
   "bFilter": true,
   'sDom': 'rtpli',
   "bSortable": false,  // change
   "autoWidth": true,
   "ordering": false,
   "bInfo": true,
   "lengthMenu": [[10, 25, 50, 100], [10, 25, 50, 100]],
   "iDisplayLength": 10,
   "aoColumnDefs": [

   ]

   });
});