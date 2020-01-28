# 58. Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.

x=input()
# i=x.index('@')
# j=x.index('.')
print(x[((x.index('@'))+1):(x.index('.'))])
