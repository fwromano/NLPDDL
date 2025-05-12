```pddl
(define (problem blocksworld-4ops-problem)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on a b)
         (on b table)
         (on c a)
         (clear c))
  (:goal (on a c)))
```