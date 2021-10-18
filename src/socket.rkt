#lang racket

(define-values (in out) (tcp-connect  "127.0.0.1" 9876))
(define (msg line)
  (displayln line out)
  (flush-output out)
  (display "Response: ")
  (displayln (read-line in)))


(msg '("START" ("/" 0 "/" 0 "/" 10) ("/" 0 "/" 5 "/" 5)))
(close-input-port in)
(close-output-port out)