import './app.css';
import App from './App.svelte';
import { API } from './utils/api';
import { getPopularRedditTopics, getPopularTweets, getPopularInstagramPosts, getPopularHackerNewsPosts } from './utils/scrape';

export const api = new API(`${window.location.protocol}//${window.location.hostname}`)

// getPopularRedditTopics().then((posts) => {
//   console.log('Top Reddit posts:', posts);
// });

// getPopularTweets().then((posts) => {
//   console.log('Top Twitter posts:', posts);
// });

// getPopularInstagramPosts().then((posts) => {
//   console.log('Top Insta posts:', posts);
// });

// getPopularHackerNewsPosts().then((posts) => {
//   console.log('Top Hacker-News posts:', posts);
// });


const app = new App({
  target: document.getElementById('app'),


})

export default app
