#!/usr/bin/env python3

class Animal:

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False
    
    def alimentar(self):
        self.alimentado = True

    def vender(self):
        self.alimentado = False


    def __str__(self):
        return f"{self.nombre} - ({self.especie}) - {'Alimentado' if  self.alimentado else 'Hambriento'}"


class TiendaAnimales:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []


    def agregar_animal(self, animal):
        self.animales.append(animal)


    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)


    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                self.animales.remove(animal)
                return 
        
        print(f"\n[!] No se ha encontrado ningun animal con nombre {nombre}\n")



if __name__ == "__main__":
    

    tienda = TiendaAnimales("Mi tienda de animales")
    
    gato = Animal("Tijuana", "Gato")
    perro = Animal("Juan", "Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    tienda.mostrar_animales()
    tienda.alimentar_animales()
    
    print(f"\n[+] Monstrando los animales una vez estos han sido alimentados:\n")

    tienda.mostrar_animales()
    tienda.vender_animal("Tijuana")

    print(f"\n[+] Mostrando los animales una vez Tijuana ha sido vendido\n")
    tienda.mostrar_animales()
