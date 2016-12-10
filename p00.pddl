;; The arm is empty and there is a stack of three blocks: C is on B
;; which is on A which is on the table.  The goal is to reverse the
;; stack, i.e., have A on B and B on C.  We don't need to mention that
;; C is on the table, since the domain constraints will enforce it.

(define (problem 00)
  (:domain hw5)
  (:objects A B C)
  (:init (arm-empty)
         (block A)
	 (on-table A)
         (block B)
	 (on B A) 
         (block C)
	 (on C B)
	 (clear C))
  (:goal (and (on A B) (on B C))))