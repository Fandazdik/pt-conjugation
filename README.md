# pt-conjugation
Module that provides function to conjugate Portuguese verbs

## `conjugate(verb, pers, tense)`
*DOES NOT ACCURATELY CONJUGATE IRREGULAR VERBS YET*

Takes in string input for verb (can be anything so long as it ends in 'ar', 'er', or 'ir')

Takes in a person: `[EU, ELAE, TU, NOS, ELESAS]` (elae works as ela/e, similarly for elesas as eles/as)

Takes in a tense: `[PRESENT, PRETERITE, IMPERFECT, PLUPERFECT, FUTURE, CONDITIONAL, PRESENTSUBJECTIVE, IMPERFECTSUBJECTIVE, FUTURESUBJECTIVE]`

Returns a conjugated verb.

### Examples
`conjugate('seguir', ELAE, PRESENTSUBJECTIVE)` -> `segues`

`conjugate('dormir', NOS, IMPERFECT)` -> `dormiamos`

`conjugate('cozinhar', EU, CONDITIONAL)` -> `cozinharia`
