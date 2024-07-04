import json
import datetime

class User:
    def __init__(self, username):
        self.u = username
        self.p = []
        self.lps = []

    def cp(self, c):
        p = {"u": self.u, "c": c, "l": [], "cm": []}
        self.p.append(p)
        return p

    def rt(self):
        if len(self.p) > 0:
            for i, po in enumerate(self.p):
                print u"Post {}:\n{}".format(i, po)
        else:
            print u"No posts to display."

    def lp(self, post):
        if post not in self.lps:
            self.lps.append(post)
            post["l"].append(self.u)
            print "Post liked successfully."
        else:
            print "You have already liked this post."

    def cop(self, p, c):
        p["cm"].append({"u": self.u, "c": c})

class SM:
    def __init__(self):
        self.u = {}

    def cu(self, u):
        if u not in self.u:
            self.u[u] = User(u)
        else:
            print "User already exists."

    def gu(self, u):
        return self.u.get(u)

    def mm(self):
        while True:
            print "Social Media Platform"
            print "1. Create User"
            print "2. Create Post"
            print "3. View Timeline"
            print "4. Like a Post"
            print "5. Comment on a Post"
            print "6. Exit"
            c = raw_input("Enter your choice: ")
            if c == '1':
                u = raw_input("Enter username: ")
                self.cu(u)
            elif c == '2':
                u = raw_input("Enter username: ")
                us = self.gu(u)
                if us:
                    c = raw_input("Enter post content: ")
                    p = us.cp(c)
                    print "Post created by {} with content: {}".format(p['u'], p['c'])
                else:
                    print "User not found."
            elif c == '3':
                u = raw_input("Enter username: ")
                us = self.gu(u)
                if us:
                    us.rt()
                else:
                    print "User not found."
            elif c == '4':
                u = raw_input("Enter username: ")
                us = self.gu(u)
                if us:
                    pi = int(input("Enter the post index you want to like: "))
                    au = raw_input("Enter the author's username: ")
                    auu = self.gu(au)
                    if auu:
                        us.lp(auu.p[pi])
                    else:
                        print "Author not found."
                else:
                    print "User not found."
            elif c == '5':
                u = raw_input("Enter username: ")
                us = self.gu(u)
                if us:
                    pi = int(input("Enter the post index you want to comment on: "))
                    au = raw_input("Enter the author's username: ")
                    auu = self.gu(au)
                    if auu:
                        co = raw_input("Enter your comment: ")
                        us.cop(auu.p[pi], co)
                    else:
                        print "Author not found."
                else:
                    print "User not found."
            elif c == '6':
                break
            else:
                print "Invalid choice. Please enter a valid option."

def main():
    s = SM()
    s.mm()

if __name__ == "__main__":
    main()
