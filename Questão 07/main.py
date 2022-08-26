step_height = float(input("Informe a Altura do Degrau: "))
height_to_rise = float(input("Informe a Altura que Deseja Subir: "))

steps_to_climb = height_to_rise / step_height

print("Degraus a Subir para Alcanca o Objetivo: ", int(steps_to_climb))
