from views.view import View
from model import Model
from controller import Controller

if __name__ == '__main__':
    controller = Controller(View(), Model())
