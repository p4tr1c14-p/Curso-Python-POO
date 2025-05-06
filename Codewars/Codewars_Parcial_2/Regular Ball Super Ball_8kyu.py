class Ball(object):

    #esta es la función se ejecuta automáticamente
    #cuando se crea un nuevo objeto de tipo ball
    def __init__(self, ball_type="regular"):
        #si noo se proporciona ningún valor al crear la pelota ball_type será regular por defecto

        #despues guardo el tipo de pelota en una variable interna del objeto llamada ball_type
        #y self representa al propio objeto que estoy creando 🤠
        self.ball_type = ball_type
