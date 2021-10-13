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
  (list id-player id-team 0 0 0))

(define (create-team total-players id-team)

  (cond ((< total-players 12)  
         
         (cons (create-player total-players id-team) (create-team (+ total-players 1) id-team)))))

; Lista que contiene a los equipos que se van a enfrentar
(define (game team1 team2)
  (list team1 "/" team2))

(game (create-team 1 1) (create-team 1 2))

; Busca el equipo especificado
(define (check-team id-team game)
  (cond ((= id-team 1)
         (car game))
        ((= id-team 2)
         (cadr game))
        (else
         (print "Número de equipo no identificado"))))

; Busca el jugador especificado
#|
(define (check-player id-team id-player)
  )
|#