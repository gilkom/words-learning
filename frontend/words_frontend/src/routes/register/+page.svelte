<script>
    import {goto} from '$app/navigation';
    let username = ''
    let password = ''
    let errors = {}

    let handleSubmit = () => {
        const endpoint = 'http://localhost:8000/register/'
        const requestOptions = {
            method: "POST",
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username: username, password: password})
        }
        
        fetch(endpoint, requestOptions)
            .then(response => response.json().then(data => ({status: response.status, body:data})))
            .then(data =>{
                if(data.status === 201){
                    goto('/register/success/')
                }else{
                    errors = data.body
                    console.log(data)
                }
            })
    }
</script>


<div class="col-12 col-md-4">  
    <h2 class ="my-4">Register</h2>

    <form on:submit|preventDefault={handleSubmit}>
        <div class="mb-3">
            <input class="form-control" type="text" placeholder="username" bind:value={username}>

            {#if errors && errors.username }
                <p class="text-danger">{errors.username[0]}</p>
            {/if}
        </div>
        <div class="mb-3">
            <input class="form-control" type="text" placeholder="password" bind:value={password}>

            {#if errors && errors.password }
                <p class="text-danger">{errors.password[0]}</p>
            {/if}
        </div>

        <button class="btn btn-primary" type="submit">Register</button>
    </form>
</div>