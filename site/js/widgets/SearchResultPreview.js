class SearchResultPreview extends HTMLElement {
    // styleSheet = '../../css/DashboardEntry.css';

    constructor() {
        super();
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
        // `<style> @import "${this.styleSheet}"; </style>
        `<div class="SearchResultPreview" onclick="location.href='TODO'">
            <h1>${this.title}</h1>
            <p>${this.description}</p>
            <img src='${this.art}'>
        </div>`
        
        this.innerHTML = template;          
    }
}
      
customElements.define('search-result-preview', SearchResultPreview);