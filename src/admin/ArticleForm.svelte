<script lang="ts">
  import Card from "./Card.svelte";
  import { api } from "../main";
  import { onMount } from "svelte";
    import { fade } from "svelte/transition";

  let newFileName = "";
  let meta = null;
  let edit = false;
  let currentArticle = {};

  onMount(async () => {
    meta = await api.getArticleMetadata();
  });
</script>

{#if !edit}
  {#if meta !== null}
    <div class="card-container">
      {#each Object.entries(meta) as [category, articles]}
        <div class="card">
          <h2 class="card-title">{category}</h2>
          {#each Object.keys(articles) as article}
            <div
              on:click={() => {
                currentArticle = { category, article };
                edit = true;
              }}
              class="article"
            >
              <h3 class="article-title">{article}</h3>
              <p class="article-date">{articles[article].created_at}</p>
            </div>
          {/each}
        </div>
      {/each}
    </div>
  {:else}
    <p>Loading metadata...</p>
  {/if}
{:else}
  <Card {currentArticle} />
{/if}
<div
  id="new"
  transition:fade
  style="display: flex; flex-direction: row; justify-content: space-around; margin-top: 30px; align-content: center;"
>
  <input
    type="text"
    style="height: 2rem; align-self: center; background: var(--ctp-base);"
    bind:value={newFileName}
    placeholder=""
  />
  <div
    class="ultrafocus button"
    on:click={async () => {
      await api.createArticle("unindexed", newFileName);
      meta = await api.getArticleMetadata();
    }}
  >
    Create New File
  </div>
</div>

<style>
  .card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    justify-content: center;
  }
</style>
