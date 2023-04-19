<script lang="ts">
  import { api } from "../main";
  import { getCookieValue, onUltraMount } from "../utils/shenanigans";
  import { fly, scale } from "svelte/transition";
  import { page, testApiDivs } from "../store";
  let username = "";
  let loginStatus = "";
  let isLogin = false;
  let isError = false;
  let bottomleft;
  let topright;
  const gifUrl = "https://media.tenor.com/TLhWkKdr770AAAAd/giga-chad.gif";

  if (getCookieValue("token")) {
    isLogin = true;
  }

  async function handleLogin() {
    loginStatus = "Logging in...";
    await api.login(username, password).then((response) => {
      if (response) {
        loginStatus = "Login successful!";
        isError = false;
        page.set("AdminPage");
        // Select the :root element
        const rootElement = document.querySelector(":root");

        // Update the value of the --ctp-mauve variable
        //@ts-ignore
        rootElement.style.setProperty("--ctp-mauve", "rgb(237, 135, 150)");
      } else {
        loginStatus = "Incorrect username or password.";
        isError = true;
      }
    });
  }

  onUltraMount(() => {});

  let email = "";
  let password = "";

  function handleSubmit() {
    if (email === "" || password === "") {
      alert("Please fill in all fields.");
    } else {
      console.log("Submitting form...");
      // Add your form submission logic here
    }
  }
</script>

<div class="login-container">
  <div transition:scale={{ delay: 100, duration: 900 }} class="login-box">
    <div
      style="display: flex; flex-direction: row; justify-content: center; align-content: center;"
    >
      <!-- <h1>{`${getCookieValue("user").toUpperCase()}'s CONSOLE`}</h1> -->
      <div class="circle">
        <img src={gifUrl} alt="Embedded GIF" />
      </div>
    {#if isLogin}
      <h1 class="login-title">CHAD'S CONSOLE</h1>
    {:else}
      <h1 class="login-title">CHAD'S LOGIN</h1>
    {/if}
    </div>
    {#if !isLogin}
      <input
        class="login-input"
        type="text"
        placeholder="Username"
        bind:value={username}
      />
      <input
        class="login-input"
        type="password"
        placeholder="Password"
        bind:value={password}
      />
      {#if isError}
        <p transition:fly={{ x: -200 }} class="login-error">
          Invalid Credentials
        </p>
      {/if}
      <div class="ultrafocus login-button zone" on:click={handleLogin}>Log in</div>
    {/if}
    {#if isLogin}
      <div class="buttons">
        <div
          style="margin: 5px; height: fit-content;"
          class="function:AdminPage login-button ultrafocus"
        >
          Console
        </div>
        <div
          style="margin: 5px; height: fit-content;"
          class="function:ArticleForm login-button ultrafocus"
        >
          Editor
        </div>
        <div
          style="margin: 5px; height: fit-content;"
          class="function:StyleGuide button login-button ultrafocus"
        >
          Style Guide
        </div>
        <div
          style="margin: 5px; height: fit-content;"
          class="function:TestApi login-button ultrafocus"
        >
          Run Api Test
        </div>
        <div
          style="margin: 5px; height: fit-content;"
          class="function:Logout login-button ultrafocus"
        >
          Log out
        </div>

        <div class="test-group">
          <div id="test-results">
            {#each $testApiDivs as testElement}
              {@html testElement.outerHTML}
            {/each}
          </div>
        </div>
      </div>
    {/if}
  </div>
  <!-- Added elements for animation -->
</div>
<div bind:this={topright} class="rotate top-right" />
<div bind:this={bottomleft} class="rotate bottom-left" />

<style>
  .test-group {
    margin-bottom: 50px;
    margin-top: 50px;
  }

  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: var(--ctp-base);
    background-image: radial-gradient(var(--ctp-mauve) 1px, transparent 1px),
      radial-gradient(var(--ctp-mauve) 1px, transparent 1px);
    background-size: 50px 50px;
    background-position: 0 0, 25px 25px;
  }

  .login-box {
    z-index: 1;
  }

  .login-container {
    position: relative;
  }

  .rotate {
    position: absolute;
    width: 230%;
    height: 200%;
    background-color: var(--ctp-mauve);
    animation-duration: 0.9s;
    animation-fill-mode: forwards;
    animation-timing-function: ease-in-out;
    z-index: 0;
  }

  .top-right {
    animation-name: topRightAnim;
  }

  .bottom-left {
    animation-name: bottomLeftAnim;
  }

  @keyframes topRightAnim {
    from {
      top: -50px;
      right: -50px;
      transform: rotate(70deg);
    }
    to {
      top: 50%;
      right: 50%;
      transform: rotate(35deg);
    }
  }

  @keyframes bottomLeftAnim {
    from {
      bottom: -50px;
      left: -50px;
      transform: rotate(70deg);
    }
    to {
      bottom: 50%;
      left: 50%;
      transform: rotate(35deg);
    }
  }


  .circle {
    background-color: transparent;
    border: 2px solid;
    border-radius: 50%;
    display: inline-block;
    height: 46px; /* 35px width + 2*3px border */
    width: 46px; /* 35px height + 2*3px border */
    overflow: hidden;
    margin-right: 10px;
    margin-top: -10px;
    align-self: center;
  }

  .circle img {
    margin-right: 10px;
    width: 45px;
    height: 45px;
  }

  .login-box {
    max-width: 400px;
    padding: 2rem;
    border-radius: 5px;
    background-color: var(--ctp-mantle);
    box-shadow: 5px 5px 10px var(--ctp-teal);
  }

  .login-title {
    font-size: 2rem;
    font-weight: bold;
    color: var(--ctp-mauve);
    margin-bottom: 2rem;
    text-align: center;
  }

  .login-input {
    width: 85%;
    padding: 0.75rem;
    margin-bottom: 1rem;
    border: 2px solid var(--ctp-mauve);
    border-radius: 5px;
  }

  .login-button {
    padding: 0.75rem;
    background-color: var(--ctp-mauve);
    color: var(--ctp-surface1);
    font-weight: bold;
    text-transform: uppercase;
    border-radius: 8px;
    outline: 2px solid;
    transition: background-color 0.3s ease;
  }

  .login-error {
    color: var(--ctp-red);
    text-align: center;
    margin-top: 1rem;
  }
  .buttons {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    align-content: center;
    justify-content: center;
  }
</style>
