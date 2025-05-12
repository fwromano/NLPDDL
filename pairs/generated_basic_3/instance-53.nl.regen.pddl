```pddl
(define (problem blocksworld-4ops-problem)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on-table a)
         (on b a)
         (on-table c)
         (clear b)
         (clear c))
  (:goal (on b a)))
```