<script>
    import {WordStore} from '../../word-store'
    import {onMount} from 'svelte'
    import { authStore } from '../../stores/auth.js';
    import { goto } from '$app/navigation';


    onMount(async function () {
        console.log("1")
        if (!$WordStore.length) {
            console.log("2")
            if (!$authStore.loggedIn){
                console.log("3")
                goto('/login');
                return;
            }

            try {
                console.log("4")
            const endpoint = 'http://localhost:8000/words/';
            const response = await fetch(endpoint, {
                method: 'GET',
                headers: {
                'Content-Type': 'application/json',      
                },
                mode: 'cors',
                credentials: 'include' 
            });
            console.log('ffloggedIn:', $authStore.loggedIn);
            const data = await response.json();
            WordStore.set(data);
            }catch(error){
                console.error(error);
            }
        }
    })

    let handleDelete = (id) => {
        const endpoint = `http://localhost:8000/words/${id}`
        fetch(endpoint, {method: 'DELETE'}).then(response => {
            if (response.status == 204) {
                WordStore.update(prev => prev.filter(word => word.word_id != id))
            }
        })
    }
</script>

<div>
    <h2 class="my-4">Word List</h2>
    
    <div class="my-4 row">
        {#each $WordStore as word}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">Word: { word.word }</h5>
                        <p class="card-text">Translation: { word.translation }</p>
                        <p class="card-text">Example: { word.example_sentence }</p>
                    </div>
                    <div>
                        <a href="/words/{word.word_id}" class="btn btn-primary">View</a>

                        <button on:click={() => handleDelete(word.word_id)} class="btn btn-danger ml-2">
                            Delete 
                        </button>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>