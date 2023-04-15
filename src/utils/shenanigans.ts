import { onMount } from 'svelte';
import { elementsStore } from '../store';

function getCookieValue(key: string): string | null {
  const cookies = document.cookie.split(";");
  for (let cookie of cookies) {
    const [cookieKey, cookieValue] = cookie.trim().split("=");
    if (cookieKey === key) {
      return decodeURIComponent(cookieValue);
    }
  }
  return null;
}

function setCookie(name: string, value: string | number, expirationDays: number = 1): void {
  const date = new Date();
  date.setTime(date.getTime() + expirationDays * 24 * 60 * 60 * 1000);
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${encodeURIComponent(value)};${expires};samesite=none;secure`;
}

function deleteCookie(name: string): void {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`; //samesite=none;secure;
}

function deleteAllCookies(): void {
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i];
    const [name] = cookie.trim().split("=");
    deleteCookie(name);
  }
}

function onUltraMount(fn: Function) {
  const wrappedFn = async () => {
    await fn();
    elementsStore.set(Array.from(document.getElementsByClassName("ultrafocus")));
  };
  onMount(wrappedFn);
}

function createElement(
  tag: string,
  options: { [key: string]: string }
): HTMLElement {
  const element = document.createElement(tag);

  for (const [key, value] of Object.entries(options)) {
    if (key === "style") {
      element.setAttribute(key, value);
    } else {
      element[key] = value;
    }
  }

  return element;
}
export {
  getCookieValue,
  setCookie,
  deleteCookie,
  deleteAllCookies,
  onUltraMount,
  createElement
}


