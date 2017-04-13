import eventmanager
import model
import view
import controller

def run():
    evManager = eventmanager.EventManager()
    gamemodel = model.GameEngine(evManager, 7, 6)
    graphics = view.GraphicalView(evManager, gamemodel, 7, 6)
    keyboard = controller.Keyboard(evManager, graphics)
    gamemodel.run()

if __name__ == '__main__':
    run()