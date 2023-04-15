<script lang="ts">
  import { api } from "../main";
  import { onUltraMount } from "../utils/shenanigans";
  let username = "";
  let password = "";
  let loginStatus = "";
  let isSuccess = false;
  let isError = false;

  async function handleLogin() {
    loginStatus = "Logging in...";
    await api.login(username, password).then((response) => {
      if (response) {
        loginStatus = "Login successful!";
        isSuccess = true;
        isError = false;
        // Select the :root element
        const rootElement = document.querySelector(":root");

        // Update the value of the --ctp-mauve variable
        rootElement.style.setProperty("--ctp-mauve", "rgb(237, 135, 150)");
      } else {
        loginStatus = "Incorrect username or password.";
        isSuccess = false;
        isError = true;
      }
    });
  }

  onUltraMount(() => {});
</script>

<h1>Login</h1>

<label>
  Username:
  <input type="text" bind:value={username} />
</label>

<label>
  Password:
  <input type="password" bind:value={password} />
</label>

<button on:click={handleLogin}>Log in</button>

{#if loginStatus}
  {#if isSuccess}
    <div class="success">{loginStatus}</div>
    <div class="function:Home ultrafocus button success">Back to Home</div>
  {:else if isError}
    <div class="error">{loginStatus}</div>
  {/if}
{/if}

<style>
  h1 {
    color: var(--ctp-yellow);
  }
  label {
    color: var(--ctp-text);
    margin-bottom: 10px;
  }
  input {
    background-color: var(--ctp-surface1);
    border: none;
    border-radius: 5px;
    padding: 10px;
    margin-left: 10px;
    color: var(--ctp-text);
  }
  button {
    background-color: var(--ctp-green);
    color: var(--ctp-crust);
    border: none;
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
    cursor: pointer;
  }
  .success {
    background-color: var(--ctp-green);
    color: var(--ctp-crust);
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
  }
  .error {
    background-color: var(--ctp-red);
    color: var(--ctp-crust);
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
  }
</style>
