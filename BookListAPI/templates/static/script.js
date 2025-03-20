document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0;
    const singleBooks = document.querySelectorAll('.book-container .book');
    const totalBooks = singleBooks.length;

    function showBook(index) {
        singleBooks.forEach((book, i) => {
            book.style.display = (i === index) ? 'block' : 'none';
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

    document.getElementById('toggle-list').addEventListener('click', function() {
        var bookList = document.getElementById('book-list');
        if (bookList.style.display === 'none') { 
            bookList.style.display = 'block'; 
            this.textContent = 'Hide list of books';
        } else { 
            bookList.style.display = 'none'; 
            this.textContent = 'Display list of books';
        } 
    });

    // JavaScript for navigating through individual books
    let currentBookIndex = 0;
    const books = document.querySelectorAll('.book');
    document.getElementById('prev').addEventListener('click', function() {
        books[currentBookIndex].style.display = 'none';
        currentBookIndex = (currentBookIndex - 1 + books.length) % books.length;
        books[currentBookIndex].style.display = 'block';
    });
    document.getElementById('next').addEventListener('click', function() {
        books[currentBookIndex].style.display = 'none';
        currentBookIndex = (currentBookIndex + 1) % books.length;
        books[currentBookIndex].style.display = 'block';
    });

    // Show the first book initially
    showBook(currentIndex);
});