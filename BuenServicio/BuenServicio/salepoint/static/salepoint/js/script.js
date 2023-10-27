$(document).ready(function(){
    const url = 'products/search-products/';
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
        for (var i = 0; i < results.length; i++) {
            resultsHtml += '<li class="result-item" id="' + results[i].pk + '">' +
                '<p>' + results[i].fields.name + '</p>' +
                '<p>$' + results[i].fields.cost + '</p>' +
                '<input type="hidden" name="id" value="' + results[i].pk + '">' +
                '<input name="quantity" type="number">' +
                '</li>';
        }

        $('#search-results').html(resultsHtml);
    };

    function performSearch(data, searchValue) {
      searchValue = searchValue.toLowerCase();
      data.forEach(function(item) {
        var element = document.getElementById(item.pk);
        
        if (element) {
          if (item.fields.name.toLowerCase().includes(searchValue)) {
            element.style.display = 'block';
          } else {
            element.style.display = 'none';
          }
        }
      });
    }
