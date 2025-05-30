from database import create_table, add_user, get_users, update_user, delete_user

def main():
    print("Setting up the database...")
    create_table()

    print("\nAdding users...")
    add_user("Alice", "alice@example.com", 30)
    add_user("Bob", "bob@example.com", 25)

    print("\nFetching users...")
    users = get_users()
    for user in users:
        print(user)

    print("\nUpdating user...")
    update_user(1, "Alice Smith")

    print("\nUsers after update:")
    users = get_users()
    for user in users:
        print(user)

    print("\nDeleting user with ID 2...")
    delete_user(2)

    print("\nFinal users list:")
    users = get_users()
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
