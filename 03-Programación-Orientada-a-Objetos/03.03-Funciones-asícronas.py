#################################################
#            Procesamiento síncrono             #
#################################################

def main():
    print("Hola...")
    print("...Adios")

print("Incio Sync")
main()
print("Fin Sync")
print("")



#################################################
#            Procesamiento asíncrono            #
#################################################

import asyncio

async def main(): #marcamos la función como asíncrona
    print("Hola...")
    await asyncio.gather(func1(), func2()) #Llamamos a las FUNC1-2 aquí, porque el hilo principal es síncrono por definición y no funcionaría
    print("...Adios")

async def func1():
    print("F1A")
    await asyncio.sleep(5) #Las otras lineas seguirá mientras está espera
    print("F1B")

async def func2():
    print("F2A")
    for i in range (1,10):
        print(f"async func2-> {i}")
        await asyncio.sleep(0.6) #Esperará medio segundo entre cada FOR
    print("F2B")

print("Incio Async")
asyncio.run(main()) #Lanza las tareas en asíncrono

print("Fin Async")
print("")