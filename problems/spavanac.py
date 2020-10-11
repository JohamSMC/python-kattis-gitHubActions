from datetime import datetime, date, time, timedelta
def main():
	hour, minutes = list(map(int,input().split()))

	fechaAux= datetime(2000,1,1,hour,minutes,0,0)
	horaAux = time(fechaAux.hour,fechaAux.minute,fechaAux.second)
	tiempoRestado=fechaAux-timedelta(seconds=(60*45))
	tiempoRestado=time(tiempoRestado.hour,tiempoRestado.minute,tiempoRestado.second)
	print(str(tiempoRestado.hour),str(tiempoRestado.minute))

if __name__ == '__main__':
	main()