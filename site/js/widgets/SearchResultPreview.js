class SearchResultPreview extends HTMLElement {
    styleSheet = '../../css/SearchResultPreview.css';

    constructor() {
        super();

        this.attachShadow({mode: 'open'});
    }
    
    static get observedAttributes() {
        return ['title', 'description', 'art'];
    }

    get title () {
        return this.getAttribute('title');
    }

    get description () {
        return this.getAttribute('description');
    }

    get art () {
        return this.getAttribute('art');
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (!oldValue || newValue != oldValue) {
            this.render();
        }
    }

    render() {
        const template = 
        `<style> @import "${this.styleSheet}"; </style>
        <div class="SearchResultPreview" onclick="location.href='TODO'">
            <h1>${this.title}</h1>
            <div class="row-align">
                <img src='${this.art}'>
                <p>${this.description}</p>
            </div>
        </div>`
        
        this.shadowRoot.innerHTML = template;          
    }
}
      
customElements.define('search-result-preview', SearchResultPreview);