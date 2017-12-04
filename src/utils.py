import time

def takePicture(savePic):
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
    if savePic: pygame.image.save(img, "./src/assets/captured.png")
    cam.stop()
    return img
