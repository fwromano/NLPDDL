```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on-table a)
         (on-table b)
         (on c b)
         (clear a)
         (clear c))
  (:goal (on a b)))
```