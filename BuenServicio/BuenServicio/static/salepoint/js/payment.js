$(document).ready(function(){
    $('.discount-input').on('input', function() {
        const inputValue = $(this).val();
        performSearch(results, inputValue);
    });
  })
  .catch(error => {
    console.error('Ocurrió un error:', error);
  });



function showResults(results) {
        var resultsHtml = '';
        console.log(results)
        for (var i = 0; i < results.length; i++) {
            resultsHtml += '<tr class="result-item" id="' + results[i].pk + '">' +
            '<input type="hidden" name="id" value="' + results[i].pk + '">' +
            '<td>' + results[i].fields.name + '</td>' +
            '<td>$' + results[i].fields.cost + '</td>' +
            '<td><input name="quantity" type="number" value="0" min="0"></td>' +
            '</tr>';
        }

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
