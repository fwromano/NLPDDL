```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on-table a)
         (on b a)
         (on c b)
         (clear c))
  (:goal (and (on a b)
              (on c a))))
```