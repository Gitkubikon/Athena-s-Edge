<script lang="ts">
  import { fade } from "svelte/transition";
  import ArticleCard from "../components/ArticleCard.svelte";
  import { api } from "../main";
  import { getCookieValue, onUltraMount } from "../utils/shenanigans";

  let contentFiles: string[] = [];

  onUltraMount(async (): Promise<void> => {
    api.getMetadata().then((metadata) => {
      contentFiles = Object.keys(metadata);
    });
  });
</script>

<div transition:fade>
  {#each contentFiles as fileName}
    <ArticleCard {fileName} filename={fileName} />
  {/each}
</div>

<style>
  div {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
