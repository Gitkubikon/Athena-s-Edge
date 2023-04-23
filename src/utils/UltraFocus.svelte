<script lang="ts">
  import { onUltraMount, createElement } from "./shenanigans";
  import { functions } from "./functions";
  import { elementsStore } from "../store";

  interface Point {
    x: number;
    y: number;
  }

  let current: HTMLElement = createElement("div", {});
  let mouse: Point = { x: 27.5, y: 150 };
  // let elements: Element[] = [];
  $: elements = $elementsStore;

  let trailer: HTMLElement;

  let currentTouchElement: HTMLElement | null = null;

  onUltraMount(() => {
    const trailer = document.getElementById("trailer"); // Replace "trailer" with the actual ID of your trailer element

    trailer.style.cursor = "none";
    if ("ontouchstart" in window || navigator.maxTouchPoints) {
      addEventListener("touchend", handleTouchClick);
      document.body.style.cursor = "default";
      trailer.style.scale = "0";
    } else {
      document.addEventListener("mousedown", handleClick);
      document.body.style.cursor = "none";
      trailer.style.visibility = "visible";
      document.addEventListener("mousemove", updateMousePosition);

      // Add event listeners for mouseout and mouseover events on the window object
      window.addEventListener("mouseout", handleMouseOut);
      window.addEventListener("mouseover", handleMouseOver);
    }
    requestAnimationFrame(onEnter);
  });

  // Define event handler for mouseout
  function handleMouseOut(event) {
    const trailer = document.getElementById("trailer"); // Replace "trailer" with the actual ID of your trailer element
    trailer.style.scale = "0";
  }

  // Define event handler for mouseover
  function handleMouseOver(event) {
    const trailer = document.getElementById("trailer"); // Replace "trailer" with the actual ID of your trailer element
    trailer.style.scale = "1";
  }

  // function handlePointerClick(event): void {
  //   const elements: Element[] = Array.from(
  //     document.elementsFromPoint(mouse.x, mouse.y)
  //   );
  //   const divElements: HTMLDivElement[] = elements.filter(
  //     (el) => el.tagName === "DIV"
  //   ) as HTMLDivElement[];
  //   const classList = divElements[0].classList;
  //   const functionClass = [...classList].find((c) => c.startsWith("function:"));

  //   if (functionClass) {
  //     const Function = functionClass.split(":")[1];
  //     const FunctionWithSpaces = functionClass.split(":").slice(1).join(":");
  //     const FunctionName = FunctionWithSpaces.split("(")[0];
  //     const Input = FunctionWithSpaces.split("(")[1]?.split(")")[0];
  //     functions[FunctionName](Input);

  //     console.log("Input : ", Input, " Name : ", FunctionName, " Function : ", FunctionWithSpaces)
  //   } else {
  //     // Check if this function was called by the click event on divElements[0]
  //     if (event.target !== divElements[0]) {
  //       divElements[0].click();
  //     }
  //   }
  // }

  function handleTouchClick(event: TouchEvent): void {
    const touch = event.changedTouches[0];
    const elements: Element[] = Array.from(
      document.elementsFromPoint(touch.clientX, touch.clientY)
    );
    const divElements: HTMLDivElement[] = elements.filter(
      (el) => el.tagName === "DIV"
    ) as HTMLDivElement[];
    const classList = divElements[0].classList;
    const functionClass = [...classList].find((c) => c.startsWith("function:"));

    // Remove 'current' from the previous element
    if (currentTouchElement) {
      currentTouchElement.classList.remove("current");
    }

    if (functionClass) {
      const functionName = functionClass.split(":")[1];
      console.log(functionName);
      functions[functionName]();
    }
    if (classList.contains("ultrafocus")) {
      divElements[0].classList.add("current");
      currentTouchElement = divElements[0];
    } else {
      divElements[0].click();
    }
  }

  function handleClick(event: MouseEvent): void {
    const rect = trailer.getBoundingClientRect();
    const x = rect.left + rect.width / 2;
    const y = rect.top + rect.height / 2;
    const elements: Element[] = Array.from(document.elementsFromPoint(x, y));
    const divElements: HTMLDivElement[] = elements.filter(
      (el) => el.tagName === "DIV"
    ) as HTMLDivElement[];
    const classList = divElements[0].classList;
    const functionClass = [...classList].find((c) => c.startsWith("function:"));

    if (functionClass) {
      const functionName = functionClass.split(":")[1];
      functions[functionName]();
    } else {
      // Check if this function was called by the click event on divElements[0]
      if (event.target !== divElements[0]) {
        divElements[0].click();
      }
    }
  }

  function updateMousePosition(event: MouseEvent) {
    mouse.x = event.pageX;
    mouse.y = event.pageY;
  }

  function getNearestPointerElement(event: Point): {
    distance: number;
    newCurrent: HTMLDivElement;
  } {
    let newCurrent: HTMLDivElement;
    let distance = Infinity;
    elements.forEach((element: HTMLDivElement) => {
      const rect = element.getBoundingClientRect();
      const x = rect.left;
      const y = rect.top;
      const width = rect.width;
      const height = rect.height;
      const cursorX = event.x;
      const cursorY = event.y;
      const xDistance = Math.max(x - cursorX, 0, cursorX - (x + width));
      const yDistance = Math.max(y - cursorY, 0, cursorY - (y + height));
      const newDistance = Math.sqrt(xDistance ** 2 + yDistance ** 2);
      if (newDistance < distance) {
        distance = newDistance;
        newCurrent = element;
      }
    });
    return { distance, newCurrent: newCurrent! };
  }

  function onEnter() {
    if (!trailer) return;
    requestAnimationFrame(onEnter);
    const result = getNearestPointerElement(mouse);
    if (
      current.classList.contains("current") &&
      current !== result.newCurrent
    ) {
      current.classList.remove("current");
      // current.style.transition = "";
      return;
    }
    if (result.distance < 34) {
      trailer.style.transition = "none";
      current.style.transition = "all 0.2s cubic-bezier(0, 0.2, 0,1)";
      if (current?.classList.contains("zone")) {
        trailer.style.left = `${mouse.x}px`;
        trailer.style.top = `${mouse.y}px`;
        trailer.style.transform = "scale(1.3)";
      } else {
        trailer.style.transition = "all 0.2s cubic-bezier(0, 0.2, 0,1)";
        const parent = current?.parentNode as Element;
        if (parent == undefined) return;
        const parentRect = parent.getBoundingClientRect();
        const currentRect = current.getBoundingClientRect();
        const centerX =
          currentRect.left + currentRect.width / 2 - parentRect.left;
        const centerY =
          currentRect.top + currentRect.height / 2 - parentRect.top;
        const newTop = centerY - trailer.offsetHeight / 2 + parentRect.top;
        const newLeft = centerX - trailer.offsetWidth / 2 + parentRect.left;
        trailer.style.top = `${newTop}px`;
        trailer.style.left = `${newLeft}px`;
        trailer.style.transform = "scale(1.6)";
      }
      result.newCurrent.classList.add("current");
      current = result.newCurrent;
    } else {
      // trailer.style.left = `${
      //   trailer.offsetLeft +
      //   (mouse.x - trailer.offsetLeft - trailer.offsetWidth / 2) * 1
      // }px`;
      // trailer.style.top = `${
      //   trailer.offsetTop +
      //   (mouse.y - trailer.offsetTop - trailer.offsetHeight / 2) * 1
      // }px`;
      trailer.style.transition = "none";
      trailer.style.left = `${mouse.x}px`;
      trailer.style.top = `${mouse.y}px`;

      trailer.style.transform = "scale(1)";
      current = result.newCurrent;
    }
  }
</script>

<div id="trailer" bind:this={trailer} />

<style>
  #trailer {
    overflow: none !important;
    display: block;
    border: 2px solid var(--ctp-mauve);
    background-color: var(--ctp-base);
    height: 10px;
    width: 10px;
    border-radius: 6.43px;
    position: fixed;
    z-index: 99000;
    pointer-events: none;
    transition: scale 1000ms ease;
  }
</style>
