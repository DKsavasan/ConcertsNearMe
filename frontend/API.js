< script type = "text/javascript" >
    var apiUrl = 'https://app.ticketmaster.com/discovery/v2/';
fetch(apiUrl).then(response => {
    return response.json();
}).then(data => {
    // Work with JSON data here
    console.log(data);
}).catch(err => {
    // Do something for an error here
    console.log(err);
}); <
/script>