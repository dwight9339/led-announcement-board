from rundisplay import SignController

ctlr = SignController()
ctlr.scrollRL("Test 1")
ctlr.reset()
ctlr.flyInTop("Test 2", color=(200, 255, 80))
ctlr.reset()
ctlr.flyInBottom("Test 3", 5, (233, 124, 79))
ctlr.reset()
