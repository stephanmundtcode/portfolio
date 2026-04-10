document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.contact-form form');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        form.classList.add('hidden');
    })
});