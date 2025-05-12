```pddl
(define (problem blocksworld-4ops-problem)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on-table a)
         (on b c)
         (on-table c)
         (clear a)
         (clear b))
  (:goal (on a c)))
```