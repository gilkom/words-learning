<!--<script>
    import {goto} from '$app/navigation';
    let username = ''
    let password = ''
    let errors = {}

    let handleSubmit = () => {
        const endpoint = 'http://localhost:8000/login/'
        const requestOptions = {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: username, password: password})
        }

        fetch(endpoint, requestOptions)
            .then(response => response.text().then(data => ({status: response.status, body:data})))
            .then(data =>{
                if(data.status === 202){
                    console.log(data)
                    goto('/')
                }else{
                    errors = data.body
                    console.log(data)
                }
            })
    }
</script>


<div class="col-12 col-md-4">
    <h2 class ="my-4">Login</h2>

    <form on:submit|preventDefault={handleSubmit}>
        <div class="mb-3">
            <input class="form-control" type="text" placeholder="username" bind:value={username}>

            {#if errors && errors.username }
                <p class="text-danger">{errors.username[0]}</p>
            {/if}
        </div>
        <div class="mb-3">
            <input class="form-control" type="password" placeholder="password" bind:value={password}>

            {#if errors && errors.password }
                <p class="text-danger">{errors.password[0]}</p>
            {/if}
        </div>
        {#if errors && errors.general}
            <div class="mb-3">
                <p class="text-danger">{errors.general[0]}</p>
            </div>
        {/if}

        <button class="btn btn-primary" type="submit">Login</button>
    </form>
</div>
-->
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
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const data = await response.json();
                setLoggedIn(true, data.username);
                //goto('/');
            } else {
                const data = await response.json();
                throw new Error(data.error);
            }
        } catch (error) {
            console.error(error);
            error = 'Błąd logowania. Spróbuj ponownie.';
        }
    };

    const logout = async () => {
        try {
            const response = await fetch('http://localhost:8000/logout/', {
                method: 'POST', // Zakładając, że wylogowanie wymaga metody POST
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            if (response.ok) {
                logoutAction(); // Wylogowanie użytkownika z użyciem funkcji z store
                goto('/login'); // Przekierowanie na stronę logowania po wylogowaniu
            } else {
                throw new Error('Błąd podczas wylogowywania');
            }
        } catch (error) {
            console.error(error);
            // Obsługa błędu wylogowywania
        }
    };

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
    });
</script>

{#if $authStore.loggedIn}
    <div>
        <h1>Witaj {$authStore.userData}!</h1>
        <button on:click={logout}>Wyloguj</button>
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
