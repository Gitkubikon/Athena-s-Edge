<script>
  // @ts-nocheck

  import { page, updateElements } from "./store";
  import Trailer from "./utils/UltraFocus.svelte";
  import Top from "./routes/nav/Top.svelte";
  import Side from "./routes/nav/Side.svelte";
  import Login from "./routes/Login.svelte";
  import Home from "./routes/Home.svelte";
  import Article from "./routes/Article.svelte";
  import About from "./routes/About.svelte";
  import Foo from "./routes/404.svelte";
  import ArticleForm from "./admin/ArticleForm.svelte";
    import { getCookieValue } from "./utils/shenanigans";

  const pages = [
    { id: "Login", component: Login },
    { id: "Home", component: Home },
    { id: "Article", component: Article },
    { id: "About", component: About },
    { id: "Foo", component: ArticleForm },
  ];

  const getComponent = function () {
    try {
      if (window.location.pathname.includes("/Login")) {
        return Login;
      }
      return pages.find((p) => p.id === $page).component;
    } catch (e) {
      return Foo;
    }
  };

  if (getCookieValue("token")) {
    document
      .querySelector(":root")
      .style.setProperty("--ctp-mauve", "rgb(237, 135, 150)");
  }
</script>

<main class="w-screen h-screen">
  <Top />
  <div class="flex flex-row">
    <Side />
    <div id="sectionback">
      <section>
        <svelte:component this={getComponent()} />
      </section>
    </div>
  </div>
</main>

<Trailer />

<style>
</style>
