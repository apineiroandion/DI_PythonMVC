import sys
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QIcon, QImage
from PyQt6.QtWidgets import QApplication

from app.EjemploQListView import EjemploQListView


class ModeloTareas(QAbstractListModel): # QAbstractListModel es una clase abstracta que se encarga de manejar los datos de una lista
    def __init__(self, tareas = None): #tarefas es una lista de tareas
        super().__init__()
        self.tareas = tareas or [] # Si no se pasa una lista de tareas, se crea una lista vacía

    #index es un objeto de tipo QModelIndex, role es un entero que indica el rol de los datos
    #QMoldelIndex es un objeto que se utiliza para acceder a los datos de un modelo, en este caso, de la lista de tareas
    #role es un entero que indica el rol de los datos, en este caso, se utiliza el rol DisplayRole que indica que se quiere mostrar el texto de la tarea
    #otros roles son EditRole, que indica que se quiere editar el texto de la tarea, y DecorationRole, que indica que se quiere mostrar un icono etc.
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole: # Si el rol es DisplayRole, se devuelve el texto de la tarea
            _, texto = self.tareas[index.row()] # Se obtiene el texto de la tarea
            return texto
        if role == Qt.ItemDataRole.DecorationRole:
            estado,_ = self.tareas[index.row()]
            if estado:
                imagen = QImage("check.png")
                imagen_scaled = imagen.scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                return imagen_scaled

    def rowCount(self, index): # Devuelve la cantidad de tareas
        return len(self.tareas) # Se devuelve la cantidad de tareas

