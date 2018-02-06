# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
x=  my_dict.items()
#This next line is to check weather it is a tuple by returning true or false
print isinstance(x[0],tuple)