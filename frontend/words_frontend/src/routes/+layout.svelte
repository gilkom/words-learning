<script>
  import { authStore } from "../stores/auth";

</script>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          {#if $authStore.loggedIn}
          {#if $authStore.loggedIn && !$authStore.regular}
            <li class="nav-item">
                <a class="nav-link" href="/words">Words List</a>
            </li>
          {/if}
            <li class="nav-item">
              <a class="nav-link" href="/userwords">User Words List</a>
          </li>            
            <li class="nav-item">
              <a class="nav-link" href="/logout">Logout</a>
            </li>
            {:else}
            <li class="nav-item">
              <a class="nav-link" href="/login">Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/register">Register</a>
            </li>
            {/if}
        </ul>
      </div>
    </div>
  </nav>

  {#if $authStore.loggedIn}
  <div class="container">
    <div class="row">
        <p class="text-end">User: {$authStore.userData}</p>      
    </div>
  </div>
  {/if}
<div class="container">
    <slot />
</div>