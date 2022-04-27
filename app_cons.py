def input_parameters(parameter_names):
    result = {}

    if 'Соотношение матрица-наполнитель' in parameter_names:
        parameter.pop('Соотношение матрица-наполнитель')

    for key, value in parameter_names.items():
        while True:
            text_value = input(
                f'Введите значение параметра "{key}": '
            )
            try:
                parameter_value = float(text_value)
                if parameter_value < 0.0 or parameter_value > 1.0:
                    raise ValueError('Out of range!')
                result[value] = parameter_value
                break

            except ValueError:
                print(
                    f'\tВведено недопустимое значение "{text_value}"!'
                )
    return result


if __name__ == '__main__':
    try:
        print('\n\n'
                    'Прогнозирование выходного параметра "Соотношение матрица-наполнитель"\n'
              )
        parameters = input_parameters(parameter_names)
        
        print(
            '\n\n'
            f'Соотношение матрица-наполнитель: {predicted_value[0][0]}'
        )

    except KeyboardInterrupt:
        print('\n\n'
              '\tВыполнение программы окончено.\n')
