```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on-table a)
         (on b c)
         (on-table c)
         (clear a)
         (clear b))
  (:goal (on a c)))
```