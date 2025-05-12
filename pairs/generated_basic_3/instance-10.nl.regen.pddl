```pddl
(define (problem blocksworld-4ops-1)
  (:domain blocksworld-4ops)
  (:objects a b c - block)
  (:init (handempty)
         (on a table)
         (on b c)
         (on c table)
         (clear a)
         (clear b))
  (:goal (and (on a c)
              (on c b)))
)
```