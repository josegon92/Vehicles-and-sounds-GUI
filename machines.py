from PIL import ImageTk, Image
import tkinter
import pygame


# Initialize app
pygame.init()
window = tkinter.Tk()
window.title("Images and sounds")
window.resizable(0,0)
window.configure(background="#add8e6")

# Sounds
sounds = ["sounds/car.wav", "sounds/moto.wav", "sounds/airplane.wav", "sounds/boat.wav"]

def playSound(wav_file):
	sound = pygame.mixer.Sound(wav_file)
	sound.play()

def car_sound():
	playSound(sounds[0])

def motorcycle_sound():
	playSound(sounds[1])

def airplane_sound():
	playSound(sounds[2])

def boat_sound():
	playSound(sounds[3])


# Labels
label_options = ["Car", "Motorcycle", "Airplane", "Speed Boat"]
labels = [tkinter.Button(window, text=option, relief=tkinter.GROOVE, font="-weight bold") for option in label_options]

for index, label in enumerate(labels):
    label.grid(column=index, row=0, padx=5, pady=5)

brand_label = tkinter.Label(window, text="Gonzalez 2015. Boston, MA.", bg="darkgray", fg="black")
brand_label.grid(row=2, columnspan=len(label_options), sticky=tkinter.NSEW)


# Images
image_paths = ["images/car.png", "images/moto.jpg", "images/airplane.jpg", "images/boat.jpg"]
originals = [Image.open(path).resize((250,150), Image.ANTIALIAS) for path in image_paths]
resized = [ImageTk.PhotoImage(picture) for picture in originals]


#Buttons
buttons = [tkinter.Button(window, image= picture, relief=tkinter.GROOVE) for picture in resized]

buttons[0].config(command=car_sound)
buttons[1].config(command=motorcycle_sound)
buttons[2].config(command=airplane_sound)
buttons[3].config(command=boat_sound)

for index, button in enumerate(buttons):
	button.grid(column=index, row=1, padx=5, pady=5)

window.mainloop()















