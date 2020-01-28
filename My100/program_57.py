# 57. Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

x=input()
i=x.index('@')
j=x.index('.')
#prints user name from email
print(x[:i])
#prints company name from email
print(x[i+1:j])