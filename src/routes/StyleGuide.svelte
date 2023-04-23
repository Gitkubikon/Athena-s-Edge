<script>
  import { fade, fly } from "svelte/transition";
  import { onUltraMount } from "../utils/shenanigans";

  onUltraMount(() => {});
</script>

<section style="display: flex; justify-content: center; align-content: center;" transition:fly={{ y: -200 }}>
  <div id="stg">
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-text)"
    >
      Text
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0);  background-color: var(--ctp-subtext1)"
    >
      subtext1
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0);  background-color: var(--ctp-subtext0)"
    >
      subtext0
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-text);  background-color: var(--ctp-overlay2)"
    >
      overlay2
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-overlay1)"
    >
      overlay1
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-surface2)"
    >
      surface2
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-surface1)"
    >
      surface1
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-surface0)"
    >
      surface0
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-crust)"
    >
      crust
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-mantle)"
    >
      mantle
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-subtext1);  background-color: var(--ctp-base)"
    >
      base
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-rosewater)"
    >
      rosewater
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-flamingo)"
    >
      flamingo
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-pink)"
    >
      pink
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-mauve)"
    >
      mauve
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-red)"
    >
      red
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-maroon)"
    >
      maroon
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-peach)"
    >
      peach
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-yellow)"
    >
      yellow
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-green)"
    >
      green
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-teal)"
    >
      teal
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-sky)"
    >
      sky
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-sapphire)"
    >
      sapphire
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-blue)"
    >
      blue
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-surface0); background-color: var(--ctp-lavender)"
    >
      lavender
    </div>
    <div
      class="ultrafocus button color function:copyColor"
      style="color: var(--ctp-overlay2);  background-color: rvar(--ctp-overlay0)"
    >
      overlay0
    </div>
  </div>
</section>

<style>
  .color {
    height: 3.5vh;
    padding: 2rem;
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
  #stg {
    position: absolute;
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    height: 140%;
    max-width: 800px;
    max-height: 400px;
    padding: 2rem;
    border-radius: 5px;
    background-color: rgb(180, 197, 228);
    box-shadow: 5px 5px 5px var(--ctp-mauve);
  }
</style>
