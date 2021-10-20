#lang racket
(require "genetic.rkt")

(define-values (in out) (tcp-connect  "127.0.0.1" 9876))
(define (msg line)
  (displayln line out)
  (flush-output out)
  (display "Response: ")
  (displayln (read-line in)))

(define (num-games gen)
  (msg (game (create-team 1 1 20) (create-team 1 2 20)))
  (sleep 5)
  (cond (> gen 0)
        (num-games (- gen 1))))

(define (CCEQ equipo-1 equipo-2 generaciones)
  (msg '("START" ("/" (car equipo-1) "/" (cadr equipo-1) "/" (caddr equipo-1))
                 ("/" (car equipo-2) "/" (cadr equipo-2) "/" (caddr equipo-2))))
  (num-games generaciones))

#|
(msg '("START" ("/" 4 "/" 4 "/" 2) ("/" 4 "/" 3 "/" 3)))

(sleep 6)

(msg '((1 1 5 4)
       (1 2 7 1)
       (1 3 3 9)
       (1 4 5 3)
       (1 5 3 6)
       (1 6 1 1)
       (1 7 8 8)
       (1 8 2 3)
       (1 9 4 4)
       (1 10 6 5)
       (1 11 7 3)
       /
       (2 1 5 4)
       (2 2 7 1)
       (2 3 3 9)
       (2 4 5 3)
       (2 5 3 6)
       (2 6 1 1)
       (2 7 8 8)
       (2 8 2 3)
       (2 9 4 4)
       (2 10 6 5)
       (2 11 7 3)))
|#
(close-input-port in)
(close-output-port out)