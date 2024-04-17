<script>
    import {WordStore} from '../../word-store'
    import {onMount} from 'svelte'
    import { authStore,  logout as logoutAction } from '../../stores/auth.js';
    import { goto } from '$app/navigation';
    import { UserWordStore } from '../../user-word-store.js';


    const allStores = [authStore, WordStore, UserWordStore];
/*
    onMount(async function () {
            if (!$authStore.loggedIn){
                goto('/login');
                return;
            }
    })
*/
onMount(async function () {
    if (!$authStore.loggedIn){
                goto('/login');
                return;
            }
        try {
            const response = await fetch('http://localhost:8000/logout/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',    
                },
                mode: 'cors',
                credentials: 'include',                
            });

            if (response.ok) {                
                logoutAction(); // Wylogowanie użytkownika z użyciem funkcji z store
                allStores.forEach(store => store.set([]));
                goto('/login');
            } else {
                const data = await response.json();
                throw new Error(data.error);
            }
        } catch (error) {
            console.error(error);
            error = 'Błąd logowania. Spróbuj ponownie.';
        }
    });
   /* export async function handleLogout() {
        if (!$authStore.loggedIn){
                goto('/login');
                return;
            }
        try {
            const response = await fetch('http://localhost:8000/logout/', {
                method: 'POST', // Zakładając, że wylogowanie wymaga metody POST
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                mode: 'cors',
                //credentials: 'include',  
            });

            if (response.ok) {
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


