;; There is only one block, A, which is on the table.  A sprayer with
;; red paint is on the table.  Our goal is to have A be red and the
;; arm empty.

(define (problem 0)
  (:domain hw5)
  (:objects blockA redSprayer)
  (:init (arm-empty)
         (block blockA)
         (clear blockA)
         (on-table blockA)
         (sprayer redSprayer red)
         (clear redSprayer)
         (on-table redSprayer)
         )
  (:goal (and (arm-empty)
              (color blockA red)
              (clear blockA)
          )))