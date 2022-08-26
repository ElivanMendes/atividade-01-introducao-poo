time = input("Informe a Hora de Inicio da Experiencia no Formato HH:mm:ss: ").split(":")
experience_duration = int(input("Informe a Duração da Experiencia em Segundos: "))

total_seconds = (int(time[0]) * 3600) + (int(time[1]) * 60) + int(time[2]) + experience_duration

h = int(total_seconds / 3600)
m = int((total_seconds % 3600) / 60)
s = int((total_seconds % 3600) % 60)

print("Horario de Termino da Experiencia: {:2}h:{:2}m:{:2}s".format(h, m, s))
