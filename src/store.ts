import { writable } from "svelte/store";

export const page = writable("Home");

export const elementsStore = writable([]);

export function updateElements() {
  elementsStore.set(Array.from(
    document.getElementsByClassName("ultrafocus")
  ))
}
