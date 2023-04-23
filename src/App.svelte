<script>
  // @ts-nocheck

  import { page, updateElements } from "./store";
  import { getCookieValue } from "./utils/shenanigans.ts";
  import Trailer from "./utils/UltraFocus.svelte";
  import Top from "./routes/nav/Top.svelte";
  import Side from "./routes/nav/Side.svelte";
  import Login from "./routes/Login.svelte";
  import Home from "./routes/Home.svelte";
  import Article from "./routes/Article.svelte";
  import About from "./routes/About.svelte";
  import Foo from "./routes/404.svelte";
  import ArticleForm from "./admin/ArticleForm.svelte";
  import AdminPage from "./admin/AdminPage.svelte";
  import StyleGuide from "./routes/StyleGuide.svelte";
  import Footer from "./components/Footer.svelte";
  import Test from "./test.svelte";

  const pages = [
    { id: "Login", component: Login },
    { id: "Home", component: Home },
    { id: "Article", component: Article },
    { id: "About", component: About },
    { id: "Foo", component: Foo },
    { id: "AdminPage", component: AdminPage },
    { id: "ArticleForm", component: ArticleForm },
    { id: "StyleGuide", component: StyleGuide },
  ];

  const getComponent = function () {
    try {
      return pages.find((p) => p.id === $page).component;
    } catch (e) {
      return Foo;
    }
  };

  if (getCookieValue("token")) {
    document
      .querySelector(":root")
      .style.setProperty("--ctp-mauve", "rgb(125, 196, 228)");
    page.set("AdminPage");
  }

  let currentTry = 0;
  const sequence = ["g", "i", "g", "a", "c", "h", "a", "d"];

  document.addEventListener("keydown", (event) => {
    if (event.key === sequence[currentTry]) {
      currentTry++;
      if (currentTry === sequence.length) {
        page.set("AdminPage");
        currentTry = 0;
      }
    } else {
      currentTry = 0;
    }
  });
</script>

<main class="w-screen h-screen">
  <Top />
  <div class="flex flex-row">
    <Side />
    <div id="sectionback">
      <svelte:component this={getComponent()} />
    </div>
  </div>
</main>

<Trailer />
<!-- <Test /> -->

<style>
</style>
