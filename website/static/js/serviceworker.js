// self.addEventListener('install', function(event) {
//     console.log('Service Worker installed');
//     // Optionally, you can skip the waiting phase to activate immediately
//     self.skipWaiting();
// });

// self.addEventListener('activate', function(event) {
//     console.log('Service Worker activated');
//     event.waitUntil(clients.claim());  // Take control of the page immediately
// });

// // A simple fetch event to simulate caching
// self.addEventListener('fetch', function(event) {
//     console.log('Service Worker intercepting fetch request:', event.request.url);
//     // You can respond with a static file or just return the response as-is
//     // event.respondWith(
//     //     new Response('Service Worker response')
//     // );
// });

// // This variable will save the event for later use.
// let deferredPrompt;
// window.addEventListener('beforeinstallprompt', (e) => {
//   // Prevents the default mini-infobar or install dialog from appearing on mobile
//   e.preventDefault();
//   // Save the event because you'll need to trigger it later.
//   deferredPrompt = e;
//   // Show your customized install prompt for your PWA
//   // Your own UI doesn't have to be a single element, you
//   // can have buttons in different locations, or wait to prompt
//   // as part of a critical journey.
//   showInAppInstallPromotion();
// });