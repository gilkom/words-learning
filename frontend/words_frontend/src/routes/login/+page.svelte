<script>
    import { onMount } from 'svelte';
    import { authStore, setLoggedIn, logout as logoutAction } from '../../stores/auth.js';
    import { goto } from '$app/navigation';

    let username = '';
    let password = '';
    let error = '';

    const handleSubmit = async () => {
        try {
            const response = await fetch('http://localhost:8000/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
                mode: 'cors',
                credentials: 'include',                
            });

            if (response.ok) {
                const data = await response.json();
                setLoggedIn(true, data.username, data.id, data.regular);
                localStorage.setItem('authState', JSON.stringify({ loggedIn: true, userData: data.username, id: data.id, regular: data.regular}));            
            } else {
                const data = await response.json();
                throw new Error(data.error);
            }
        } catch (error) {
            console.error(error);
            error = 'Błąd logowania. Spróbuj ponownie.';
        }
    };
    onMount(() => {
        const authState = localStorage.getItem('authState');
        if (authState) {
            const { loggedIn, userData, id, regular, } = JSON.parse(authState);
            setLoggedIn(loggedIn, userData, id);
        }
});

</script>

{#if $authStore.loggedIn}
    <div>
        <h1>Witaj {$authStore.userData}!</h1>
    </div>
{:else}
    <p>{error}</p>
    <div class="col-12 col-md-4">
        <h2 class="my-4">Login</h2>
    
        <form on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
                <input class="form-control" type="text" placeholder="username" bind:value={username}>
            </div>
            <div class="mb-3">
                <input class="form-control" type="password" placeholder="password" bind:value={password} autocomplete="on">
            </div>
    
            <button class="btn btn-primary" type="submit">Login</button>
        </form>
    </div>
{/if}