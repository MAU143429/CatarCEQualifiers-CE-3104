#lang racket

#|Construye a un jugardor ingresando sus características en una lista.
id-player: número del jugador
id-team: equipo al que pertenece
position: posición en el mapa
desplazamiento: velocidad con la que corre en la cancha
fuerza: fuerza con la que le da a la bola
|#
(define (create-player id-player id-team)
  (list id-team id-player 4 (list-ref (list 0 1 2 3 4 5 6 7 8 9 10) (random 10)) (list-ref (list 0 1 2 3 4 5 6 7 8 9 10) (random 10))))

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
(define (get-id-player player)
  (cadr player))

(define (get-id-team player)
  (car player))

(define (get-position player)
  (caddr player))

(define (get-movement player)
  (cadddr player))

(define (get-force player)
  (cadr(cdddr player)))

(define (get-fitness player)
  (caddr(cdddr player)))

; Realiza la seleccion de los jugadores con mayor fitness
(define (selection player)
  (cond ((> (get-fitness player) 3)
         (list (get-id-team player) (get-id-player player)(get-position player)(get-movement player)(get-force player)(get-fitness player)))
        
  ))

; Cruce: realiza el cruce de las caracteristica entre dos jugadores
(define (cruce player)
  (list (get-id-team player)(get-id-player player)(get-position player)(/ (+ (get-movement player)(get-movement player)) 2) (/ (+ (get-force player)(get-force player)) 2)))

; Funcion de fitness:  
(define (fitness player)
  (list (get-id-team player) (get-id-player player) (get-position player) (get-movement player) (get-force player) (exact-round(/ (+ (* (get-movement player)(/ 75 100)) (* (get-force player)(/ 25 100))) 2))))

; Crea la lista con los jugadores
(define (create-team total-players id-team)

  (cond ((< total-players 12)  
         
         (cons (create-player total-players id-team) (create-team (+ total-players 1) id-team)))))

; Lista que contiene a los equipos que se van a enfrentar
(define (game team1 team2)
  (list team1 "/" team2))

; Crea la poblacion sobre la cual va a actuar el genetico
(define (create-population total-players id-team)
  (cond ((> total-players 0)
         (cons (fitness (create-player total-players id-team)) (create-population (- total-players 1) id-team)))))
(create-population 10 1)
#|
(game (create-team 1 1) (create-team 1 2))

(get-team 2 (game (create-team 1 1) (create-team 1 2)))
(get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6)
(get-id-player (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-id-team (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-position (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-movement (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-force (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))|#