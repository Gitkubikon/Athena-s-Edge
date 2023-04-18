<script lang="ts">
  import { marked } from "marked";
  import { onMount, onDestroy } from "svelte";
  import TurndownService from "turndown";
  import { api } from "../main";
  import { onUltraMount } from "../utils/shenanigans";
  import { fade, fly } from "svelte/transition";

  let content: string = "";
  let renderedContent: string | undefined;
  let contentFiles: string[] = [];
  let selectedContentFile: string | undefined;
  let select: boolean = false;
  let edit: boolean = false;
  let newFileName: string | undefined;

  function demarked(html: string): string {
    const turndownService = new TurndownService();
    return turndownService.turndown(html);
  }

  async function loadContent(target: string): Promise<void> {
    const response = await api.get(`/content/${target}`);
    content = response.content;
    renderedContent = marked(content);
    select = true;
    selectedContentFile = target;
  }

  onUltraMount(async (): Promise<void> => {
    const response = await api.get("/content");
    contentFiles = JSON.parse(response.content);
    // Load the first file by default
    // if (contentFiles.length > 0) {
    //   await loadContent(contentFiles[0]);
    // }
  });

  // async function createContent(content, url) {
  //   const template = {
  //     [selectedContentFile]: {
  //       tags: "",
  //       content,
  //       upvotes: "",
  //       downvotes: "",
  //       comments: {
  //         user: "comment",
  //       },
  //       hot: "",
  //     },
  //   };
  //   const outputContent = JSON.stringify(template);
  //   await api.post(url, { content: outputContent });
  // }

  const handleContentChange = (event: { target: { value: string } }): void => {
    content = demarked(event.target.value);
    api.post(`/content/${selectedContentFile}`, { content });
  };
  const handleChange = (event: { target: { value: string } }): void => {
    content = event.target.value;
    api.post(`/content/${selectedContentFile}`, { content });
  };

  async function createNewFile(): Promise<void> {
    if (!newFileName?.trim()) return;
    const filename = `${newFileName}.md`;
    const response = await api.put(`${filename}`);
    if (response.status === 200) {
      contentFiles.push(filename);
      selectedContentFile = filename;
      newFileName = "";
      await loadContent(selectedContentFile);
      const response = await api.get("/content");
      contentFiles = JSON.parse(response.content);
    }
  }
</script>

{#if !select}
  <div class="card-menu" transition:fly={{ x: -200 }}>
    {#each contentFiles as file}
      <div
        style="display: flex; flex-direction: row; justify-content: space-between;"
      >
        <div
          class="button ultrafocus"
          style="width: 100%;"
          on:click={() => loadContent(file)}
        >
          <div class="card-title">{file}</div>
          <!-- Add a delete button that calls the deleteContent function with the name of the file -->
          <!-- <div class="card-preview">{previewContent[file]}</div> -->
        </div>
        <div
          class="ultrafocus button"
          on:click={async () => {
            await api.delete(file);
            const response = await api.get("/content");
            contentFiles = JSON.parse(response.content);
          }}
        >
          Delete
        </div>
      </div>
    {/each}
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
          createNewFile();
          const response = await api.get("/content");
          contentFiles = JSON.parse(response.content);
        }}
      >
        Create New File
      </div>
    </div>
  </div>
{:else}
  <div transition:fly={{ x: 200 }}>
    <div style="display: flex; flex-direction: row; justify-content: space-evenly;">
      <div class="button ultrafocus" on:click={() => (select = false)}>
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
{/if}

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
