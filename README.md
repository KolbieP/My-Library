<h1>My Library</h1>

<h2> BookList Project </h2>

<h4> Overview </h4>

<p>The BookList project is a Django-based web application that stores the books you have read in a database. 
  It provides a RESTful API to manage your book collection, allowing you to add, view, update, and delete books.</p>

<h4> Project Details </h4>

<ul>
  <li>Framework: Django 5.0</li>
  <li>Language: Python</li>
  <li>Database: SQLite (db.sqlite3)</li>
</ul>

<h4> Features </h4>

<ul>
  <li>View Books: Class-based view to look at books in the library with filtering, sorting, and searching capabilities.</li>
  <li>Add Books: Allows adding new books to the library.</li>
  <li>Update/Delete Books: Enables updating or deleting books in the database.</li>
  <li>Index Page: Connects to index.html.</li>
  <li>Library Page: Connects to library.html to display books.</li>
</ul>


<h4> Best Practices </h4>
<h5> This project follows best practices for creating a RESTful API using Django and Django REST Framework. It includes:</h5>

<ul>
  <li>Pagination: Displays books 10 per page.</li>
  <li>Filtering and Searching: Allows ordering by rating and author, and searching by title, author, and rating.</li>
</ul>

<h4> Installation </h4>

<p> Clone the repository: </p>
<p><i>git clone https://github.com/yourusername/BookList.git</i></p>
<p>Navigate to the project directory:</p>
<p><i>cd BookList</i></p>
<p>Install the required packages:</p>
<p><i>pip install -r requirements.txt</i></p>
<p>Run the development server:</p>
<p><i>python manage.py runserver</i></p>

<h4>Usage</h4>

<p>Access the API endpoints to manage your book collection.</p>
<p>Visit the index and library pages to view the books.</p>
