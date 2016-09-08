import bge

cont = bge.logic.getCurrentController()
objeto = cont.owner

barra = cont.sensors["Keyboard"]
accion = cont.actuators["Action"]

if barra.positive:
    cont.activate(accion)