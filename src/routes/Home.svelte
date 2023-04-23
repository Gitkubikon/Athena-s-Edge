<script>
  import { fly } from "svelte/transition";
  import ArticleCard from "../components/ArticleCard.svelte";
  import Footer from "../components/Footer.svelte";
  import { api } from "../main";
  import { onUltraMount } from "../utils/shenanigans";

  let meta = null;
  let categories = [];
  let currentArticle = {};
  let selectedCategory = "";

  let edit = false;

  function handleCloseEditor() {
    edit = false;
  }

  onUltraMount(async () => {
    meta = await api.getArticleMetadata();
    categories = Object.keys(meta);
    if (categories.length > 0) {
      selectedCategory = "";
    }
  });
</script>

<section transition:fly={{ y: -1000 }}>
  <div class="category-cards">
    <div
      on:keydown={() => {}}
      on:click={() => {
        selectedCategory = "";
      }}
      class={selectedCategory === ""
        ? "active ultrafocus button"
        : "ultrafocus button"}
    >
      All
    </div>
    {#each categories as category}
      <div
        on:keydown={() => {}}
        on:click={() => {
          selectedCategory = category;
        }}
        class={selectedCategory === category
          ? "active ultrafocus button"
          : "ultrafocus button"}
      >
        {category}
      </div>
    {/each}
  </div>

  <div class="article-cards">
    {#if meta !== null}
      {#each Object.entries(meta) as [category, articles]}
        {#if selectedCategory === "" || selectedCategory === category}
          {#each Object.entries(articles) as [article, metadata]}
            <div
              on:keydown={() => {}}
              on:click={() => {
                currentArticle = { category, article };
              }}
              class="article"
            >
              <ArticleCard
                upload_date={metadata.created_at}
                name={article}
                description={metadata.description}
                imgSrc={metadata.cover}
                bgSrc={metadata.background}
                dislikes={metadata["engagement"]["dislikes"]}
                main_tag={category}
                likes={metadata["engagement"]["likes"]}
              />
            </div>
          {/each}
        {/if}
      {/each}
      <Footer />
    {:else}
      <p>Loading metadata...</p>
    {/if}
  </div>
</section>

<style>
  section {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: center;
  }

  .category-cards {
    display: flex;
    justify-content: center;
    margin-bottom: 32px;
  }

  .article-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 100%;
  }
  .category-cards > div {
    display: flex;
    height: 24px;
    justify-content: center;
    align-content: center;
    font-size: 16px;
    font-weight: bold;
    border-radius: 16px;
    color: var(--ctp-text);
  }

  .category-cards > div.active {
    background-color: var(--ctp-mauve) !important;
  }

  .category-cards div {
    /* Set common styles for category cards */
    padding: 10px;
    margin-right: 10px;
    cursor: pointer;
    color: #fff;
    font-weight: bold;
  }

  /* Set background colors using CSS variables */
  .category-cards div:nth-child(1) {
    background-color: var(--ctp-rosewater);
  }
  .category-cards div:nth-child(2) {
    background-color: var(--ctp-flamingo);
  }
  .category-cards div:nth-child(3) {
    background-color: var(--ctp-pink);
  }
  .category-cards div:nth-child(4) {
    background-color: var(--ctp-lavender);
  }
  /* .category-cards div:nth-child(4) { */
  /*   background-color: var(--ctp-mauve); */
  /* } */
  .category-cards div:nth-child(5) {
    background-color: var(--ctp-red);
  }
  .category-cards div:nth-child(6) {
    background-color: var(--ctp-maroon);
  }
  .category-cards div:nth-child(7) {
    background-color: var(--ctp-peach);
  }
  .category-cards div:nth-child(8) {
    background-color: var(--ctp-yellow);
  }
  .category-cards div:nth-child(9) {
    background-color: var(--ctp-green);
  }
  .category-cards div:nth-child(10) {
    background-color: var(--ctp-teal);
  }
  .category-cards div:nth-child(11) {
    background-color: var(--ctp-sky);
  }
  .category-cards div:nth-child(12) {
    background-color: var(--ctp-sapphire);
  }
  .category-cards div:nth-child(13) {
    background-color: var(--ctp-blue);
  }
</style>
