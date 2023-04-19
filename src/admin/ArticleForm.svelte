<script>
  import { onMount } from "svelte";
  import { api } from "../main";

  onMount(async () => {
    const metadata = await api.getArticleMetadata();
    console.log(metadata)
  });
</script>

