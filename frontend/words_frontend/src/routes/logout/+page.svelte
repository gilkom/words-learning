<script>
    import {WordStore} from '../../word-store'
    import {onMount} from 'svelte'
    import { authStore,  logout as logoutAction } from '../../stores/auth.js';
    import { goto } from '$app/navigation';
    import { UserWordStore } from '../../user-word-store.js';


    const allStores = [authStore, WordStore, UserWordStore];

    onMount(async function () {

        try {
            const response = await fetch('http://localhost:8000/logout/', {
                method: 'POST', // Zakładając, że wylogowanie wymaga metody POST
                headers: {
                    'Content-Type': 'application/json'
                },
                mode: 'cors',
            });

            if (response.ok) {
                logoutAction(); // Wylogowanie użytkownika z użyciem funkcji z store
                allStores.forEach(store => store.reset({}));
                goto('/login'); // Przekierowanie na stronę logowania po wylogowaniu
            } else {
                throw new Error('Błąd podczas wylogowywania');
            }
        } catch (error) {
            console.error(error);
            // Obsługa błędu wylogowywania
        }
    })

</script>