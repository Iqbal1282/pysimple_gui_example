import os 
import sys 
sys.path.append("yolov5")
import PySimpleGUI as pg 
from yolov5.detect_gui import detect 



# step 1: ste the theme 
pg.theme("DarkAmber")

# step 2: create layout 
file_list_column = [
	[
		pg.Text("Folder"),
		pg.In(size= (30,1), enable_events = True, key = "-FOLDER-"),
		pg.FolderBrowse(),
	],
	[
		pg.Listbox(
			values =[],
			size = (50, 20), 
			key = "-FILE_LIST-",
			enable_events = True
			)

	]

]

# file_viwer_column = [
# 	[pg.Text("Choose a file from the list", size = (50,1))],
# 	[pg.Text("File name ", size = (70, 3), key = "-TOUT-")],
# 	[pg.Multiline(size = (70, 30), key = "-TEXT-")]
# ]

file_viwer_column2 = [
	[pg.Text("(Optional) Destination Folder Name: ", size =(20,5)), pg.InputText(size= (40,5), key = "-TARGET-"), pg.Button("OK", key = "OK")],

	[pg.Text("Detection from Selected Folder?", size = (30,1)),pg.Button("Yes", key = "OK1", size =(20,1))],
	[pg.Text("", key="-Folder_Done-")],
	[pg.Text("Detection from Selected Image?", size = (30,1)),pg.Button("Yes", key = "OK2", size = (20,1))],
	[pg.Text("", key= "-Image_Done-")],
	[pg.Text("Detection & Crop from Selected Folder?", size = (30,1)), pg.Button("Yes", key = "OK3", size =(20,1))],
	[pg.Text("", key="-Folder_Crop_Done-")],
	[pg.Text("Detection & Crop from Selected Image?", size = (30,1)),pg.Button("Yes", key = "OK4", size = (20,1))],
	[pg.Text("", key= "-Image_Crop_Done-")]
	
]


layout = [
	[
		pg.Column(file_list_column),
		pg.VSeperator(),
		#pg.Column(file_viwer_column),
		pg.VSeperator(),
		pg.Column(file_viwer_column2)
	]
]


# create window 
window = pg.Window("Signature GUI", layout)

# event monitoring 
folder_location = ''
save_to = False 

while True: 
	event, values = window.read()
	print(values)

	#detect()
	#detect("./data/images2")

	if event == pg.WIN_CLOSED or event == "Exit":
		break 

	elif event == "OK":
		save_to = values["-TARGET-"]
		print(save_to)

	elif event == "-FOLDER-":
		folder_location = values["-FOLDER-"]
		try: 
			files = os.listdir(folder_location)

		except: 
			files = []

		file_names = [
			file for file in files
			if os.path.isfile(os.path.join(folder_location, file))
		]
		#print(file_names)

		window["-FILE_LIST-"].update(file_names)

	elif event == "-FILE_LIST-":
		file_selection = values["-FILE_LIST-"][0]

	elif event == "OK1": # detection from from 
		
		if save_to: 

			window['-Folder_Done-'].update("Please Wait :)")
			detect(folder_location, save_to, isave_crop = False)
			window['-Folder_Done-'].update("Completed! :D")
		else: 
			window['-Folder_Done-'].update("Please Wait :)")
			detect(folder_location, "All_Results", isave_crop = False)
			window['-Folder_Done-'].update("Completed! :D")

		 
		
	elif event == "OK2": # detection from file 
		if save_to: 
			window['-Image_Done-'].update("Please Wait :)")
			target = "Output_" + file_selection.split(".")[0]
			detect(folder_location+"/"+ file_selection, save_to, isave_crop = False)
			window['-Image_Done-'].update("Completed! :D")
		else:
			window['-Image_Done-'].update("Please Wait :)")
			target = "Output_" + file_selection.split(".")[0]
			detect(folder_location+"/"+ file_selection, target, isave_crop = False)
			window['-Image_Done-'].update("Completed! :D")

		
	elif event == "OK3": # detection and crop entire folder 
		if save_to: 
			window['-Folder_Crop_Done-'].update("Please Wait :)")
			detect(folder_location, save_to, isave_crop = True)
			window['-Folder_Crop_Done-'].update("Completed! :D")
		else: 
			window['-Folder_Crop_Done-'].update("Please Wait :)")
			detect(folder_location, "ALL_Results_Croped", isave_crop = True)
			window['-Folder_Crop_Done-'].update("Completed! :D")
		
	elif event == "OK4": # detection a single image 
		if save_to: 
			window['-Image_Crop_Done-'].update("Please Wait :)")
			target = "Output_Croped_" + file_selection.split(".")[0]
			detect(folder_location +"/" + file_selection, save_to, isave_crop = True)
			window['-Image_Crop_Done-'].update("Completed! :D")
		else: 
			window['-Image_Crop_Done-'].update("Please Wait :)")
			target = "Output_Croped_" + file_selection.split(".")[0]
			detect(folder_location +"/" + file_selection, target, isave_crop = True)
			window['-Image_Crop_Done-'].update("Completed! :D")



# closing the window 

window.close()