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
   <li><strong>View Books</strong>: Class-based view to look at books in the library with filtering, sorting, and searching capabilities.</li>
   <li><strong>Add Books</strong>: Allows adding new books to the library.</li>
   <li><strong>Update/Delete Books</strong>: Enables updating or deleting books in the database.</li>
   <li><strong>Index Page</strong>: Connects to index.html.</li>
   <li><strong>Library Page</strong>: Connects to library.html to display books.</li>
</ul>


<h4> Best Practices </h4>
<h5> This project follows best practices for creating a RESTful API using Django and Django REST Framework. It includes:</h5>

<ul>
  <li>Pagination: Displays books 10 per page.</li>
  <li>Filtering and Searching: Allows ordering by rating and author, and searching by title, author, and rating.</li>
</ul>

<h4> Installation </h4>
 <ol>
      <li>Clone the repository:
      <pre><code>git clone https://github.com/yourusername/BookList.git</code></pre>
  </li>
      <li>Navigate to the project directory:
      <pre><code>cd BookList</code></pre>
  </li>
      <li>Install the required packages:
      <pre><code>pip install -r requirements.txt</code></pre>
  </li>
      <li>Run the development server:
      <pre><code>python manage.py runserver</code></pre>
  </li>
</ol>

<h4>Usage</h4>

<p>Access the API endpoints to manage your book collection.</p>
<p>Visit the index and library pages to view the books.</p>
