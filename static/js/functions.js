/* custom functions */
function updateEntries(list, date=undefined) {
  var url = '/api/entries';
  if (date) {
    var date_start = new Date(new Date(date).setHours(0,0,0,0)).toISOString();
    var date_end = new Date(new Date(date).setHours(24,0,0,0)-1).toISOString();
    url += "?date_start="+date_start+"&date_end="+date_end
  }
  nanoajax.ajax({url: url, method: 'GET'}, function (code, responseText, request) {
    if (code == 200) {
      list.clear();
      list.add(JSON.parse(responseText).entries);
    }
  })
}