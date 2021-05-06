# The Last Dream

### Working files
* some tests with object instantiation
* several prototypes of the pyxis game

### the most recent version of pyxis doesn't work as intended
* i think earlier versions do, but it's been so long since i created them and/or looked at them so i don't recall

## Here's what I'd like to get done:
* there are three main hint categories
* within each category there are several possibilities of the type of hint, save for one hint type
* i don't want the same hint to repeat itself, as that's stupid and inefficient
* i want one hint to be more rare than the rest
* _alot of this depends on the random number drawn_
* upon rolling a certain hint type, and upon a subcategory being used to convey the hint, i want to ensure that same hint can't come up again in the same game
* also: ensure that the same type of hint doesn't happen twice in a row

 * i.e. "you sense the answer is greater than X and less than Y" twice in a row
 * i.e. "you sense the first digit is odd" twice in a row

* those are purpose-defeating behaviours

#### i write this readme after years of not looking at this project or testing the code, so not sure how accurate all of those are, but i remember the problems because they pained me greatly
* the object test and dinky little class scripts were a method to learn and familiarize myself with objects (that is still greatly in the process)
* i also thought it would be fun to desing minor creatures and heroes and include snippets about them

#### repo structuring
* separate folders for heroes / monsters? break each one out into its own file?
* in pyxis dir, break out hint funcs into separate files? separate file for 'main' + dialogue?
