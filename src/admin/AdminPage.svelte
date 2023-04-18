<script>
  import { testApiDivs } from "../store";
  import { onUltraMount } from "../utils/shenanigans";
  import {
    fade,
    fly,
    scale,
    draw,
    blur,
    slide,
    crossfade,
  } from "svelte/transition";

  onUltraMount(() => {});
</script>

<section
  transition:fly={{ y: -200 }}
  class="absolute left-0 flex flex-col justify-center"
>
  <div class=" pos terminal">
    <!-- <h1>{`${getCookieValue("user").toUpperCase()}'s CONSOLE`}</h1> -->
    <h1>CHAD'S CONSOLE</h1>
    <div class="buttons flex flex-wrap justify-between py-4 px-10">
      <div class="function:auth m-10 button ultrafocus font-semibold py-2 px-4">
        Authenticate
      </div>
      <div
        class="function:downPlan m-10 button ultrafocus font-semibold py-2 px-4"
      >
        Download Plan
      </div>
      <div class="function:lock m-10 button ultrafocus font-semibold py-2 px-4">
        Lock
      </div>
      <div class="function:list m-10 button ultrafocus font-semibold py-2 px-4">
        List
      </div>
      <div
        class="function:upload m-10 button ultrafocus font-semibold py-2 px-4"
      >
        Upload
      </div>
      <div
        class="function:download m-10 button ultrafocus font-semibold py-2 px-4"
      >
        Download
      </div>
      <div
        class="function:notify m-10 button ultrafocus font-semibold py-2 px-4"
      >
        Notify
      </div>
      <div
        class="function:timetable m-10 button ultrafocus font-semibold py-2 px-4"
      >
        Timetable
      </div>
      <div
        class="function:TestApi m-10 button ultrafocus font-semibold py-2 px-4"
      >
        Run API Test
      </div>
    </div>
    <div class="test-group">
      <div id="test-results">
        {#each $testApiDivs as testElement}
          {@html testElement.outerHTML}
        {/each}
      </div>
    </div>
  </div>
</section>

<style>
  h1 {
    font-size: 2em;
    font-weight: bold;
  }

  .pos {
    position: absolute;
    top: 0px;
  }

  .terminal {
    background-color: rgba(0, 0, 0, 0.55);
    padding: 50px;
    position: relative;
    margin-top: auto;
    margin-bottom: auto;
    margin-right: auto;
    margin-left: auto;
    border-radius: 20px;
  }

  .button {
    width: fit-content;
    margin: 10px;
    padding: 10px;
  }

  .buttons {
    /* flex flex-wrap justify-between py-4 px-10 */
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: space-around;
    flex-direction: row;
  }

  .test-group {
    margin-bottom: 50px;
    margin-top: 50px;
  }
</style>

