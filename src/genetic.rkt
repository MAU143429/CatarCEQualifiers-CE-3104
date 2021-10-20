#lang racket

#|Construye a un jugardor ingresando sus características en una lista.
id-player: número del jugador
id-team: equipo al que pertenece
desplazamiento: velocidad con la que corre en la cancha
fuerza: fuerza con la que le da a la bola
|#
(define (create-player id-player id-team)
  (list id-team id-player (list-ref (list 0 1 2 3 4 5 6 7 8 9 10) (random 10)) (list-ref (list 0 1 2 3 4 5 6 7 8 9 10) (random 10))))

; Crea la lista con los jugadores
(define (create-team total-players id-team total-generations)

  (cond ((< total-players 12)  
         
         (cons (genetic total-generations id-team total-players)(create-team (+ total-players 1) id-team total-generations)))))

; Busca el equipo especificado
(define (get-team id-team game)
  (cond ((= id-team 1)
         (car game))
        ((= id-team 2)
         (caddr game))
        (else
         (print "Número de equipo no identificado"))))

; Busca el jugador especificado con su id
(define (get-player team player-id)
  (cond ((= (cadar team) player-id)
         (car team))
        (else
         (get-player (cdr team) player-id))))

; Obtienen las características de un jugador especificado

(define (get-id-team player)
  (car player))

(define (get-id-player player)
  (cadr player))

(define (get-movement player)
  (caddr player))

(define (get-force player)
  (cadddr player))

(define (get-fitness player)
  (cadr(cdddr player)))

; Funcion de fitness:  
(define (fitness player)
  (list (get-id-team player) (get-id-player player)(get-movement player) (get-force player) (exact-round(/ (+ (* (get-movement player)(/ 75 100)) (* (get-force player)(/ 25 100))) 2))))


; Lista que contiene a los equipos que se van a enfrentar
(define (game team1 team2)
  (list team1 "/" team2))

; Elimina un elemento de la lista
(define (delete-player list player)
  (cond ((null? list)
         list)
        ((equal? (car list) player)
         (delete-player (cdr list) player)
         (cons (car list) (delete-player (cdr list) player)))))

; Obtiene una de las versiones del jugador de la poblacion del jugador del mismo tipo
(define (get-version-player population)
  (car population))

; Realiza la seleccion de los jugadores con mayor fitness
(define (selection population total-players)
  (cond ((> total-players 0)
         (cond ((> (get-fitness(car population)) 3)
                 (cons (car population) (selection (cdr population)(- total-players 1))))
               (else

                (selection (cdr population)(- total-players 1)))))))

; Crea el hijo
(define (create-child id-team id-player movement force)
  (list id-team id-player movement force))


; Cruce: realiza el cruce de las caracteristica entre dos jugadores
(define (cruce selected-players id-team id-player)
  
  (cond ((null? selected-players)
         (print "entra a null")
         selected-players)
        (else (cons (fitness(create-child id-team id-player
                       (exact-round(/ (+ (get-movement(car selected-players))(get-movement(car selected-players))) 2))
                       (exact-round(/ (+ (get-force (car selected-players))(get-force (car selected-players))) 2))))
        selected-players)))
)

; Crea la poblacion sobre la cual va a actuar el genetico
(define (create-population total-players id-team id-player)
  (cond ((> total-players 0)
         (cons (fitness (create-player id-player id-team)) (create-population (- total-players 1) id-team id-player)))))

; Aplica seleccion y cruce en el algoritmo genetico
(define (genetic total-generations id-team id-player)
  (list-ref (cruce(selection (create-population total-generations id-team id-player) total-generations) id-team id-player)
             (random 1)))


(game (create-team 1 1 20) (create-team 1 2 20))



#|(create-population 10 1)
(game (create-team 1 1) (create-team 1 2))
(get-team 2 (game (create-team 1 1) (create-team 1 2)))
(get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6)
(get-id-team (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))
(get-id-player (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))
(get-movement (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))
(get-force (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))|#
