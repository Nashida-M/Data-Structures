# list of  available cars and their prices in a dealership
#import numpy as np
brands=('mercedesBenz, toyota, bmw, hyundai, honda')
mercedesBenz={"A-Class Sedan":"$35,000", "CLA":"$46,160", "C-Class Coupe":"$59,740",\
              "EQS Sedan":"109,390", "G-Class SUV":"134,300", "E-Class Coupe":"$75,710"}
toyota={"Camry":"$26,220", "Corolla":"$20,425", "4Runner":"$38,105", "bZ4X":"42,000",\
        "C-HR":"$24,280", "GR86":"$27,700"}
bmw={"228 Gran Coupe":"$37,800", "230":"$38,200", "330":"43,800", \
     "Alpina XB7":"$145,000", "iX":"$84,100", "X1":"39,100"}
hyundai={"Elantra":"$20,650", "Sonata":"$25,250", "Venue": "$19,500",\
         "Kona":"$22,140", "Tucson":"$26,700", "SantaFe":"$28,450"}
honda={"Accord":"$27,295", "Civic":"$25,050", "Passport":"$41,100", "HR-V":"$23,800", \
       "CR-V":"$31,610", "Pilot":"$39,150"}
carBrands= input("Please specify the brand of car you want to purchase: ")
if carBrands in brands:
    print("Brand Available") 
    model= input("Please specify model: ")
    if model in mercedesBenz:
        carPrice=mercedesBenz[model]
        print("The price of the MercedesBenz {} is {}".format(model,carPrice))
    elif model in toyota:
        carPrice=toyota[model]
        print("The price of the Toyota {} is {}".format(model,carPrice))
    elif model in bmw:
        carPrice=bmw[model]
        print("The price of the BMW {} is {}".format(model,carPrice))
    elif model in hyundai:
        carPrice=hyundai[model]
        print("The price of the Hyundai {} is {}".format(model,carPrice))
    elif model in honda:
        carPrice=honda[model]
        print("The price of the Honda {} is {}".format(model,carPrice))
    else:
        print("The model you are interested in is NOT available")
else:
    print("Brand NOT available") 

