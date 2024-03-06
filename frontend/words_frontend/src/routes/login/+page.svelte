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
            });

            if (response.ok) {
                const data = await response.json();
                setLoggedIn(true, data.username, data.id);
            } else {
                const data = await response.json();
                throw new Error(data.error);
            }
        } catch (error) {
            console.error(error);
            error = 'Błąd logowania. Spróbuj ponownie.';
        }
    };/*
    onMount(() => {
        if(!$authStore.loggedIn){
            fetch('http://localhost:8000/check_login_status/')
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    } else if (response.status === 401) {
                        throw new Error('Nieautoryzowany');
                    } else {
                        throw new Error('Błąd podczas sprawdzania statusu logowania');
                    }
                })
                .then(data => {
                    setLoggedIn(true, data.username);
                    goto('/');
                })
                .catch(error => {
                    console.error(error);
                    if (error.message === 'Nieautoryzowany') {
                        // Obsługa błędu 401
                    }
                });
        }
    });*/
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
                <input class="form-control" type="password" placeholder="password" bind:value={password}>
            </div>
    
            <button class="btn btn-primary" type="submit">Login</button>
        </form>
    </div>
{/if}