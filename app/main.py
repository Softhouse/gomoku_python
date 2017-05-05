import controller
import events
import model
import view

HEIGHT = 6
WIDTH = 7


def run():
    evManager = events.EventManager()
    gamemodel = model.GameEngine(evManager, HEIGHT, WIDTH)
    graphics = view.GraphicalView(evManager, gamemodel, HEIGHT, WIDTH)
    keyboard = controller.UserInput(evManager, graphics)
    gamemodel.run()


if __name__ == '__main__':
    run()
