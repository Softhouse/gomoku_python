import controller
import events
import model
import view


def run():
    evManager = events.EventManager()
    gamemodel = model.GameEngine(evManager, 7, 6)
    graphics = view.GraphicalView(evManager, gamemodel, 7, 6)
    keyboard = controller.UserInput(evManager, graphics)
    gamemodel.run()


if __name__ == '__main__':
    run()
