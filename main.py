import sqlite3
from datetime import datetime

def connect_db():
    """
    Connects to the SQLite database.
    If the database does not exist, it will be created.
    """
    return sqlite3.connect("community_help.db")

def create_table():
    """
    Creates the posts table if it does not already exist.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            date_posted TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_post():
    """
    Adds a new help post to the database.
    """
    title = input("Enter post title: ")
    description = input("Enter description: ")
    category = input("Enter category: ")
    date_posted = datetime.now().strftime("%Y-%m-%d")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts (title, description, category, date_posted)
        VALUES (?, ?, ?, ?)
    """, (title, description, category, date_posted))

    conn.commit()
    conn.close()

    print("Post added successfully.\n")

def view_posts():
    """
    Displays all help posts stored in the database.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    conn.close()

    if not posts:
        print("No posts found.\n")
        return

    for post in posts:
        print(f"ID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Description: {post[2]}")
        print(f"Category: {post[3]}")
        print(f"Date Posted: {post[4]}")
        print("-" * 30)

def show_menu():
    print("\nCommunity Help Board")
    print("====================")
    print()
    print("1. Add a post")
    print("2. View all posts")
    print("3. Exit")

def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
