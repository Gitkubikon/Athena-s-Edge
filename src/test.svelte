<script lang="ts">
  interface Point {
    x: number;
    y: number;
  }

  let mouse: Point = { x: 27.5, y: 150 };

  let prevMouseX = null;
  let prevMouseY = null;
  let prevTime = null;

  // create 5 trailer elements
  let trailers = [];
  for (let i = 0; i < 200; i++) {
    const trailer = document.createElement("div");
    trailer.classList.add("trail");
    document.body.appendChild(trailer);
    trailers.push(trailer);

    // Add event listener to trigger the animation on this trailer element
    trailer.addEventListener("mousemove", (event) => {
      console.log("mousemove")
      const x = event.clientX - trailer.offsetWidth / 2,
        y = event.clientY - trailer.offsetHeight / 2;

      const keyframes = {
        transform: `translate(${x}px, ${y}px)`,
      };

      trailer.animate(keyframes, {
        duration: 800,
        fill: "forwards",
      });
    });
  }

  function updateMousePosition(event: MouseEvent) {
    mouse.x = event.pageX;
    mouse.y = event.pageY;
    // Get the current mouse position and time
    const mouseX = event.clientX;
    const mouseY = event.clientY;
    const time = Date.now();

    // If this is the first mousemove event, set the previous values to the current ones
    if (prevMouseX === null && prevMouseY === null && prevTime === null) {
      prevMouseX = mouseX;
      prevMouseY = mouseY;
      prevTime = time;
      return;
    }

    // Calculate the distance and time difference between the current and previous positions
    const deltaX = mouseX - prevMouseX;
    const deltaY = mouseY - prevMouseY;
    const deltaTime = time - prevTime;

    // Calculate the velocity as pixels per second
    const velocityX = (deltaX / deltaTime) * 1000; // Multiply by 1000 to convert from milliseconds to seconds
    const velocityY = (deltaY / deltaTime) * 1000;
    // Calculate the direction as an angle in radians
    const velocity = Math.sqrt(velocityX ** 2 + velocityY ** 2);
    console.log(velocity)
    const maxDistance = 0.09;
    const minDistance = 0.009;
    let distance =
      minDistance + (maxDistance - minDistance) * Math.exp(velocity / 4000);
    // Calculate the direction as an angle in radians
    const direction = Math.atan2(deltaY, deltaX);

    // update the position and scale of the trail elements
    for (let i = 0; i < 200; i++) {
      const trailer = trailers[i];
      const offset = (i + 1) * -distance;
      const scale = i / 90; // scale the first element to 0 and linearly scale the rest up to 1
      const x = mouse.x + offset * Math.cos(direction);
      const y = mouse.y + offset * Math.sin(direction);
      trailer.style.transform = `translate(${x}px, ${y}px) scale(${scale})`;
      const keyframes = {
        transform: `translate(${x}px, ${y}px) scale(${scale})`,
      };
      trailer.animate(keyframes, {
        duration: 100,
        fill: "forwards",
      });
    }

    // Store the current position and time as the previous values for the next event
    prevMouseX = mouseX;
    prevMouseY = mouseY;
    prevTime = time;
  }

  // Add event listener to update mouse position
  document.addEventListener("mousemove", updateMousePosition);
</script>


<style>
  #trailer {
    height: 20px;
    width: 20px;
    background-color: white;
    border-radius: 20px;

    position: fixed;
    left: 0;
    top: 0;
    z-index: 10000;

    pointer-events: none;
    opacity: 1;
    transition: opacity 500ms ease;
  }
</style>
