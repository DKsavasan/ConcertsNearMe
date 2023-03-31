const form = document.querySelector('.form');
const genreInput = document.querySelector('.input-box:nth-of-type(1)');
const dateInput = document.querySelector('.input-box:nth-of-type(2)');
const priceInput = document.querySelector('.input-box:nth-of-type(3)');
const distanceInput = document.querySelector('.input-box:nth-of-type(4)');
const submitButton = document.querySelector('.submit-button');


//The values that will be transfered to the back-end
submitButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent form submission
  const genre = genreInput.value;
  const dateRange = dateInput.value;
  const maxPrice = priceInput.value;
  const maxDistance = distanceInput.value;
  console.log(genre, dateRange, maxPrice, maxDistance); // Do something with the values
});


//Function to retrieve the ZIP-CODE of the USER
const findMyState = () => {
  const status = document.querySelector('.status');

  const success = (position) => {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    const geoApiURL = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en'

    let zipcode;

    fetch(geoApiURL)
    .then(res => res.json())
    .then(data => {
      zipcode = data.postcode;
    })
    .then(() => {
      console.log(zipcode);
    });
    
  }

  const error = () => {
    status.textContent = "Unable";
  }

  navigator.geolocation.getCurrentPosition(success,error);
} 

document.querySelector(".location-button").addEventListener("click", findMyState);