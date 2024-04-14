<script>
    import {WordStore} from '../../word-store'
    import {onMount} from 'svelte'
    import { authStore,  logout as logoutAction } from '../../stores/auth.js';
    import { goto } from '$app/navigation';
    import { UserWordStore } from '../../user-word-store.js';


    const allStores = [authStore, WordStore, UserWordStore];


    const handleLogout = async () => {
        try {
            const response = await fetch('http://localhost:8000/logout/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',    
                },
                //body: JSON.stringify({ username, password }),
                mode: 'cors',
                credentials: 'include',                
            });

            if (response.ok) {
                const data = await response.json();
                //setLoggedIn(true, data.username, data.id);
                console.log("user:", data.username)
                console.log("id:", data.id)
                logoutAction(); // Wylogowanie użytkownika z użyciem funkcji z store
                allStores.forEach(store => store.set([]));
            } else {
                const data = await response.json();
                throw new Error(data.error);
            }
        } catch (error) {
            console.error(error);
            error = 'Błąd logowania. Spróbuj ponownie.';
        }
    };
   /* export async function handleLogout() {
        console.log("Zawartość obiektu request:");
        console.log("isLoggedIn:", $authStore.loggedIn);
        console.log("User ID:", $authStore.userId);
        console.log("Username:", $authStore.username);
        console.log("Access Token:", $authStore.accessToken);
        console.log("CSRF Token:", $authStore.csrfToken);
        const csrftoken = cookies.get('csrftoken');
        if (!$authStore.loggedIn){
                console.log("!!!!!svelte 1Gilo")
                goto('/login');
                return;
            }
        console.log("!!!!!svelte response poczatek!!!!!")
        try {
            console.log("!!!!!svelte response srodek!!!!!")
            console.log("x-csrftoken:", $authStore.csrfToken);
            const response = await fetch('http://localhost:8000/logout/', {
                method: 'POST', // Zakładając, że wylogowanie wymaga metody POST
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                mode: 'cors',
                //credentials: 'include',  
            });
            console.log("Headers in the request:");
            for (let [key, value] of response.headers) {
                console.log(`${key}: ${value}`);
            }

            if (response.ok) {
                console.log("!!!!!svelte response jest ok!!!!!")
                logoutAction(); // Wylogowanie użytkownika z użyciem funkcji z store
                allStores.forEach(store => store.set([]));
                //document.cookie = 'sessionid=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';  // Usunięcie ciasteczka sessionid
                //document.cookie = 'csrftoken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';  // Usunięcie ciasteczka csrftoken
                goto('/login'); // Przekierowanie na stronę logowania po wylogowaniu
            } else {
                throw new Error('Błąd podczas wylogowywania');
            }
        } catch (error) {
            console.error(error);
            // Obsługa błędu wylogowywania
        }
    }*/

</script>


<div>
    <h1>Witaj {$authStore.userData}!</h1>
    <button on:click={handleLogout}>Wyloguj</button>
</div>