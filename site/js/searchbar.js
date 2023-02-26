let search_box = document.getElementById("anime-search")
search_box.onkeyup = (e)=>{
    console.log(e.target.value)
    document.dispatchEvent(new CustomEvent('search-bar-update', {
        detail: {
            value: e.target.value,
        },
    }));
}

var query = `
query ($page: Int, $perPage: Int, $search: String) {
    Page(page: $page, perPage: $perPage) {
        media(search: $search, type: ANIME) {
            title {
                english
                native
            }
            description
            genres
            status
            coverImage {
                medium
            }
        }
    }
}`

var variables = {
    page: 1,
    perPage: 5,
    search: "fma"
};

let url = 'https://graphql.anilist.co'
let options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
    body: JSON.stringify({
        query: query,
        variables: variables
    })
}

fetch(url, options).then(handleResponse)
                   .then(handleData)
                   .catch(handleError);

function handleResponse(response) {
    return response.json().then(function (json) {
        return response.ok ? json : Promise.reject(json);
    });
}

function handleData(data) {
    console.log(data)
}

function handleError(error) {
    alert('Error, check console')
    console.error(error)
}