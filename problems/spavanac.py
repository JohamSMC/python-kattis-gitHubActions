from datetime import datetime, time, timedelta


def main():
    hour, minutes = list(map(int, input().split()))

    fecha_aux = datetime(2000, 1, 1, hour, minutes, 0, 0)
    # horaAux = time(fecha_aux.hour, fecha_aux.minute, fecha_aux.second)
    tiempo_restado = fecha_aux-timedelta(seconds=(60*45))
    tiempo_restado = time(tiempo_restado.hour, tiempo_restado.minute, tiempo_restado.second)
    print(str(tiempo_restado.hour), str(tiempo_restado.minute))


if __name__ == '__main__':
    main()
