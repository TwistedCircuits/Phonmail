import twint

search = input("What do you want to search for:")
user = input("Who do you want these tweets to be from:")

c = twint.Config
c.Search = search
c.User = user

twint.run.Search(c)