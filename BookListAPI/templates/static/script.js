document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const books = document.querySelectorAll('.book');
    const totalBooks = books.length;

    function showBook(index) {
        books.forEach((book, i) => {
            book.classList.toggle('active', i === index);
        });
    }

    document.getElementById('prev').addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalBooks - 1;
        showBook(currentIndex);
    });

    document.getElementById('next').addEventListener('click', function() {
        currentIndex = (currentIndex < totalBooks - 1) ? currentIndex + 1 : 0;
        showBook(currentIndex);
    });

    showBook(currentIndex);
});