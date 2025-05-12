```pddl
(define (problem blocksworld-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (empty-hand)
         (on-table a)
         (on-table b)
         (on c b)
         (clear a)
         (clear c))
  (:goal (on c b)))
```