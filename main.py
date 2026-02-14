import sqlite3
from datetime import datetime

def connect_db():
    #Connects to the SQLite database.
    #If the database does not exist, it will be created.
    return sqlite3.connect("community_help.db")

def create_table():
    #Creates the posts table if it does not already exist.
    conn = connect_db()
    cursor = conn.cursor()

    # SQL command to create the posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            date_posted TEXT NOT NULL
        )
    """)

    # Save changes and close connection
    conn.commit()
    conn.close()

def add_post():
    #Adds a new help post to the database.
    title = input("Enter post title: ")
    description = input("Enter description: ")
    category = input("Enter category: ")
    # Get current date and time
    date_posted = datetime.now().strftime("%Y-%m-%d")

    conn = connect_db()
    cursor = conn.cursor()

    # Insert new record into database
    cursor.execute("""
        INSERT INTO posts (title, description, category, date_posted)
        VALUES (?, ?, ?, ?)
    """, (title, description, category, date_posted))

    conn.commit()
    conn.close()

    print("Post added successfully.\n")

def view_posts():
    #Displays all help posts stored in the database.
    conn = connect_db()
    cursor = conn.cursor()

    # Select all posts
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    conn.close()

    if not posts:
        print("No posts found.\n")
        return

    # Loop through and display each post
    for post in posts:
        print(f"ID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Description: {post[2]}")
        print(f"Category: {post[3]}")
        print(f"Date Posted: {post[4]}")
        print("-" * 30)

def update_post():
    #Updates an existing post by ID.
    post_id = input("Enter the ID of the post to update: ")

    new_title = input("Enter new title: ")
    new_description = input("Enter new description: ")
    new_category = input("Enter new category: ")

    conn = connect_db()
    cursor = conn.cursor()

    # Update SQL command
    cursor.execute("""
        UPDATE posts
        SET title = ?, description = ?, category = ?
        WHERE id = ?
    """, (new_title, new_description, new_category, post_id))

    conn.commit()
    conn.close()

    print("Post updated successfully.\n")

def delete_post():
    #Deletes a post from the database using its ID.
    post_id = input("Enter the ID of the post to delete: ")

    conn = connect_db()
    cursor = conn.cursor()

    # Delete SQL command
    cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))

    conn.commit()
    conn.close()

    print("Post deleted successfully.\n")

def filter_posts_by_date():
    #Displays posts within a specific date range.
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()

    # Select posts between two dates
    cursor.execute("""
        SELECT * FROM posts
        WHERE date_posted BETWEEN ? AND ?
    """, (start_date, end_date))

    posts = cursor.fetchall()
    conn.close()

    if not posts:
        print("No posts found in this date range.\n")
        return

    for post in posts:
        print(f"ID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Description: {post[2]}")
        print(f"Category: {post[3]}")
        print(f"Date Posted: {post[4]}")
        print("-" * 30)

def filter_by_category():
    # Ask user for category input
    category = input("Enter category to filter (Help Request, Help Offer, Announcement, General): ")
    
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to get posts matching the category
    cursor.execute("""SELECT id, title, description, date_posted FROM posts WHERE category = ?""", (category,))
    posts = cursor.fetchall()
    conn.close()
    
    if not posts:
        print(f"No posts found in category '{category}'.\n")
        return
    
    print(f"\nPosts in category '{category}':\n")
    for post in posts:
        print(f"ID: {post[0]}")
        print(f"Title: {post[1]}")
        print(f"Description: {post[2]}")
        print(f"Date Posted: {post[3]}\n")

# --------------------------------------------------
# Displays the menu options to the user
# --------------------------------------------------
def show_menu():
    print("\nCommunity Help Board")
    print("====================")
    print()
    print("1. Add a post")
    print("2. View all posts")
    print("3. Update a post")
    print("4. Delete a post")
    print("5. Filter posts by date")
    print("6. Filter posts by category")
    print("7. Exit")

# --------------------------------------------------
# Main program loop
# --------------------------------------------------
def main():
    # Ensure database and table exist
    create_table()
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_post()
        elif choice == "2":
            view_posts()
        elif choice == "3":
            update_post()
        elif choice == "4":
            delete_post()
        elif choice == "5":
            filter_posts_by_date()
        elif choice == "6":
            filter_by_category()
        elif choice == "7":
            print("Goodbye! Thanks for using Community Help Board.")
            break
        else:
            print("Please enter a valid number from the menu.")


# --------------------------------------------------
# Program entry point
# --------------------------------------------------
main()