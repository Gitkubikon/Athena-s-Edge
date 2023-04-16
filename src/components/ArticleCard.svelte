<script lang="ts">
  import { marked } from "marked";
  import TurndownService from "turndown";
    import { api } from "../main";
  

  export let fileName;

  let markdownContent: string;

  const turndownService = new TurndownService();

  async function getContent(): Promise<void> {
    // const response = await api.getContent(`/content/${fileName}`);
    // markdownContent = turndownService.turndown(marked(response));
  }

  $: {
    getContent();
  }
</script>

<div class="card">
  <h3>{fileName}</h3>
  <div class="card-body" innerHTML={markdownContent} />
</div>

<style>
  .card {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    margin: 10px;
  }

  .card h3 {
    margin-top: 0;
  }
</style>
