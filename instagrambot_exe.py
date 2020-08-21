from main import *
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Instagram Automation Bot")
root.geometry("500x750")


def login_phase(driver, username, password):
    #login_func(driver, username, password)
    get_follower_button = Button(
        root, text="Get Followers Names",  bg="#cce7e8", command=lambda: get_followers_names(driver, username))
    get_follower_button.grid(row=5, column=4, padx=5, pady=5)

    get_following_button = Button(
        root, text="Get Following Names", bg="#cce7e8", command=lambda: get_following_names(driver, username))
    get_following_button.grid(row=6, column=4, padx=5, pady=5)

    get_not_following_back_button = Button(
        root, text="Get Not Following Back Names", bg="#cce7e8", command=lambda: names_not_following_back("followers_names.txt", "following_names.txt"))
    get_not_following_back_button.grid(
        row=7, column=4, padx=5, pady=5)

    unfollow_button = Button(root, text="Unfollow With File", bg="#cce7e8",
                             command=lambda: unfollow_with_file(driver, "not_following_back.txt"))
    unfollow_button.grid(row=8, column=4, padx=5, pady=5)
    Label(root, text="Hashtags:").grid(row=9, column=3)
    hashtags = Entry(root, bd=3)
    hashtags.grid(row=9, column=4)

    like_button = Button(root, text="Like With Hashtags",  bg="#e07b39",
                         command=lambda: like_with_hashtags(driver, hashtags.get()))
    like_button.grid(row=10, column=4, padx=5, pady=5)

    comment_button = Button(
        root, text="Comment With Hashtags", bg="#e07b39", command=lambda: only_comments(driver, hashtags.get()))
    comment_button.grid(column=4, padx=5, pady=5)

    follow_button = Button(root, text="Follow With Hashtag", bg="#e07b39",
                           command=lambda: follow_with_hashtags(driver, hashtags.get()))
    follow_button.grid(column=4, padx=5, pady=5)

    like_comment_follow_button = Button(
        root, text="Like, Comment and  Follow", bg="#e07b39", command=lambda: like_comment_follow_func(driver, hashtags.get()))
    like_comment_follow_button.grid(column=4, padx=5, pady=5)


def StartAutomation():
    driver = webdriver.Chrome("C:/setups/chromedriver_win32/chromedriver.exe")
    url = "https://www.instagram.com/"
    driver.get(url)
    time.sleep(2)

    Label(root, text="username:").grid(row=2, column=3)
    username_input = Entry(root, bd=5)
    username_input.grid(row=2, column=4)
    # PAssword input section
    password_input = Entry(root, bd=5, show="*")

    Label(root, text="password:").grid(row=3, column=3)

    password_input.grid(row=3, column=4)

    LoginButton = Button(root, bg="light blue", text="Login", command=lambda: login_phase(
        driver, username_input.get(), password_input.get()))

    LoginButton.grid(row=4, column=4, pady=5, padx=5)


file = Image.open("Image.jpg")
file = file.resize((200, 200), Image.ANTIALIAS)
Image = ImageTk.PhotoImage(file)  # <---
ImageLabel = Label(root, image=Image)
ImageLabel.image = Image
ImageLabel.grid(row=0, column=2, ipadx=150, columnspan=16)
StartButton = Button(root, text="Start Browser", command=StartAutomation)
StartButton.grid(row=1, column=2, ipadx=20, pady=10, columnspan=16)
Label(root,
      text="Created by Hilmi Cihan Yıldırım",
      fg="light green",
      bg="dark green",
      font="Helvetica 16 bold italic").place(
    relx=0.5, rely=0.95, anchor=CENTER)

root.mainloop()
