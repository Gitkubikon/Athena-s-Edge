<script lang="ts">
  import { api } from "../main";
  import { marked } from "marked";
  import TurndownService from "turndown";
  import { onMount } from "svelte";
  import { fade, fly } from "svelte/transition";
  import { createEventDispatcher } from "svelte";
  import { onUltraMount } from "../utils/shenanigans";

  export let currentArticle;

  let content = "";
  let renderedContent = "";

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("close-editor");
  }

  function handleChange() {
    renderedContent = marked(content);
    api.updateArticle(currentArticle.category, currentArticle.article, content);
  }

  onUltraMount(async () => {
    const response = await api.getArticle(
      currentArticle.category,
      currentArticle.article
    );
    //@ts-ignore
    content = response.content;
    renderedContent = marked(content);
  });
</script>

<div class="editor">
  <div
    style="width: 24px;"
    class="close-btn ultrafocus button"
    on:click={handleClick}
  >
    <svg fill="var(--ctp-base)" viewBox="0 0 24 24" stroke-width="1.5">
      <circle
        cx="12"
        cy="12"
        r="10"
        stroke="var(--ctp-red)"
        stroke-linecap="round"
        stroke-linejoin="round"
        fill="var(--ctp-red)"
      />
      <path
        stroke="var(--ctp-red)"
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5"
      />
    </svg>
  </div>
  <div class="markdown-editor">
    <textarea
      class="markdown-textarea"
      bind:value={content}
      on:input={handleChange}
      placeholder="Write your article here"
    />
  </div>
  <div style="width: 3px; background-color: var(--ctp-crust);" />
  <div class="markdown-preview" transition:fade>
    {@html renderedContent || ""}
  </div>
</div>

<style>
  .editor {
    display: flex;
    flex-direction: row;
    height: 100%;
    color: var(--ctp-sky);
    background-color: var(--ctp-mantle);
    overflow: hidden;
  }

  .close-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    border: none;
    cursor: pointer;
    transition: transform 0.2s;
  }

  .close-btn:hover {
    transform: scale(1.2);
  }

  .close-btn img {
    width: 20px;
    height: 20px;
  }

  .markdown-editor {
    flex: 1;
    padding: 20px;
  }

  .markdown-textarea {
    display: block;
    width: 100%;
    height: 100%;
    border: none;
    font-size: 16px;
    font-family: "Montserrat", sans-serif;
    resize: none;
    background-color: transparent;
    color: var(--ctp-sky);
    outline: none;
  }

  .markdown-preview {
    flex: 1;
    padding: 20px;
    overflow: auto;
  }
</style>
