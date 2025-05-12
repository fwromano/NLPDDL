```pddl
(define (problem blocksworld-4ops-problem)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (hand-empty)
         (on a c)
         (on b table)
         (on c table)
         (clear a)
         (clear b))
  (:goal (on b a)))
```