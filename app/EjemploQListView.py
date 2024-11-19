import sys

from PyQt6.QtWidgets import QListView, QVBoxLayout, QApplication, QHBoxLayout, QPushButton, QWidget, QMainWindow, \
    QLineEdit


class EjemploQListView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.show()

        self.setWindowTitle("Ejemplo QListView")
        lista_tareas = [(False, "Ir al gimnasio"), (False, "Hacer la compra"), (False, "Estudiar para el examen")]
        from app.Main import ModeloTareas
        self.modelo = ModeloTareas(lista_tareas)

        caja_v = QVBoxLayout()

        self.lista_tareas = QListView()
        self.lista_tareas.setModel(self.modelo)
        self.lista_tareas.setSelectionMode(QListView.SelectionMode.MultiSelection)

        contenedor = QWidget()
        contenedor.setLayout(caja_v)
        self.setCentralWidget(contenedor)

        caja_v.addWidget(self.lista_tareas)

        caja_h = QHBoxLayout()

        btn_borrar = QPushButton("Borrar")
        btn_borrar.pressed.connect(self.on_btn_borrar_pressed)

        btn_feito = QPushButton("Feito")
        btn_feito.pressed.connect(self.on_btn_feito_pressed)

        self.text_field = QLineEdit()

        btn_add_tarea = QPushButton("Nueva Tarea")
        btn_add_tarea.pressed.connect(self.on_btn_add_tarea_pressed)

        caja_h.addWidget(btn_borrar)
        caja_h.addWidget(btn_feito)
        caja_v.addLayout(caja_h)
        caja_v.addWidget(self.text_field)
        caja_v.addWidget(btn_add_tarea)

    def on_btn_add_tarea_pressed(self):
        texto = self.text_field.text()
        if texto:
            self.modelo.tareas.append((False, texto))
            self.modelo.layoutChanged.emit()
            self.text_field.clear()

    def on_btn_borrar_pressed(self):
        indices = self.lista_tareas.selectedIndexes()
        for index in sorted(indices, reverse=True):
            self.modelo.tareas.pop(index.row())
        self.modelo.layoutChanged.emit()
        self.lista_tareas.clearSelection()

    def on_btn_feito_pressed(self):
        indices = self.lista_tareas.selectedIndexes()
        for index in indices:
            hecho, texto = self.modelo.tareas[index.row()]
            if hecho:
                self.modelo.tareas[index.row()] = (False, texto)
            else:
                self.modelo.tareas[index.row()] = (True, texto)
        self.modelo.layoutChanged.emit()
        self.lista_tareas.clearSelection()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = EjemploQListView()
    app.exec()
