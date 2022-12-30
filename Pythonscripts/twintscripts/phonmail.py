#Imports
import twint 

#Variables and input
email = input("Do you want twint to scrape for emails. Must input True or False, exactly as typed in this sentence: ")
phone_numbers = input("Do you want twint to scrape for phone_numbers. Must input True or False, exactly as typed in this sentence: ")
limit = input("How many tweets do you want: ")
username = input("What user do you want these tweets to be from: ")

#Twint Config
c = twint.Config()
c.Email = email
c.Phone = phone_numbers
c.Limit = limit
c.Username = username

#Run the script
twint.run.Search(c)
