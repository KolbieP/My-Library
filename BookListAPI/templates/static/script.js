document.addEventListener('DOMContentLoaded', function() {
    function toggleLibrary() {
        var bookDisplay = document.getElementById('bookDisplay');
        var button = document.querySelector('.book-button');
        if (bookDisplay.style.display === 'none') {
            bookDisplay.style.display = 'block';
            button.textContent = 'Hide Library';
        } else {
            bookDisplay.style.display = 'none';
            button.textContent = 'Display Library';
        }
    }

    var button = document.querySelector('.book-button');
    if (button) {
        button.addEventListener('click', toggleLibrary);
    }
});

