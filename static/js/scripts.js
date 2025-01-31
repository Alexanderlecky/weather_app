document.addEventListener('DOMContentLoaded', function () {
    const locationInput = document.querySelector('input[name="location"]');
    locationInput.focus();

    // Dynamic background based on weather
    const weatherDescription = document.querySelector('.weather-results p:last-child');
    if (weatherDescription) {
        const description = weatherDescription.textContent.toLowerCase();
        const body = document.body;

        if (description.includes('clear')) {
            body.style.backgroundImage = "url('https://i.pinimg.com/736x/e3/39/7c/e3397c5557a5869e48d2138d9bfdce16.jpg')";
        } else if (description.includes('rain')) {
            body.style.backgroundImage = "url('https://i.pinimg.com/736x/4b/1f/04/4b1f04ffc3e2043494ffb62263abbf92.jpg')";
        } else if (description.includes('cloud')) {
            body.style.backgroundImage = "url('https://i.pinimg.com/736x/76/4e/a8/764ea83c9e875e4d6c9743f543af678c.jpg')";
        } else {
            body.style.backgroundImage = "url('https://i.pinimg.com/736x/a6/4c/f7/a64cf70f8ed017d44dbb5d88e80f9c63.jpg')";
        }
    }
});