import pygame.camera
import time
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
time.sleep(2)
cam.start()
img = cam.get_image()
import pygame.image
pygame.image.save(img, "./src/assets/captures.png")
cam.stop()
