const form = document.querySelector('.form');
const genreInput = document.querySelector('.input-box:nth-of-type(1)');
const dateInput = document.querySelector('.input-box:nth-of-type(2)');
const priceInput = document.querySelector('.input-box:nth-of-type(3)');
const distanceInput = document.querySelector('.input-box:nth-of-type(4)');
const submitButton = document.querySelector('.submit-button');

submitButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent form submission
  const genre = genreInput.value;
  const dateRange = dateInput.value;
  const maxPrice = priceInput.value;
  const maxDistance = distanceInput.value;
  console.log(genre, dateRange, maxPrice, maxDistance); // Do something with the values
});
