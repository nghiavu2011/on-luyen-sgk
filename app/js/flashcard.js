let cards = [];
let currentCard = 0;

async function initFlashcards() {
    try {
        const params = getUrlParams();
        const res = await smartFetch(`content/grade-${params.grade}/${params.subject}/${params.chapter}-flashcards.json`);
        if (!res.ok) throw new Error();
        const data = await res.json();
        cards = data.cards || [];
    } catch {
        cards = [
            { front: "Tập hợp là gì?", back: "Một nhóm các đối tượng (phần tử) được xác định rõ ràng." },
            { front: "N = ?", back: "Tập hợp các số tự nhiên: {0, 1, 2, 3, ...}" }
        ];
    }

    renderCard();
}

function renderCard() {
    if (cards.length === 0) return;
    if (currentCard >= cards.length) {
        alert("🎉 Bạn đã ôn xong bộ thẻ này! +10 XP");
        addXP(10);
        history.back();
        return;
    }

    document.getElementById('flashcard').classList.remove('is-flipped');

    const c = cards[currentCard];
    document.getElementById('fc-front').innerHTML = c.front;
    document.getElementById('fc-back').innerHTML = (c.back || '').replace(/\n/g, '<br>');

    if (window.renderMathInElement) {
        renderMathInElement(document.getElementById('flashcard'), {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }

    document.getElementById('fc-counter').innerText = `(${currentCard + 1}/${cards.length})`;
}

function flipCard() {
    document.getElementById('flashcard').classList.toggle('is-flipped');
}

function markCard(known) {
    if (known) addXP(1);
    currentCard++;
    setTimeout(renderCard, 300);
}

document.addEventListener('DOMContentLoaded', initFlashcards);
