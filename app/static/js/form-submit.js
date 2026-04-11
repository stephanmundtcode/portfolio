document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.contact-form form');
    const formDiv = document.querySelector('.contact-form');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(form);

        console.log(formData);

        fetch('/contact', {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                console.log('Form submitted successfully', form);
                formDiv.classList.add('hidden');
                document.getElementById('formFeedback').classList.remove('hidden');
                document.getElementById('main-content-2').classList.remove('hidden');
                initTypingGame()
            } else {
                console.error('Error:', response);
            }
        });
    });

    // Typing Speed Test
    const sentences = [
        "The best way to predict the future is to invent it, and the only way to do that is to start building before you feel ready.",
        "Code is like humor. When you have to explain it, it is bad. Write code that tells a story anyone on your team can follow without a map.",
        "First, solve the problem clearly in your head. Then write the code. Jumping straight to the keyboard is how bugs are born before a single line runs.",
        "Experience is the name everyone gives to their mistakes, and the best engineers are simply those who have made more of them and learned from every single one.",
        "In order to be irreplaceable, one must always be different and willing to take on the problems that everyone else has decided are too difficult to bother with.",
    ];

    let startTime = null;
    let timerInterval = null;
    let gameActive = false;

    function initTypingGame() {
        const gameContainer = document.querySelector('#typingGame');
        if (!gameContainer) return;

        const fullSentence = sentences[Math.floor(Math.random() * sentences.length)];
        const split_sentence = fullSentence.split(" ");
        const span_sentence = split_sentence.map((word, index) => {
            return `<span id="word-${index}">${word}</span>`;
        });
        const sentence = span_sentence.join(" ");

        document.querySelector('#typingTarget').innerHTML = sentence;

        const input = document.querySelector('#typingInput');
        const stats = document.querySelector('#typingStats');
        const wpmResult = document.querySelector('#wpmResult');
        const timeResult = document.querySelector('#timeResult');
        const retryBtn = document.querySelector('#retryBtn');

        input.addEventListener('input', () => {

            //timer start
            if (!gameActive) {
                gameActive = true;
                startTime = Date.now();
            }

            const typed = input.value;
            const target = sentence;

            //check if the word is correct
            input.value.split(" ").slice(0, -1).forEach((word, index) => {

                if (split_sentence[index] === word) {
                    document.querySelector(`#word-${index}`).classList.remove('incorrect');
                    document.querySelector(`#word-${index}`).classList.add('correct');
                } else {
                    document.querySelector(`#word-${index}`).classList.remove('correct');
                    document.querySelector(`#word-${index}`).classList.add('incorrect');
                }
            });
            if (typed === fullSentence) {

                document.querySelector(`#word-${split_sentence.length-1}`).classList.remove('incorrect');
                document.querySelector(`#word-${split_sentence.length-1}`).classList.add('correct');
                
                const elapsed = (Date.now() - startTime) / 1000;
                const words = target.trim().split(" ").length;
                const wpm = Math.round((words / elapsed) * 60);

                input.disabled = true;
                gameActive = false;

                wpmResult.textContent = `${wpm} WPM`;
                timeResult.textContent = `${elapsed.toFixed(1)}s`;
                stats.classList.remove('hidden');
            }
        });

        retryBtn.addEventListener('click', () => {
            gameActive = false;
            startTime = null;
            input.disabled = false;
            input.value = "";
            input.focus();
            stats.classList.add('hidden');
            initTypingGame();
        });
    }
});