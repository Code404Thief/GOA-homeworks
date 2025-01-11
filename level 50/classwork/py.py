                  # Classwork


# # Level 50:
# 1) ჩამოთვალეთ ყველა დღეს ნასწავლი error'ის ტიპი და ახსენით რა რა შემთხვევაში გამოდის
# 2) დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით
# 3) დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით
# 4) დაწერეთ ისეთი კოდი სადაც იქნება ValueError და გაუმკლავდით try/except'ით
# 5) კომენტარებით ახსენით რაში გვადგება try/except
                  
                       #write
# 1. არის indexerror- როცა არასწორ ინდექსის გამოყენებას ცდილობთ მაგრამ ეს ინდექსი არ არსებობს, valueerror- როცა მაგალითად რიცხვებში ასოა და ინტად ვერ გამოიტან, nameerror- როცა ცვლადი არ არსებობს რომლის გამოყენებაც ცადეთ, typeerror- როცა არასწორი არგუმენტია. syntaxerror- მაგალითად როცა print"Hello" გიწერია და ფრჩხილები არ გაქვს
try:
    print(x)
except NameError:
    print("NameError: 'x' not found")

y = [1, 2, 3]
try:
    print(y[4])
except IndexError:
    print("no index 4")

try:
    int("543a2")
except ValueError:
    print("theres an error in values")

# try/except is used when there could be an error but you want to still continue the code
