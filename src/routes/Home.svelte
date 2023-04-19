<script>
  import ArticleCard from "../components/ArticleCard.svelte";
  import Footer from "../components/Footer.svelte";
  import { api } from "../main";
  import { onUltraMount } from "../utils/shenanigans";

  onUltraMount(async () => {
    
    const meta = await api.getArticleMetadata();
    console.log(meta);
  });
</script>

<section>
  <ArticleCard
    upload_date="Level 4"
    name="The Barbarian"
    description="The Barbarian is a kilt-clad Scottish warrior with an angry, battle-ready expression, hungry for destruction. He has Killer yellow horseshoe mustache."
    imgSrc="https://s3-us-west-2.amazonaws.com/s.cdpn.io/195612/barbarian.png"
    dislikes="20"
    main_tag="16"
    likes="150"
  />
  <Footer />
</section>
