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

  const gifUrl = "https://media.tenor.com/TLhWkKdr770AAAAd/giga-chad.gif";
  onUltraMount(() => {});
</script>

<section transition:fly={{ y: -200 }}>
  <div class="pos terminal">
    <div
      style="display: flex; flex-direction: row; justify-content: center; align-content: center;"
    >
      <!-- <h1>{`${getCookieValue("user").toUpperCase()}'s CONSOLE`}</h1> -->
      <div class="circle">
        <img src={gifUrl} alt="Embedded GIF" />
      </div>
      <h1>CHAD'S CONSOLE</h1>
    </div>
    <div class="buttons flex flex-wrap justify-between py-4 px-10">
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
  .circle {
    background-color: transparent;
    border: 2px solid;
    border-radius: 50%;
    display: inline-block;
    height: 46px; /* 35px width + 2*3px border */
    width: 46px; /* 35px height + 2*3px border */
    overflow: hidden;
    margin-right: 10px;
    margin-top: -3px;
    align-self: center;
  }

  .circle img {
    margin-right: 10px;
    width: 45px;
    height: 45px;
  }
</style>
