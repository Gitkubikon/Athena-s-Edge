<script lang="ts">
  import { api } from "../main";
  import { marked } from "marked";
  import TurndownService from "turndown";
  import { onUltraMount } from "../utils/shenanigans";
  import { fade, fly } from "svelte/transition";
  import { page } from "../store";

  export let currentArticle;
  let renderedContent: string | undefined;
  let edit: boolean = false;
  let content: string;

  function demarked(html: string): string {
    const turndownService = new TurndownService();
    return turndownService.turndown(html);
  }
  async function loadContent(target: string): Promise<void> {
    const content = await api.getArticle(
      currentArticle.category,
      currentArticle.article
    );
    renderedContent = marked(content);
  }

  const handleContentChange = (): void => {
    content = demarked(content);
    api.updateArticle(currentArticle.category, currentArticle.article, content);
  };
  const handleChange = (): void => {
    api.updateArticle(currentArticle.category, currentArticle.article, content);
  };

  onUltraMount(async (): Promise<void> => {
    let response = await api.getArticle(
      currentArticle.category,
      currentArticle.article
    );
    content = response.valueOf().toString();
  });
</script>

<div transition:fly={{ x: 200 }}>
  <div
    style="display: flex; flex-direction: row; justify-content: space-evenly;"
  >
    <div class="button ultrafocus" on:click={() => page.set("ArticleForm")}>
      Back to Card Menu
    </div>
    <div class="button ultrafocus" on:click={() => (edit = !edit)}>
      Toggle Editor Mode
    </div>
  </div>
  {#if !edit}
    <div
      on:input={handleContentChange}
      bind:innerHTML={renderedContent}
      contenteditable="true"
      class="editor"
    />
  {:else}
    <textarea
      on:input={handleChange}
      bind:innerHTML={content}
      contenteditable="true"
      class="editor"
    />
  {/if}
</div>

<style>
  .editor {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 78.5vh;
    color: var(--ctp-sky);
    background-color: var(--ctp-mantle);
    overflow: auto;
  }
  .card-menu {
    width: calc(100vw - 150px);
    height: -moz-available;
    display: flex;
    position: absolute;
    flex-direction: column;
    top: 2rem;
  }
  #new {
    top: 0px;
    width: calc(100vw - 200px);
    height: -moz-available;
    display: flex;
  }
  .button {
    padding: 0.6rem;
    background: var(--ctp-mantle);
    color: var(--ctp-teal);
  }
</style>
