#lang racket

#|Construye a un jugardor ingresando sus características en una lista.
id-player: número del jugador
id-team: equipo al que pertenece
position: posición en el mapa
desplazamiento: velocidad con la que corre en la cancha
fuerza: fureza con la que le da a la bola
3rd:
|#
(define (create-player id-player id-team)
  (list id-player id-team 4 3 2))


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
  (cond ((= (caar team) player-id)
         (car team))
        (else
         (get-player (cdr team) player-id))))



; Obtienen las características de un jugador especificado
(define (get-id-player player)
  (car player))

(define (get-id-team player)
  (cadr player))

(define (get-position player)
  (caddr player))

(define (get-movement player)
  (cadddr player))

(define (get-force player)
  (cadr(cdddr player)))


(print "Genetico")

; Genetic Algorithm definition


; Fitness 
(define (fitness player)
  (list (get-id-player player) (get-id-team player) (get-position player) (get-movement player) (get-force player) (/ (+ (* (get-movement player)(/ 75 100)) (* (get-force player)(/ 25 100))) 2)))

(define (create-team total-players id-team)

  (cond ((< total-players 12)  
         
         (cons (fitness (create-player total-players id-team)) (create-team (+ total-players 1) id-team)))))

; Lista que contiene a los equipos que se van a enfrentar
(define (game team1 team2)
  (list team1 "/" team2))

(game (create-team 1 1) (create-team 1 2))

(get-team 2 (game (create-team 1 1) (create-team 1 2)))
(get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6)
(get-id-player (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-id-team (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-position (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-movement (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))

(get-force (get-player (get-team 1 (game (create-team 1 1) (create-team 1 2))) 6))