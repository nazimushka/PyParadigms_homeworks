sum([], 0).

sum([Head|Tail], Sum) :-
    sum(Tail, TempSum),
    Sum is Head + TempSum.

?- sum([1, 2, 3, 4, 5], Sum), write(Sum).