# string = სიტყვის ტიპი
# int = რიცხვის ტიპი
# float = ათწილადის ტიპი
# boolean = true თუ false ტიპი

# string-ის integer-ად გადაქცევა გვჭირდება რომ მოცემული რიცხვი არ წაიკითხოს სიტყვად არამედ რიცხვად, რომელიც საჭიროა რიცხვის გამოყენებისთვის
x =input("შემოიტანეთ რაიმე")
if x.isdigit()==True:
    print("თქვენი შემოტანილი რიცხვი არის რიცხვი")
elif x.replace(".", "").isdigit()==True and x.count(".")==1:
    print("თქვენი შემოტანილი რიცხვი ათწილადია")
elif x=="True" or x=="False":
    print("თქვენი შემოტანილი არის სიმართლე ან ტყუილი")
else:
    print("თქვენი შემოტანილი სტრინგია")

print(10 < 1)
# გამოიტანა False რადგან print-ში boolean წერია და არასწორია