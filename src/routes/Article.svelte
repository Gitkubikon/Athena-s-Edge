<script>
  import { fade, fly } from "svelte/transition";
  import Footer from "../components/Footer.svelte";
  import { content } from "../store";
  import { marked } from "marked";
</script>

<section transition:fly={{ y: 1000 }}>
  <article>
    {@html marked($content.content)}
  </article>
  <Footer />
</section>

<style>
  article {
    font-family: sans-serif;
    line-height: 1.5;
    font-size: 16px;
    font-family: "Montserrat", sans-serif;
    resize: none;
    background-color: transparent;
    color: var(--ctp-mauve);
    padding-bottom: 80px;
  }
</style>
