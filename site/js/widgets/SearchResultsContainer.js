import './SearchResultPreview.js'

class SearchResultsContainer extends HTMLElement {
    // styleSheet = '../../css/DashboardEntry.css';

    constructor() {
        super();
    }

    connectedCallback() {
        document.addEventListener('search-bar-update', this.debounce((e) => {
            this.searchAniList(e.detail.value);
        }));
    }
    
    static get observedAttributes() {
        return ['search_results'];
    }

    get search_results() {
        return JSON.parse(this.getAttribute('search_results'));
    }

    set search_results(v) {
        this.setAttribute('search_results',JSON.stringify(v));
    }
    
    attributeChangedCallback(name, oldValue, newValue) {
        if (!oldValue || newValue != oldValue) {
            this.render();
        }
    }
  
    render() {
        const template = 
        `<p>Data is In</p>
        <div class="SearchResultContainer">
            ${this.renderPreviews()}
        </div>`
        
        this.innerHTML = template;
    }

    renderPreviews() {
        let previewTemplate = ``;
        this.search_results.forEach(media => {
            previewTemplate += `<search-result-preview title=\"${media.title.native}\"
                                                       description=\"${media.description}\"
                                                       art=\"${media.coverImage.medium}\">
                                </search-result-preview>\n`;
        });
        return previewTemplate;
    }

    searchAniList(search_string) {
        let query = `
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
        }`;

        let variables = {
            page: 1,
            perPage: 5,
            search: search_string
        };

        let url = 'https://graphql.anilist.co';
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
        };

        console.log("Send Request")
        function handleAniListResponse(response) {
            return response.json().then(function (json) {
                return response.ok ? json : Promise.reject(json);
            });
        }
    
        function handleAniListData(response_data) {
            this.search_results = response_data.data.Page.media;
        }
    
        function handleAniListError(error) {
            console.error(error)
        }

        fetch(url, options).then(handleAniListResponse)
                           .then(handleAniListData.bind(this))
                           .catch(handleAniListError);

    }

    debounce(func, timeout = 500) {
        let timer;
        return (...args) => {
            clearTimeout(timer);
            timer = setTimeout(() => { func.apply(this, args); }, timeout);
        };
    }
}
      
customElements.define('search-results-container', SearchResultsContainer);