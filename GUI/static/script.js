async function fetchResults() {
    try {
        const response = await fetch('/api/results');
        const data = await response.json();

        const container = document.querySelector('.previouslyScraped');
        container.innerHTML = "<h2 class='previouslyScrapedH2'>Poprzednio przeszukane:</h2>";

        data.forEach(result => {
            const div = document.createElement('div');
            div.className = 'Result';

            const headersList = result.headers.map(h => `<li class='ResultLI'>${h}</li>`).join('');
            const linksList = result.links.map(link => `<li class='ResultLI'><a href="${link}" target="_blank">${link}</a></li>`).join('');
            const emailsList = result.emails.map(e => `<li>${e}</li>`).join('');

            div.innerHTML = `
                <h3 class='ResultH3'>URL: ${result.url}</h3>
                <p class='ResultTitle'>Tytuł: ${result.title}</p>
                <p class='ResultP'>Nagłówki:</p>
                <ul class='ResultList'>${headersList}</ul>
                <p class='ResultP'>Linki:</p>
                <ul class='ResultList'>${linksList}</ul>
                <p class='ResultP'>Maile:</p>
                <ul class='ResultList'>${emailsList}</ul>
            `;

            container.appendChild(div);
        });

    } catch (err) {
        console.error('Błąd podczas pobierania wyników:', err);
    }
}

setInterval(fetchResults, 5000);
window.onload = fetchResults;