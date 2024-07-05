
class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.liked_posts = []  
#comment

    def create_post(self, content):
        post = Post(self.username, content)
        self.posts.append(post)
        return post  # Return the created post object

    def view_timeline(self):
        if len(self.posts) > 0:
            for i, post in enumerate(self.posts):
                print(f"Post {i}:\n{post}")
        else:
            print("No posts to display.")

    def like_post(self, post):
        if post not in self.liked_posts:
            self.liked_posts.append(post)  
            post.add_like(self.username)
            print("Post liked successfully.")
        else:
            print("You have already liked this post.")

    def comment_on_post(self, post, comment):
        post.add_comment(self.username, comment)

class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.likes = [] 
        self.comments = []

    def add_like(self, liker_username):
        self.likes.append(liker_username)

    def add_comment(self, commenter_username, comment):
        self.comments.append({"username": commenter_username, "comment": comment})

    def __str__(self):
        post_info = f"{self.username} said: {self.content}\nLikes: {len(self.likes)}, Comments:"
        for comment in self.comments:
            post_info += f"\n- {comment['username']} commented: {comment['comment']}"
        return post_info

class SocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
        else:
            print("User already exists.")

    def get_user(self, username):
        return self.users.get(username)

    def main_menu(self):
        while True:
            print("Social Media Platform")
            print("1. Create User")
            print("2. Create Post")
            print("3. View Timeline")
            print("4. Like a Post")
            print("5. Comment on a Post")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                username = input("Enter username: ")
                self.create_user(username)
            elif choice == '2':
                username = input("Enter your username: ")
                user = self.get_user(username)
                if user:
                    content = input("Enter post content: ")
                    post = user.create_post(content)
                    print(f"Post created by {post.username} with content: {post.content}")
                else:
                    print("User not found.")
            elif choice == '3':
                username = input("Enter your username: ")
                user = self.get_user(username)
                if user:
                    user.view_timeline()
                else:
                    print("User not found.")
            elif choice == '4':
                username = input("Enter your username: ")
                user = self.get_user(username)
                if user:
                    post_index = int(input("Enter the post index you want to like: "))
                    author_username = input("Enter the author's username: ")
                    author = self.get_user(author_username)
                    if author:
                        user.like_post(author.posts[post_index])
                    else:
                        print("Author not found.")
                else:
                    print("User not found.")
            elif choice == '5':
                username = input("Enter your username: ")
                user = self.get_user(username)
                if user:
                    post_index = int(input("Enter the post index you want to comment on: "))
                    author_username = input("Enter the author's username: ")
                    author = self.get_user(author_username)
                    if author:
                        comment = input("Enter your comment: ")
                        user.comment_on_post(author.posts[post_index], comment)
                    else:
                        print("Author not found.")
                else:
                    print("User not found.")
                    
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

def main():
    social_media = SocialMediaPlatform()
    social_media.main_menu()

if __name__ == "__main__":
    main()
