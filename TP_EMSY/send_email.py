__author__ = "Pouly Steeve"
__version__ = "0.1"
__maintainer__ = "Pouly Steeve"
__email__ = "steve.pouly@eduvaud.ch"
__status__ = "Prototype"
__date__ = "Avril 2026"

#-----------------------------------------------------
# Importing libraries and modules
#-----------------------------------------------------
import datetime                                                             # Library for date and time related stuff
import math                                                                 # Library for math stuff
import csv                                                                  # Library for csv handling stuff

import send_email

from sensirion_i2c_driver import I2cConnection                              # Sensor driver
from sensirion_i2c_sht.sht4x import Sht4xI2cDevice                          # Sensor driver
from sensirion_i2c_driver.linux_i2c_transceiver import LinuxI2cTransceiver  # Sensor driver


#-----------------------------------------------------
# Declaring the sensor object
#-----------------------------------------------------
sht40 = Sht4xI2cDevice(I2cConnection(LinuxI2cTransceiver('/dev/i2c-2')))

#-----------------------------------------------------
# Declaring functions
#-----------------------------------------------------

def read_sensor():     #fonction d'utilisation des capteur
    try:
        t, rh = sht40.single_shot_measurement()
        # Watch out! t and rh are variable that contain not only the values but also the units.
        # You can print the values with the units (print(t)) or you can also recover only the value
        # by specifying which one: t.degrees_celsius or rh.percent_rh
    except Exception as ex:
        print("Error while recovering sensor values:", ex)
    else:
        return t, rh

    return 0 # In case something went wrong

def calculate_dew_point(temp, humidity):
     # Calculate dew point here
    dp      : float = 0      #Point rosé
    Beta    : float = 17.62  #Coefficient
    Lamda   : float= 243.12  #Coefficient
    cent    : float = 100

    dp = (Lamda * (math.log(humidity/cent) + (Beta * temp / (Lamda + temp)))) / (Beta - (math.log(humidity/cent) + Beta * temp / (Lamda + temp)))   #Calcul du point de rosée

    return dp   #retour du résultat

def csv_write_row(file_path, data_row): #Fonction d'écriture dans le dossier .CSV
     try:
     # Write csv here
        with open('TempLog.csv', 'a', newline='', encoding='utf-8') as f:    #Ouverture du dossier en mode écriture SANS effacer ce qui est déjà écrit en retour à la ligne
            writer = csv.writer(f, delimiter=',')                            #écrit dans le dossier avec une "," comme séparation des infos
            writer.writerow(data_row)                                        #écriture des informations données
            return 1
     except Exception as ex:
         print("erreur", ex)
         return 0
 
#-----------------------------------------------------
# Main script
#-----------------------------------------------------
if __name__ == "__main__":  # Runs only if called as a script but not if imported
    print("Hello and welcome to EMSY")
    temperature, humidity = read_sensor()                                                                        #Appel de la fonction de lecture de température et humidité
    dew_point = calculate_dew_point(temperature.degrees_celsius, humidity.percent_rh)                            #Appel de la fonction de calcul en donnant les informations
    print("Temperature :", temperature)                                                                          #Afficher la temperature
    print("Humidite relative :", humidity)                                                                       #Afficher la valeur de l'humidite relative
    print("Point de Rosee :", round(dew_point, 2), "°C")                                                         #Afficher le point de rosée
    
    date_heur = datetime.datetime.now()                                                                          #Lecture de la date
    ligne = [date_heur.strftime("%d-%m-%Y"), date_heur.strftime("%H:%M"), temperature, humidity, dew_point]      #Met tous les inofrmation dans un tableau
    csv_write_row('TempLog.csv', ligne)                                                                          #Appel de la fonction d'automatisation avec le nom du dossier et le tableau comme infos d'entrée
    
    if temperature > 15:
        send_email(receiver, subject, message)
    
