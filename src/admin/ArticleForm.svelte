<script lang="ts">
  import Card from "./Card.svelte";
  import { api } from "../main";
  import { onMount } from "svelte";
  import { fade, fly } from "svelte/transition";
  import { testDeleteArticle } from "../utils/testapi";

  let newFileName = "";
  let meta = null;
  let edit = false;
  let currentArticle = {};

  function handleCloseEditor() {
    edit = false;
  }

  onMount(async () => {
    meta = await api.getArticleMetadata();
  });
</script>

{#if !edit}
  <section>
    {#if meta !== null}
      <div class="card-container">
        {#each Object.entries(meta) as [category, articles]}
          <div class="card">
            <h2 class="card-title">{category}</h2>
            {#each Object.keys(articles) as article}
              <div
                on:keydown={() => {}}
                on:click={() => {
                  currentArticle = { category, article };
                  edit = true;
                }}
                class="article"
              >
                <h3 class="article-title">{article}</h3>
                <p class="article-date">{articles[article].created_at}</p>
                <div style="display: flex; flex-direction: row;">
                  <!-- <div -->
                  <!--   class="ultrafocus realbutton button" -->
                  <!--   on:keydown={() => {}} -->
                  <!--   on:click={() => api.getArticle(category, article)} -->
                  <!-- > -->
                  <!--   Download -->
                  <!-- </div> -->
                  <div
                    class="ultrafocus realbutton button"
                    on:keydown={() => {}}
                    on:click={async () => {
                      api.deleteArticle(category, article);
                      edit = false;
                    }}
                  >
                    Delete
                  </div>
                </div>
              </div>
            {/each}
          </div>
        {/each}
      </div>
    {:else}
      <p>Loading metadata...</p>
    {/if}

    <div
      id="new"
      transition:fade
      style="display: flex; flex-direction: row; justify-content: space-evenly; margin-top: 30px; align-content: center;"
    >
      <input
        type="text"
        style="height: 2rem; background: var(--ctp-base);"
        bind:value={newFileName}
        placeholder=""
      />
      <div
        class="new ultrafocus button realbutton"
        on:keydown={() => {}}
        on:click={async () => {
          await api.createArticle("unindexed", newFileName);
          meta = await api.getArticleMetadata();
        }}
      >
        Create New File
      </div>
    </div>
    <div
      class="new ultrafocus button realbutton"
      on:keydown={() => {}}
      on:click={async () => {
        await api.createArticle("unindexed", newFileName);
        meta = await api.getArticleMetadata();
      }}
    >
      Generate New Article
    </div>
  </section>
{:else}
  <Card {currentArticle} on:close-editor={handleCloseEditor} />
{/if}

<style>
  .card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 1rem;
    padding: 1rem;
  }

  .card {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: var(--ctp-light);
    border-radius: 1rem;
    box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
    padding: 1rem;
    width: 30%;
    transition: transform 0.2s ease-in-out;
  }

  .card:hover {
    transform: translateY(-0.25rem);
  }

  .card-title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 1rem;
    color: var(--ctp-text);
    text-transform: uppercase;
  }

  .article-title {
    font-size: 1.5rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
    color: var(--ctp-text);
  }

  .article-date {
    font-size: 0.8rem;
    margin-top: 0.5rem;
    color: var(--ctp-secondary);
  }

  .article {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: var(--ctp-base);
    border-radius: 1rem;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    margin-bottom: 1rem;
    padding: 1rem;
    width: 90%;
    transition: transform 0.2s ease-in-out;
  }

  .article:hover {
    transform: translateY(-0.25rem);
  }

  #new {
    align-items: center;
    background-color: var(--ctp-dark);
    border-radius: 1rem;
    color: var(--ctp-light);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin-top: 1rem;
    padding: 1rem;
    width: 100%;
  }
  .new {
    background-color: var(--ctp-base);
  }

  input {
    border: none;
    border-radius: 0.5rem;
    color: var(--ctp-primary);
    font-size: 1rem;
    padding: 0.5rem;
    width: 60%;
  }

  .ultrafocus:hover {
    background-color: var(--ctp-secondary);
  }
</style>
