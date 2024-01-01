// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
    // hljs.highlightAll();

    // Select all close buttons
    let alertCloseButtons = document.querySelectorAll('.alert__close');

    // Iterate through each close button and add click event
    alertCloseButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            this.parentElement.style.display = 'none';
        });
    });
});
