$(document).ready(function(){
    const url = '/products/search-products/';
fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    var results = JSON.parse(data.products);
    showResults(results)
    return results
  }).then(results => {
    $('#search-input').on('input', function() {
        const inputValue = $(this).val();
        performSearch(results, inputValue);
        //showResults(filteredData)
    });
  })
  .catch(error => {
    console.error('Ocurrió un error:', error);
  });
})



function showResults(results) {
        var resultsHtml = '';
        console.log(results)
        for (var i = 0; i < results.length; i++) {
            resultsHtml += '<tr class="result-item" id="' + results[i].pk + '">' +
            '<td>' + results[i].fields.name + '</td>' +
            '<td>$' + results[i].fields.cost + '</td>' +
            '<td> <a href="/products/updateoneproduct/'+ results[i].pk +'">Editar</a>' +
            '<a onclick="return confirm('+ "'Seguro que deseas eliminar el producto?'" +')" href="/products/deleteoneproduct/'+ results[i].pk +'">Eliminar</a> </td>'}

        $('#search-results').html(resultsHtml);
    };

    function performSearch(data, searchValue) {
      searchValue = searchValue.toLowerCase();
      data.forEach(function(item) {
        var element = document.getElementById(item.pk);
        
        if (element) {
          if (item.fields.name.toLowerCase().includes(searchValue)) {
            element.style.display = '';
          } else {
            element.style.display = 'none';
          }
        }
      });
    }
