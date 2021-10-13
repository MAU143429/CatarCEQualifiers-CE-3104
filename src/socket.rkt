#lang racket

(define-values (in out) (tcp-connect  "127.0.0.1" 9876))
(define (msg line)
  (displayln line out)
  (flush-output out)
  (display "Response: ")
  (displayln (read-line in)))


(msg '( ( 6 7 8 9 1) "," (1 2 3 4 5) "///" (1 2 3 4 5) "," (1 2 3 4 5)))
(msg "ESP32 rocks")
(msg "HOLA SOY LAS PROXIMAS GENERACIONES DE CATAR CE QUALIFIERS")
(close-input-port in)
(close-output-port out)