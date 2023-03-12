import smtplib

email = "pythontest1234567890math@gmail.com"
password = "Can not disclose"

yeorna = input("Do You Have left Overs You Want To Donate (yes or no) : ").lower()
if yeorna == "yes":
    place = input("Where to pick up the left overs :")
    food = input("Description of the food : ")
    when = input("When to pcik it up : ")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        #This Will Not work because I did not put my password correct
        connection.login(email, password)
        connection.sendmail(from_addr="example/notreal@gmail.com", to_addrs=email, msg = f"Hello,\n Go To {place}, if you want free food({food}) at {when}")