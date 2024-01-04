#!/usr/bin/env python3

class Vehiculo:

    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True
    
    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"\n[!] El vehículo con matricula {self.matricula} no se puede alquilar")
    

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"\n[!] El vehículo con matricula {self.matricula} no se puede devolver porque no ha sido alquilado a nadie")
    

    def __str__(self):
        return f"Vehículo (matricula = {self.matricula}, modelo = {self.modelo}, disponible = {self.disponible})"


class Flota:

    def __init__(self):
        self.vehiculos = [] # Lista de objetos
        
    
    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)


    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    
    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()
     

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)


if __name__ == "__main__":
    
    flota = Flota()
    flota.agregar_vehiculo(Vehiculo("BABDAS01", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("BABDAS02", "Honda Civic"))
    
    print(f"\n[+] Flota inicial:\n")
    print(flota)
    
    flota.alquilar_vehiculo("BABDAS01")
    print("\n[+] Mostrando la flota después de haber alquilado el Toyota\n")
    print(flota)
    
    print("\n[+] Mostrando la flota despues de que el cliente nos haya devuelto el Toyota:\n")
    flota.devolver_vehiculo("BABDAS01")
    print(flota)
