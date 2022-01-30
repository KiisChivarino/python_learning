while True:
    userSeconds = input('Введите время в секундах\n')
    try:
        seconds = int(userSeconds)
        break
    except ValueError:
        print(f'Значение [{userSeconds}] не является целым числом!')
        continue
print(
    str('{0}:{1}:{2}').format(
        str((seconds // 60 // 60)).zfill(2),
        str((seconds // 60) % 60).zfill(2),
        str(seconds % 60).zfill(2)
    )
)
