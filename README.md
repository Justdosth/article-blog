# Django Blog Project

This is a simple Django project for managing a blog, including articles and comments.

## Project Structure

- **myblog/**
  - **blog/**
    - **migrations/**
    - **templates/**
      - **blog/**
        - `article_details.html`
        - `article_list.html`
        - `comment_list.html`
        - `view_comments.html`
    - `__init__.py`
    - `admin.py`
    - `apps.py`
    - `models.py`
    - `permissions.py`
    - `serializers.py`
    - `urls.py`
    - `views.py`
  - `__init__.py`
  - `asgi.py`
  - `settings.py`
  - `urls.py`
  - `wsgi.py`
- `db.sqlite3`
- `manage.py`

## Features

- Display a list of articles
- Display details of an individual article
- Filter articles based on topic
- Submit comments for articles
- View comments directly on the article details page

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-django-blog.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-django-blog
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The blog will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

- Navigate to [http://127.0.0.1:8000/api/articles/](http://127.0.0.1:8000/api/articles/) to view the list of articles.
- Explore the various API endpoints for managing articles and comments.
- Click on "View Comments" in the article details page to view and add comments.

## Contributing

Contributions are welcome! If you have any suggestions or find issues, feel free to open an [issue](https://github.com/your-username/your-django-blog/issues) or submit a [pull request](https://github.com/your-username/your-django-blog/pulls).
