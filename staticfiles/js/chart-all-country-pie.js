data = {
    datasets: [{
        data: [10, 20, 30]
    }],

    labels: [
        'Red',
        'Yellow',
        'Blue'
    ]
};
// variabels
var ctx = document.getElementById('myChart').getContext('2d');

// country datas -chart
var countryDatasChart = new Chart(ctx, {
    type: 'pie',
    data: data,
    options: options
});