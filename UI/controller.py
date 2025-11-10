import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown_musei(self):
        self._view.museo_dropdown.options.clear()
        self._view.museo_dropdown.options.append(ft.dropdown.Option( None, "Nessun filtro"))
        for museo in self._model.get_musei():
            label = f"{museo.id} | {museo.nome} | Tipologia: {museo.tipologia}"
            self._view.museo_dropdown.options.append(ft.dropdown.Option(museo.id, label))
            self._view.museo_dropdown.value = None
        self._view.update()


    def popola_dropdown_epoche(self):
        self._view.epoca_dropdown.options.append(ft.dropdown.Option(None, "Nessun filtro"))
        for epoca in self._model.get_epoche():
            self._view.epoca_dropdown.options.append(ft.dropdown.Option(epoca))
            self._view.epoca_dropdown.value = None
        self._view.update()


    # CALLBACKS DROPDOWN
    def callback_musei(self, e):
        self.museo_selezionato = self._view.museo_dropdown.value


    def callback_epoche(self, e):
        self.epoca_selezionata = self._view.epoca_dropdown.value

    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        museo_val = self.museo_selezionato
        epoca_val = self.epoca_selezionata

        artefatti = self._model.get_artefatti_filtrati(museo_val, epoca_val)
        self._view.artefatti_container.controls.clear()
        if not artefatti:
            self._view.show_alert("Non esistono artefatti per questa selezione")
        else:
            for artefatto in artefatti:
                self._view.artefatti_container.controls.append(ft.Text(str(artefatto)))

        self._view.update()
    # TODO
