```pddl
(define (problem blocksworld-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (empty-hand)
         (on-table a)
         (on-table b)
         (on c a)
         (clear b)
         (clear c))
  (:goal (on a b)))
```