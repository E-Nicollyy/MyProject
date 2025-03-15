
import pywhatkit
phone_number = "+55 11 95860-1036"
message = "Hello, this is a test message sent using Python!"
hours = 21
minutes = 58
pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
print("Message sent successfully!")