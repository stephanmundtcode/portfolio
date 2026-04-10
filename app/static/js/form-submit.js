document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.contact-form form');

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
                form.classList.add('hidden');
            } else {
                console.error('Error:', response);
            }
        })
    })
});