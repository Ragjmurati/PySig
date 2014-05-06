# Hi there! Welcome to PySig, this is a quick little script I made thats designed to
# help company admins enforce uniform email signatures for employees that use google apps for business. Hope you like!



#Import proper modules for script to communicate with Gmail API 
import gdata.apps.emailsettings.client



#Beginning of script, input name and title 


print 'Welcome to the Signature maker!'

name = input('Please input users full name ')

title = input('Thanks! Now please input their title also' )

username = input('One last thing, now input their gmail username (minus the @domain) ')

confirmation = input('Is all this information correct?(yes/no)')

#Confirm if information is correct, if incorrect ask the user to restart the program
if confirmation == yes:
	print 'Signature updated!'
	print 'oh no! Please restart this program then' 


#Declare Variable of Email Signature and assign it to the premade template
email_signature = """
						

							%(name)s
							%(title)s
							<Company Name>
							<Street Address> | <State, Zip Code>
							<Phone Number> 
							<company website>


					""" % \
					{"name": name, "title": title}


#Log into the administrator account and update the email signature with the previous
# user information


client = gdata.apps.emailsettings.client.EmailSettingsClient(domain='<company domain>')
client.ClientLogin(email='<input admin login email> ', password='<input admin password>', source='<app source (ex: mail.companyname.com)>')
client.UpdateSignature(username=username, signature=email_signature)

print 'Signature updated!'



