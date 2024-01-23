from pathlib import Path
from re import A

from tkinter import Frame, Tk
from controller import *
import controller as db_controller

from add_reservations.gui import AddReservations
from view_reservations.main import ViewReservations
from update_reservation.main import UpdateReservations
from billing.main import AddBilling

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def reservations():
    Reservations()


class Reservations(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.reservation_data = db_controller.get_reservations()
        self.reservation_id = 0
        self.configure(bg="#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            "add": AddReservations(self),
            "view": ViewReservations(self),
            "edit": UpdateReservations(self),
            "bill": AddBilling(self),
        }

        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1013.0, height=506.0)

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()
        if name == "bill":
            self.windows[name].canvas.itemconfigure(
                self.windows[name].id_text, text=self.reservation_id
            )
        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1013.0, height=506.0)

    def refresh_entries(self):
        self.reservation_data = db_controller.get_reservations()
        self.windows.get("view").handle_refresh()


if __name__ == "__main__":
    root = Tk()
    root.title("Rooms")
    root.geometry("1013x506")
    val = Reservations(root)
    val.place(x=0, y=0, width=1013.0, height=506.0)
    root.mainloop()
