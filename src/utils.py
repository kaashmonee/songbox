import time

def takePicture(path="./assets/captured.png"):
    import pygame.camera
    # print(Form)
    pygame.camera.init()
    # taking the image by initializing the camera location
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    # sleeping
    time.sleep(2)
    cam.start()
    # grabbing the image
    img = cam.get_image()
    import pygame.image
    # saving the image if the user wants to save it. otherwise, it is returned
    pygame.image.save(img, path)
    cam.stop()
    return img
