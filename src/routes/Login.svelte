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

        // Update the theme from --ctp-mauve to --ctp-red

      } else {
        loginStatus = "Incorrect username or password.";
        isSuccess = false;
        isError = true;
      }
    });
  }

  function goToHome(): void {
    window.location.href = `${window.location.protocol}//${window.location.host}`;
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

  <div class="buttoon" on:click={handleLogin}>Log in</div>

  {#if loginStatus}
    {#if isSuccess}
      <div class="success">{loginStatus}</div>
    {:else if isError}
      <div class="error">{loginStatus}</div>
    {/if}
    <div class="buttoon success" on:click={goToHome}>Back to Home</div>
  {/if}

<style>
  h1 {
    color: var(--ctp-yellow);
    animation: bounce 0.5s ease;
  }

  label {
    color: var(--ctp-text);
    margin-bottom: 10px;
    animation: slidein 0.5s ease;
  }

  input {
    background-color: var(--ctp-surface1);
    border: none;
    border-radius: 5px;
    padding: 10px;
    margin-left: 10px;
    color: var(--ctp-text);
    animation: fadein 0.5s ease;
  }

  .buttoon {
    background-color: var(--ctp-green);
    color: var(--ctp-crust);
    border: none;
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
    cursor: pointer;
    animation: pulse 0.5s ease;
  }

  .success {
    background-color: var(--ctp-green);
    color: var(--ctp-crust);
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
    animation: slidein 0.5s ease;
  }

  .error {
    background-color: var(--ctp-red);
    color: var(--ctp-crust);
    border-radius: 5px;
    padding: 10px;
    margin-top: 20px;
    animation: shake 0.5s ease;
  }

  @keyframes pulse {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.05);
    }
    100% {
      transform: scale(1);
    }
  }

  @keyframes slidein {
    from {
      transform: translateX(-100%);
    }
    to {
      transform: translateX(0);
    }
  }

  @keyframes fadein {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes bounce {
    0%,
    100% {
      transform: translateY(0);
    }
    50% {
      transform: translateY(-5px);
    }
  }

  @keyframes shake {
    0% {
      transform: translateX(0);
    }
    25% {
      transform: translateX(-2px);
    }
    50% {
      transform: translateX(2px);
    }
    75% {
      transform: translateX(-2px);
    }
    100% {
      transform: translateX(0);
    }
  }
</style> 
