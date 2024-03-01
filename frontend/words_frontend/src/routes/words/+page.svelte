<script>
    import {WordStore} from '../../word-store'
    import {onMount} from 'svelte'

    onMount(async function () {
        if (!$WordStore.length) {
            const endpoint = 'http://localhost:8000/words/'
            const response = await fetch(endpoint)
            const data = await response.json() 
            WordStore.set(data)
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