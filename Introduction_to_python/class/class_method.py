class Phone:
    price=1200
    color='black'
    brand='Apple'

    def call(self):
        print('Calling...')

    def send_sms(self,phone,sms):
        text=f"Sending SMS To : {phone+5}"
        print(text)

myphone=Phone()
result=myphone.send_sms(41524,'How are you?')
print(result)