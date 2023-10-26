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
        let filteredData = performSearch(results, inputValue);
        showResults(filteredData)
    });
  })
  .catch(error => {
    console.error('Ocurrió un error:', error);
  });
})



function showResults(results) {
        var resultsHtml = '';
        for (var i = 0; i < results.length; i++) {
            resultsHtml += '<li>' +
                '<p>' + results[i].fields.name + '</p>' +
                '<p>$' + results[i].fields.cost + '</p>' +
                '<form method="post" action="{% url "update_one_product" %}">' +
                '{% csrf_token %}' +
                '<input type="hidden" name="id" value="' + results[i].pk + '">' +
                '<button class="button" type="submit">Editar</button>' +
                '</form>' +
                '<form method="post" action="{% url "delete_one_product" %}">' +
                '{% csrf_token %}' +
                '<input type="hidden" name="id" value="' + results[i].pk + '">' +
                '<button class="button" type="submit">Eliminar</button>' +
                '</form>' +
                '</li>';
        }

        $('#search-results').html('<ul class="products-list">' + resultsHtml + '</ul>');
    };

function performSearch(data, searchValue){

    searchValue = searchValue.toLowerCase();
    return data.filter(objeto => objeto.fields.name.toLowerCase().includes(searchValue));
}
