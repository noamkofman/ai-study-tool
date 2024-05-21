import pytesseract
from PIL import Image
import tkinter as tk
import keyboard
# below we do tkinter box stuff
# window = tk.Tk()
# window.geometry("600x650")

# label =  tk.Label(window, text = "Study AI", font = ('Arial', 24))
# label.pack()

# stringvar = tk.StringVar()
# stringvar.set('Drop here or drag from here!')

# def drop(event):
#     stringvar.set(event.data)




# button = tk.Button(window, text = "Drag file here", font=('Arial', 18))
# button.pack(padx=10, pady =10)
 # below we do tesseratct extract etxt from file
# Set the path to the Tesseract executable
image_file = input("Please download your notes and move the file to the vscode folder, then copy path. Paste path of your notes here **( Only supports png if unable to use png convert it to png) *** : ").strip()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the image file
image = Image.open(image_file)

# Use pytesseract to do OCR on the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
import google.generativeai as genai
api = 'AIzaSyAziI2y1UmCIkSi2oGkM_lCJ8jjjtQ9Dx4'
# above & below we deifne our api key and below 
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
# below we create the loop using varibale x to assure its only asked once
x = 1
while x == 1:
    # below is the uatomated message to gemini
    automatic_quiz = ("Make a  user interatcble quiz based of but do not give me the answer for :" + extracted_text)
    response = chat.send_message(automatic_quiz)
    print("AI:", response.text)

    x -1
    break
running = True
while running == True:
    user_res = input("You: ")
    user_response = chat.send_message(user_res)
    print("AI:  ", user_response.text)
    if keyboard.is_pressed("space"):
        break

y = 1
while y == 1:
    # below is the uatomated message to gemini
    answers = ("give me grade out of /100 based off my answers  " + user_res)
    response1 = chat.send_message(answers)
    print("AI:", response1.text)
    y -1




