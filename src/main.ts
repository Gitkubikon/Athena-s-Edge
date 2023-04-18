import './app.css';
import App from './App.svelte';
import { API } from './utils/api';

export const api = new API(`${window.location.protocol}//${window.location.hostname}`)

const app = new App({
  target: document.getElementById('app'),
})

export default app
