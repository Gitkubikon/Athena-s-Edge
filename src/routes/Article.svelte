<script lang="ts">
  // import { getPost } from '../markdown';
  import { onMount } from 'svelte';

  export let slug: string;

  let content: string;

  onMount(async () => {
    // content = await getPost(slug);
  });
</script>

<main>
  <article>
    {@html content}
  </article>
</main>
