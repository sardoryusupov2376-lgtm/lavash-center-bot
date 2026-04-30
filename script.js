// TODO: Mini App JavaScript

// Telegram WebApp API
const tg = window.Telegram.WebApp;

// Initialize
let cart = [];
let currentCategory = 'lavash';
let userData = {};

// Get user data from Telegram
if (tg.initDataUnsafe?.user) {
    userData = tg.initDataUnsafe.user;
    console.log('User:', userData);
}

// TODO:
// 1. Categories yuklash
// 2. Products yuklash
// 3. Cart management
// 4. Checkout flow
// 5. Location selection (Google Maps)
// 6. Payment integration

window.addEventListener('load', () => {
    console.log('Mini App loaded');
    // tg.ready();
});