import { writable } from "svelte/store";

export const page = writable("Home");

export const content = writable("");

export const elementsStore = writable([]);

export const testApiDivs = writable([]);

export function updateElements() {
  elementsStore.set(Array.from(
    document.getElementsByClassName("ultrafocus")
  ))
}
