import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas

    def __str__(self):
        return f"Vehículo - Marca: {self.marca}, Modelo: {self.modelo}, Número de Ruedas: {self.numero_ruedas}"

    def guardar_datos_csv(self):
        with open('vehiculos.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.__class__.__name__, self.marca, self.modelo, self.numero_ruedas])


    def leer_datos_csv(self):
        try:
            with open('vehiculos.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == 'Automovil':
                        print(f"Automóvil: Marca - {row[1]}, Modelo - {row[2]}, Número de Ruedas - {row[3]}, Velocidad - {row[4]}, Cilindrada - {row[5]}")
                    elif row[0] == 'AutomovilParticular':
                        print(f"Automóvil Particular: Marca - {row[1]}, Modelo - {row[2]}, Número de Ruedas - {row[3]}, Velocidad - {row[4]}, Cilindrada - {row[5]}, Número de Puesto - {row[6]}")
                    elif row[0] == 'AutomovilCarga':
                        print(f"Automóvil de Carga: Marca - {row[1]}, Modelo - {row[2]}, Número de Ruedas - {row[3]}, Velocidad - {row[4]}, Cilindrada - {row[5]}, Peso de Carga - {row[6]} kg")
                    elif row[0] == 'Bicicleta':
                        print(f"Bicicleta: Marca - {row[1]}, Modelo - {row[2]}, Número de Ruedas - {row[3]}, Tipo de Bicicleta - {row[4]}")
                    elif row[0] == 'Motocicleta':
                        print(f"Motocicleta: Marca - {row[1]}, Modelo - {row[2]}, Número de Ruedas - {row[3]}, Tipo de Bicicleta - {row[4]}, Número de Radios - {row[5]}, Cuadro - {row[6]}, Motor - {row[7]}")
        except FileNotFoundError:
            print("El archivo 'vehiculos.csv' no se encuentra.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Automóvil - Marca: {self.marca}, Modelo: {self.modelo}, Número de Ruedas: {self.numero_ruedas}, Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}"


class AutomovilParticular(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, numero_puesto):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puesto = numero_puesto

    def __str__(self):
        return f"Automóvil Particular - Marca: {self.marca}, Modelo: {self.modelo}, Número de Ruedas: {self.numero_ruedas}, Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}, Número de Puesto: {self.numero_puesto}"


class AutomovilCarga(Automovil):
    def __init__(self, marca, modelo, numero_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Automóvil de Carga - Marca: {self.marca}, Modelo: {self.modelo}, Número de Ruedas: {self.numero_ruedas}, Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}, Peso de Carga: {self.peso_carga} kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

    def __str__(self):
        return f"Bicicleta - Marca: {self.marca}, Modelo: {self.modelo}, Número de Ruedas: {self.numero_ruedas}, Tipo de Bicicleta: {self.tipo_bicicleta}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"Motocicleta - Marca: {self.marca}, Modelo: {self.modelo}, Número de Ruedas: {self.numero_ruedas}, Tipo de Bicicleta: {self.tipo_bicicleta}, Número de Radios: {self.nro_radios}, Cuadro: {self.cuadro}, Motor: {self.motor}"


def main():
    vehiculo1 = Vehiculo("Toyota", "Corolla", 4)
    vehiculo2 = Vehiculo("Ford", "Mustang", 4)
    automovil1 = Automovil("Chevrolet", "Camaro", 4, 250, 3500)
    automovil_particular = AutomovilParticular("Honda", "Civic", 4, 180, 2000, 3)
    automovil_carga = AutomovilCarga("Volvo", "Truck", 6, 120, 12000, 8000)
    bicicleta_urbana = Bicicleta("Trek", "Urban", 2, "Urbana")
    motocicleta = Motocicleta("Harley-Davidson", "Sportster", 2, "De Carrera", 21, "Doble Viga", "4T")

    particular = AutomovilParticular("Ford", "Fiesta", "4", "180", "500", "5")
    carga = AutomovilCarga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "De Carrera", 21, "Doble Viga", "4T")

    motocicleta = Motocicleta("Harley-Davidson", "Sportster", 2, "De Carrera", 21, "Doble Viga", "4T")

    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, AutomovilParticular)}")
    print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta, AutomovilCarga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    particular.guardar_datos_csv()
    carga.guardar_datos_csv()
    bicicleta.guardar_datos_csv()
    motocicleta.guardar_datos_csv()


if __name__ == "__main__":
    main()
