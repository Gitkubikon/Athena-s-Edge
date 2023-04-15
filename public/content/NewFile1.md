<div align="center">
  <a href="Welcome.svg" target="_blank">
    <img src="Welcome.svg" width="100%" height="100%" alt="css-in-readme">
  </a>
</div>

## Svelte + TS + Vite + Deno + TailwindCSS

Svelte is a modern JavaScript framework that allows developers to build web applications with minimal overhead. It uses a declarative approach, meaning that developers only need to specify what they want the app to do, and Svelte takes care of the rest. This results in faster, more efficient code that is easier to maintain.

Tailwind is a CSS framework that provides a set of utility classes that allow developers to quickly style their web applications. It uses a "utility-first" approach, meaning that instead of providing pre-designed components, it provides low-level styling tools that can be composed to create any design. This results in faster development times and more flexibility in design.

Vite is a build tool for modern web development. It is designed to be fast, lightweight, and easy to use, making it a great choice for developers who want to quickly set up and iterate on their web projects. It uses a just-in-time (JIT) compilation approach, meaning that it only builds the parts of the app that are needed, resulting in faster build times and better performance.

Together, Svelte, Tailwind, and Vite make for a powerful and efficient stack for building modern web applications.

- https://svelte.dev/
- https://www.typescriptlang.org/
- https://vitejs.dev/
- https://tailwindcss.com/

## Technical considerations

**Why use this over SvelteKit?**

- It brings its own routing solution which might not be preferable for some users.
- It is first and foremost a framework that just happens to use Vite under the hood, not a Vite app.

**Why `global.d.ts` instead of `compilerOptions.types` inside `jsconfig.json` or `tsconfig.json`?**

Setting `compilerOptions.types` shuts out all other types not explicitly listed in the configuration. Using triple-slash references keeps the default TypeScript setting of accepting type information from the entire workspace, while also adding `svelte` and `vite/client` type information.

**Why enable `allowJs` in the TS template?**

While `allowJs: false` would indeed prevent the use of `.js` files in the project, it does not prevent the use of JavaScript syntax in `.svelte` files. In addition, it would force `checkJs: false`, bringing the worst of both worlds: not being able to guarantee the entire codebase is TypeScript, and also having worse typechecking for the existing JavaScript. In addition, there are valid use cases in which a mixed codebase may be relevant.

**Why is HMR not preserving my local component state?**

HMR state preservation comes with a number of gotchas! It has been disabled by default in both `svelte-hmr` and `@sveltejs/vite-plugin-svelte` due to its often surprising behavior. You can read the details [here](https://github.com/rixo/svelte-hmr#svelte-hmr).

If you have state that's important to retain within a component, consider creating an external store which would not be replaced by HMR.

```ts
// store.ts
// An extremely simple external store
import { writable } from 'svelte/store'
export default writable(0)
```

## Project Structure

```scss

├── public
│   ├── api.py
│   ├── app.py
│   ├── categorize.py
│   ├── content
│   │   ├── metadata.json
│   │   ├── NewFile1.md
│   │   └── NewFile.md
│   ├── img
│   ├── robots.txt
│   └── sitemap.xml
│
├── src
│   ├── app.css                       Global CSS (includes dark : light themes)
│   │ 
│   ├── App.svelte                    Main APP, contains navigation
│   │ 
│   ├── assets                        Contains website assets (images, JSON, ...)
│   │   └── svelte.svg
│   │ 
│   ├── components                    Svelte components (ArticleCard, Footer, Header, NewsletterSignup, UltraFocus)
│   │   ├── ArticleCard.svelte
│   │   ├── Footer.svelte
│   │   ├── Header.svelte
│   │   ├── NewsletterSignup.svelte
│   │   └── UltraFocus.svelte
│   │ 
│   ├── routes                        Svelte pages (404, About, Article, Home, Login) and navigation components (Side, Top)
│   │   ├── 404.svelte
│   │   ├── About.svelte
│   │   ├── Article.svelte
│   │   ├── Home.svelte
│   │   ├── Login.svelte
│   │   └── nav
│   │       ├── Side.svelte
│   │       └── Top.svelte
│   │ 
│   ├── admin                         Svelte pages (AdminPage, ArticleForm) for managing content
│   │   ├── AdminPage.svelte
│   │   └── ArticleForm.svelte
│   │ 
│   ├── utils                         Utility scripts for the website (API request functions, article management functions, etc.)
│   │   ├── api.ts
│   │   ├── articles.ts
│   │   ├── functions.ts
│   │   ├── markdownToHtml.ts
│   │   └── shenanigans.ts
│   │ 
│   ├── markdown.ts                   Function for converting Markdown to HTML
│   ├── store.ts                      Global store for managing app state
│   ├── main.ts                       Main entry point for the website
│   └── catppuccin.css               Custom CSS for the website
│
├── svelte.config.js
├── tsconfig.json
├── tsconfig.node.json
├── vite.config.ts
├── README.md
├── package.json
└── package-lock.json
```



### Install and run 

```
cd hive-dashboard
npm install
npm run dev
```
