<h1>📚 Book Haven</h1>

<h2>Django Project</h2>
<p><a href="https://kolbiep.pythonanywhere.com/api/" target="_blank">View the Project!</a></p>
<h3>Overview</h3>
<p>
  Book Haven is a Django-based web application that allows users to manage both a personal and a public library of books.
  It features a secure admin panel, a RESTful API, JavaScript-enhanced frontend interactivity, and a dual-database system.
</p>

<h3>Project Details</h3>
<ul>
  <li><strong>Framework:</strong> Django 5.0</li>
  <li><strong>Language:</strong> Python</li>
  <li><strong>Databases:</strong> SQLite (<code>db.sqlite3</code>, <code>public_library.sqlite3</code>)</li>
</ul>

<h3>Key Features</h3>
<ul>
  <li><strong>Admin Authentication:</strong> All write actions (add/edit/delete) are restricted to admin users.</li>
  <li><strong>Dual Library System:</strong> Personal library and public contributions are stored in separate databases.</li>
  <li><strong>Frontend Interactivity:</strong> Toggleable book displays, pop-up messages, JavaScript-based search and filters.</li>
  <li><strong>Django Admin Integration:</strong> Full access to both libraries with multi-DB support.</li>
</ul>

<h3>Frontend Views</h3>
<ul>
  <li><strong>Homepage:</strong> Intro and navigation</li>
  <li><strong>Personal Library:</strong> Single-book viewer, search, and full table</li>
  <li><strong>Public Library:</strong> Browse community books and contribute (admin only)</li>
</ul>

<h3>REST API (powered by Django REST Framework)</h3>
<ul>
  <li><code>GET /books</code> — List all personal library books</li>
  <li><code>POST /add</code> — Add book to personal library (admin only)</li>
  <li><code>PUT/DELETE /books/&lt;id&gt;</code> — Edit/delete books (admin only)</li>
  <li><code>GET /public_library</code> — List public books</li>
  <li><code>POST /public_library/add</code> — Submit a book to the public library (admin only)</li>
  <li><code>GET /all_books</code> — Full book list for frontend carousel</li>
</ul>

<h3>Best Practices</h3>
<p>This project follows Django and REST API best practices, including:</p>
<ul>
  <li>Separation of concerns with dual-database routing</li>
  <li>Admin-only write access using <code>IsAdminUser</code> and <code>@staff_member_required</code></li>
  <li>Custom admin class for multi-DB operations</li>
  <li>Pagination, search, and filtering built into class-based views</li>
</ul>

<h3>Installation</h3>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/KolbieP/BookList.git</code></pre>
  </li>
  <li>Navigate to the project directory:
    <pre><code>cd BookList</code></pre>
  </li>
  <li>Create a virtual environment (optional but recommended):
    <pre><code>python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows</code></pre>
  </li>
  <li>Install the required packages:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Apply database migrations:
    <pre><code>python manage.py migrate
python manage.py migrate --database=public_library</code></pre>
  </li>
  <li>Start the development server:
    <pre><code>python manage.py runserver</code></pre>
  </li>
  <li>(Optional) Create a superuser to access admin:
    <pre><code>python manage.py createsuperuser</code></pre>
  </li>
</ol>

<h3>Usage</h3>
<p>
  Visit <code>/</code> for the homepage, <code>/library</code> for your personal collection, and <code>/public_library</code> to view community-submitted books.
  Use the admin panel at <code>/admin</code> to manage all content securely.
</p>

<h3>Future Plans</h3>
<ul>
  <li>🔐 Add user login/signup functionality</li>
  <li>🌐 Deploy on Render or Railway</li>
  <li>📸 Add support for book cover images</li>
  <li>📬 Build a public submission form with validation</li>
</ul>

<h3>Maintainer</h3>
<p>
  Built by <strong>Kolbie Parker</strong>  
  <br>
  <a href="https://github.com/KolbieP" target="_blank">GitHub Profile</a>
</p>

