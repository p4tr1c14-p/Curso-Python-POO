def better_than_average(class_points, your_points):
    #primero calculo la suma de las notas de todos los compañeros de clase
    total_points = sum(class_points)

    #añado los puntos a la suma para obtener el total con los puntos
    total_points += your_points

    #calculamos el número total de estudiantes incluyendome jeje
    total_students = len(class_points) + 1  #+1 porque también cuento

    #calculamos el promedio de la clase incluyendome
    average = total_points / total_students

    #comparo mis puntos con el promedio
    return your_points > average
