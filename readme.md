# Book Recommendation System

## Overview

This project is a Django-based book recommendation system that allows users to manage their favorite books and receive personalized book recommendations. The system includes models for authors, books, series, and users, with relationships that support various book management and recommendation features.

## Features

- **User Authentication:** Custom user model with the ability to favorite books.
- **Book Management:** Users can browse books, filter by title or author, and manage their favorite books.
- **Recommendations:** Personalized book recommendations based on the user's favorite books.

## How the Recommendation System Works

The recommendation system is designed to suggest books to users based on their current favorites. Here’s how it operates:

1. **Retrieve Favorite Books:**
   - The system first gathers all the books a user has marked as favorites.

2. **Author-Based Recommendations:**
   - It then identifies other books written by the same authors as those of the user's favorite books.
   - These books are recommended unless they are already in the user's favorites.

3. **Keyword-Based Expansion:**
   - If fewer than 5 books are found, the system expands the recommendations by searching for books with similar titles (based on keywords from the user's favorite books).
   - This ensures a minimum of 5 recommendations, providing broader suggestions if the initial author-based recommendations are insufficient.

4. **Final Recommendations:**
   - The system returns the top 5 recommended books, ensuring they are distinct from the user’s existing favorites.

## Prisma Schema

The project uses Prisma as the ORM to manage the database schema. The Prisma schema defines the relationships between authors, books, series, favorites, and users. Here’s an outline of the key relationships:

- **Author and Book:** Many-to-Many relationship, allowing an author to have multiple books and a book to have multiple authors.
- **Series and Book:** One-to-Many relationship, where a series can include multiple books, but a book belongs to only one series.
- **Book and CustomUser (Favoriting):** Many-to-Many relationship, enabling users to favorite multiple books and books to be favorited by multiple users.

### Link to Prisma Documentation

For more information about Prisma and how to use it, please refer to the official Prisma documentation: [Prisma Documentation](https://www.prisma.io/docs/)

## Setup and Installation

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (or any supported database)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
   cd book-recommendation-system

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Configure your database:**

   Update the `DATABASE_URL` in your environment variables with your PostgreSQL connection string.

4. **Run migrations:**

   ```bash
   python manage.py migrate

5. **Start the server:**

   ```bash
   python manage.py runserver

6. **Access the application:**

    Open your web browser and navigate to http://127.0.0.1:8000/.



## Usage

- **Register/Login:** Create an account or log in with your credentials.
- **Browse Books:** Search and browse books by title or author.
- **Favorite Books:** Mark books as your favorites.
- **Recommendations:** Receive personalized book recommendations based on your favorites.