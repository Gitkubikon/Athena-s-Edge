<div align="center">
    <img src="Welcome.svg" width="100%" height="100%" alt="css-in-readme">
 <!-- <div style="margin-bottom: 10px; background-color: #a8dadc; padding: 20px; border-radius: 10px;"> -->
 <!--        <p style="color: #1d3557; font-size: 24px;">こんにちは AI lovers and productivity -->
 <!--          enthusiasts!</p> -->
 <!--        <p style="color: #1d3557; font-size: 24px;">Welcome to Athena's Edge, your ultimate -->
 <!--          destination for all things Artificial Intelligence (AI) and productivity! Our blog is like -->
 <!--          a well-sharpened katana that cuts through the clutter and brings you the sharpest insights -->
 <!--          and hacks on how to use AI to take your productivity to the next level!</p> -->
 <!--      </div> -->
 <!--      <div style="margin-bottom: 10px; background-color: #f1faee; padding: 20px; border-radius: 10px;"> -->
 <!--        <h3 style="color: #e63946; font-size: 24px;">About Athena's Edge</h3> -->
 <!--        <p style="color: #1d3557; font-size: 20px;">Our blog is named after Athena, the Greek -->
 <!--          goddess of wisdom and strategy, who embodies the intelligence, foresight, and tactical -->
 <!--          know-how that we aim to provide in our articles. We are not just another run-of-the-mill -->
 <!--          AI blog; we are a community of AI samurais and productivity ninjas, who are constantly -->
 <!--          striving to empower you with the knowledge and tools to master the art of work and life!</p> -->
 <!--      </div> -->
 <!--      <div style="margin-bottom: 10px; background-color: #457b9d; padding: 20px; border-radius: 10px;"> -->
 <!--        <h3 style="color: #f1faee; font-size: 24px;">What you can expect from Athena's Edge</h3> -->
 <!--        <p style="color: #f1faee; font-size: 20px;">Our blog is your arsenal of AI tools, tips, and -->
 <!--          techniques that will help you optimize your workflow, automate tedious tasks, and unleash -->
 <!--          your productivity potential! Here are some of the key features that you can expect from -->
 <!--          Athena's Edge:</p> -->
 <!--        <ul style="color: #f1faee; font-size: 18px;"> -->
 <!--          <li>Technical guides and tutorials on how to use AI to enhance productivity in -->
 <!--            programming, lifestyle, and overall.</li> -->
 <!--          <li>Latest developments and use cases of AI, presented in an engaging and understandable -->
 <!--            way.</li> -->
 <!--          <li>A community of AI enthusiasts, beginners, and experts, who share their knowledge and -->
 <!--            collaborate on AI-related projects.</li> -->
 <!--          <li>A reliable source of information on AI, which can help you stay ahead of the curve in -->
 <!--            this ever-changing field!</li> -->
 <!--        </ul> -->
 <!--      </div> -->
 <!--      <div style="margin-bottom: 10px; background-color: #f1faee; padding: 20px; border-radius: 10px;"> -->
 <!--        <h3 style="color: #e63946; font-size: 24px;">How to get started</h3> -->
 <!--        <p style="color: #1d3557; font-size: 20px;">Getting started with Athena's Edge is as easy as -->
 <!--          counting in Japanese! Here's what you need to do:</p> -->
 <!--        <ol style="color: #1d3557; font-size: 18px;"> -->
 <!--          <li>Visit our website at <a href="https://www.athenasedge.com" -->
 <!--              style="color: #457b9d; text-decoration: none;">www.athenasedge.com</a> and explore our -->
 <!--            articles, tutorials, and community forums.</li> -->
 <!--          <li>Sign up for our newsletter to receive the latest updates and insights on AI and -->
 <!--            productivity.</li> -->
 <!--          <li>Join our community of AI samurais and productivity ninjas, and start sharing your -->
 <!--            knowledge and collaborating on AI-related projects!</li> -->
 <!--        </ol> -->
 <!--      </div> -->
 <!--      <div style="margin-bottom: 10px; background-color: #1d3557; color: #f1faee; padding: 20px; border-radius: 10px;"> -->
 <!--        <h2>Conclusion</h2> -->
 <!--        <p>At Athena's Edge, we believe that the combination of brains and bytes is the ultimate -->
 <!--          recipe for success in the digital age. By leveraging the power of AI, we can unlock our -->
 <!--          full productivity potential and achieve our goals with grace and efficiency! So, come join -->
 <!--          us on this exciting journey, and let's sharpen our AI skills and conquer the world -->
 <!--          together! さようなら!</p> -->
 <!--      </div> -->
</div>

## Run in SSR mode (Development)
```sh
npm run dev:ssr
```

## Run in CSR mode (Development)
```sh
npm run dev:csr
```

## Build SSR

### Node.js Server:
```sh
npm run build:nodejs
```

### Cloudflare Pages:
#### Deploy with `wrangler` CLI:
```sh
npm run build:cloudflare
wrangler pages publish dist/client
```

#### Deploy with Git:
* Link your Git repository to Cloudflare Pages.
* Set build configuration:
  Build command: `npm run build:cloudflare`
  Build output directory: `/dist/client`

### Netlify Functions
* Place `src/adapters/netlify/netlify.toml` in the root directory.
* Deploy with `netlify` CLI or link your Git repository to Netlify.
* Set environment variables in Netlify web UI:
  NODE_VERSION: 18

### Netlify Edge Functions:
* Place `src/adapters/netlify-edge/netlify.toml` in the root directory.
* Deploy with `netlify` CLI or link your Git repository to Netlify.
* Set environment variables in Netlify web UI:
  NODE_VERSION: 18
  AWS_LAMBDA_JS_RUNTIME: nodejs18.x

## Build CSR
```sh
npm run build:csr
```

## Run Node.js SSR Server (Production)
```sh
npm run serve:nodejs
```

## Run CSR Server (Preview)
In production, you should use web server such as nginx.

```sh
npm run serve:csr
```

## Features

### Router
Check out [svelte-pilot](https://github.com/jiangfengming/svelte-pilot)

### Automatic image importing
In a svelte file, `<img src="./path/to/img.png">` will automatically import and bundle the image file.

### Passing Hashed CSS Class Names to Child Components
Check out [svelte-preprocess-css-hash](https://github.com/jiangfengming/svelte-preprocess-css-hash)

### Official svelte-preprocess
Check out [svelte-preprocess](https://github.com/sveltejs/svelte-preprocess)

## License
This project is licensed under the [MIT License](LICENSE).
