```pddl
(define (problem blocksworld-problem)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on-table a)
         (on b a)
         (on-table c)
         (clear b)
         (clear c))
  (:goal (and (on a b)
              (on b c))))
```