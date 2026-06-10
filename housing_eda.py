import pandas as pd
import matplotlib.pyplot as plt

housing = pd.read_csv(r'housing.csv')

print(housing.shape)
print(housing.head())
print(housing.describe())
print(housing.isnull().sum())

housing['total_bedrooms'] = housing['total_bedrooms'].fillna(housing['total_bedrooms'].median())

#Huspriser
plt.hist(housing['median_house_value'], bins=50)
plt.title('Huspriser')
plt.xlabel('Pris')
plt.ylabel('Antal')
plt.show()

#Pris per läge
housing.boxplot(column='median_house_value', by='ocean_proximity')
plt.title('Pris per läge')
plt.suptitle('')
plt.xticks(rotation=30)
plt.show()

#Inkomst vs pris
plt.scatter(housing['median_income'], housing['median_house_value'], alpha=0.1, s=5)
plt.title('Inkomst vs Pris')
plt.xlabel('Inkomst')
plt.ylabel('Pris')
plt.show()

print(housing['median_income'].corr(housing['median_house_value']))


print("=== Självutvärdering ===")
print()
print("1. Har något varit utmanande?")
print("Jag hade en del strul med Python installationen på Windows där jag inte kunde använda pip i terminalen.")
print("Det slutade med att jag fick installera en äldre version av Python för att få det att fungera ordentligt.")
print("Att påbörja själva EDA arbetet var också lite förvirrande till en början men så fort jag började att skapa")
print("projektet och ladda upp 'housing.csv' så började jag få addons för csv (rainbowcsv) som underlättade")
print("arbetet väldigt mycket. Tillägget visualiserade alla relevant data från csv filen.")
print("Sedan var det bara att börja med enkla funktioner och därefter bygga vidare.")
print()
print("2. Vilket betyg anser jag att jag ska ha?")
print("Jag anser mig själv som godkänd. Jag har inte lagt ner den tiden som krävs för ett VG eftersom")
print("jag fokuserar mer på det fundamentala och att hänga med i kursen.")
print()
print("3. Något jag vill lyfta till Terese:")
print("Det märks att du har genuint kunnande inom ämnet. Du är väldigt pedagogisk och kör ingen överkurs,")
print("du simplifierar alltihop på ett bra sätt. Dock tycker jag att boken borde funnits som E-bok alternativt")
print("att vi visar upp fysisk kopia med tillhörande kvitto så du kan skicka hela e-boken till respektive elev,")
print("då det hade underlättat att koda uppgifterna. Ett annat alternativ är att ha en sida där vi får göra uppgifterna i.")