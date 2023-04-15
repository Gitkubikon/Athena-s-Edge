import './app.css';
import App from './App.svelte';
import { Api } from './utils/api';

export const api = new Api(`${window.location.protocol}//${window.location.hostname}`)

const app = new App({
  target: document.getElementById('app'),
})

export default app
